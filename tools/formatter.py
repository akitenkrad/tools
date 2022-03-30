import json
from os import PathLike
from pathlib import Path


class Formatter(object):

    @classmethod
    def format(cls, path: PathLike, **kwargs):
        _path: Path = Path(path)
        if _path.suffix == '.json':
            return Formatter.__format_json(_path, **kwargs)

    @classmethod
    def __format_json(cls, path: Path, ensure_ascii=False, indent=2, **kwargs) -> str:
        json_data = json.load(open(path))
        return json.dumps(json_data, ensure_ascii=ensure_ascii, indent=indent, **kwargs)
