![Version](https://img.shields.io/badge/tools-v.0.1.0-blue?style=for-the-badge)
![Size](https://img.shields.io/github/repo-size/akitenkrad/tools?style=for-the-badge)
![License](https://img.shields.io/github/license/akitenkrad/tools?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/akitenkrad/tools?style=for-the-badge)

# tools
tools for AI engineers

## Install

```bash
$ pip install git+https://github.com/akitenkrad/tools
```

## Tools

<details>
<summary>format</summary>

```text
Usage: tools format [OPTIONS]

Options:
  --input-file PATH  path to input file [.json]
  --ensure-ascii     [.json] if True, ensure only ascii characters
  --indent INTEGER   [.json] indent, default=2
  --help             Show this message and exit.
```
</details>

<details>
<summary>hash</summary>

```text
Options:
  --input TEXT                    input text or file
  --hash-type [md5|sha1|sha256|sha512]
                                  hash type
  --help                          Show this message and exit.
```
</details>

<details>
<summary>show-processors</summary>

```text
Usage: tools show-processors [OPTIONS]

Options:
  --help  Show this message and exit.
```
</details>

<details>
<summary>sort</summary>

```text
Usage: tools hash [OPTIONS]Usage: tools sort [OPTIONS]

Options:
  --input TEXT  input text file
  --reverse     sort in descending order
  --overwrite   overwrite the input file with sorted results
  --help        Show this message and exit.
```
</details>

<details>
<summary>to-json</summary>

```text
Usage: tools to-json [OPTIONS]

Options:
  --file PATH  input file [yaml, toml]
  --help       Show this message and exit.
```
</details>

<details>
<summary>to-toml</summary>

```text
Usage: tools to-toml [OPTIONS]

Options:
  --file PATH  input file [yaml, toml]
  --help       Show this message and exit.
```
</details>

<details>
<summary>to-yaml</summary>

```text
Usage: tools to-yaml [OPTIONS]

Options:
  --file PATH  input file [yaml, toml]
  --help       Show this message and exit.
```
</details>

<details>
<summary>sync-to-gdrive</summary>

```text
Usage: python -m tools.cli sync-to-gdrive [OPTIONS]

  sync local directory to Google Drive

  YOU NEED "client_secret.json" file. See
  https://developers.google.com/drive/api/quickstart/python

Options:
  --secret PATH   client_secret.json for GCP
  --src-dir PATH  local source directory
  --dst-dir PATH  destination directory path for Google Drive
  --help          Show this message and exit.
```
</details>

<details>
<summary>sync-from-gdrive</summary>

```text
Usage: python -m tools.cli sync-from-gdrive [OPTIONS]

  sync Google Drive to local directory

Options:
  --id TEXT            google drive object id  [required]
  --dst-filename PATH  file name to save the object  [required]
  --help               Show this message and exit.
```
</details>