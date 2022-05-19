import mimetypes
from os import PathLike
from pathlib import Path
from typing import Any, Dict, List

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import client as oauth_client
from oauth2client import file as oauth_file
from oauth2client import tools as oauth_tools
from tqdm import tqdm


def prepare_gdrive(secret_path: PathLike):
    token_cache = Path("~/__cache__/token.json").expanduser()
    token_cache.parent.mkdir(parents=True, exist_ok=True)

    store = oauth_file.Storage(str(token_cache))
    creds = store.get()
    if not creds or creds.invalid:
        flow = oauth_client.flow_from_clientsecrets(str(secret_path), ["https://www.googleapis.com/auth/drive"])
        creds = oauth_tools.run_flow(flow, store)
    service = build("drive", "v3", http=creds.authorize(Http()))

    return service


def get_directory(service, dir_path: str):
    try:
        dir_list = dir_path.split("/")
        parent = ""
        for dir_name in dir_list:

            query = f"mimeType='application/vnd.google-apps.folder' and trashed=false and name='{dir_name}'"
            if parent:
                query += f" and '{parent}' in parents"

            directories = []
            page_token = None
            while True:
                response = (
                    service.files()
                    .list(
                        q=query,
                        spaces="drive",
                        fields="nextPageToken, files(id)",
                        pageToken=page_token,
                    )
                    .execute()
                )
                for f in response.get("files", []):
                    directories.append(f.get("id"))
                page_token = response.get("nextPageToken", None)
                if page_token is None:
                    break
            if len(directories) == 0:
                return ""
            elif len(directories) > 1:
                raise RuntimeError(f"more than one directories were found: {dir_path}")
            parent = directories[0]
    except HttpError:
        return ""
    except Exception as ex:
        raise ex

    return directories[0]


def create_directory(service, dir_path: str, parents=[]):
    directories = dir_path.split("/")
    parent_id = ""
    parent_dirs: List[str] = []
    for dir_name in directories:
        if len(parent_dirs) > 0:
            target_dir = get_directory(service, f"{'/'.join(parent_dirs)}/{dir_name}")
        else:
            target_dir = get_directory(service, f"{dir_name}")
        if target_dir == "":
            metadata: Dict[str, Any] = {
                "name": dir_name,
                "mimeType": "application/vnd.google-apps.folder",
            }
            if parent_id:
                metadata["parents"] = [parent_id]
            res = service.files().create(body=metadata, fields="id").execute()
            parent_id = res["id"]
        else:
            parent_id = target_dir
        parent_dirs.append(dir_name)

    return parent_id


def upload_file(service, src_path: str, dst_path: str):
    parent_dir = "/".join(dst_path.split("/")[:-1])
    file_name = dst_path.split("/")[-1]

    metadata: Dict[str, Any] = {
        "name": file_name,
    }

    if parent_dir:
        parent_id = create_directory(service, parent_dir)
        metadata["parents"] = [parent_id]

    media = MediaFileUpload(src_path, mimetype=mimetypes.guess_type(file_name)[0], resumable=True)

    res = service.files().create(body=metadata, media_body=media, fields="id").execute()
    file_id = res.get("id")

    return file_id


def upload_files(service, src_files: List[str], src_dir: str, dst_dir: str):
    dir_map: Dict[str, str] = {}
    with tqdm(src_files, desc="Uploading...") as it:
        for src_file in it:
            it.set_description(f"Uploading {Path(src_file).name}...")

            actual_src_dir = str(Path(src_file).parent).replace(str(Path(src_dir)) + "/", "")
            actual_dst_dir = str(Path(dst_dir) / actual_src_dir)
            if actual_dst_dir not in dir_map:
                dir_id = create_directory(service, actual_dst_dir)
                dir_map[actual_dst_dir] = dir_id
            dir_id = dir_map[actual_dst_dir]

            assert Path(src_file).exists()
            metadata = {"name": Path(src_file).name, "parents": [dir_id]}
            media = MediaFileUpload(src_file, mimetype=mimetypes.guess_type(src_file)[0], resumable=True)
            res = service.files().create(body=metadata, media_body=media, fields="id").execute()
            assert res.get("id") != ""
