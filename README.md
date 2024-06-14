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
<summary>to-csv</summary>

```text
Usage: tools to-csv [OPTIONS]

Options:
  --file PATH  input file [json]  [required]
  --help       Show this message and exit.
```
</details>
