import json
from glob import glob
from os import PathLike, linesep
from pathlib import Path

import click
from tqdm import tqdm

from tools.converter import json2toml, json2yaml, toml2json, toml2yaml, yaml2json, yaml2toml
from tools.formatter import Formatter
from tools.hash import HashType, get_hash
from tools.utils import check, describe_cpu, describe_gpu


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--input-file", type=click.Path(exists=True), default="", help="path to input file [.json]", required=True
)
@click.option("--ensure-ascii", is_flag=True, help="[.json] if True, ensure only ascii characters", required=True)
@click.option("--indent", type=int, default=2, help="[.json] indent, default=2", required=True)
def format(input_file: PathLike, ensure_ascii, indent):
    formatted_text = Formatter.format(input_file, ensure_ascii=ensure_ascii, indent=indent)
    print(formatted_text)


@cli.command()
@click.option(
    "--input",
    type=str,
    default="Answer to the Ultimate Question of Life, the Universe, and Everything",
    help="input text or file",
    required=True,
)
@click.option(
    "--hash-type",
    type=click.Choice(["md5", "sha1", "sha256", "sha512"]),
    default="md5",
    help="hash type",
    required=True,
)
def hash(input: str, hash_type: str):
    if Path(input).exists():
        text = open(input).read()
    else:
        text = input

    target_hash = {h.value: h for h in HashType}
    hash_value = get_hash(text, target_hash[hash_type])
    print(hash_value)


@cli.command()
@click.option("--input", type=str, help="input text file", required=True)
@click.option("--reverse", is_flag=True, help="sort in descending order")
@click.option("--overwrite", is_flag=True, help="overwrite the input file with sorted results")
def sort(input: str, reverse: bool, overwrite: bool):
    if Path(input).suffix == ".json":
        text = [line.strip() for line in json.load(open(input))]
    else:
        text = [line.strip() for line in open(input).read().split(linesep)]
    text = sorted(text, reverse=reverse)

    print(linesep.join(text))

    if overwrite:
        with open(input, mode="wt", encoding="utf-8") as wf:
            wf.write(linesep.join(text))


@cli.command()
def show_processors():
    describe_cpu()
    describe_gpu()


@cli.command()
@click.option("--file", type=click.Path(exists=True), help="input file [yaml, toml]", required=True)
def to_json(file):
    filepath = Path(file)
    if filepath.suffix in [".yml", ".yaml"]:
        res = yaml2json(filepath)
    elif filepath.suffix in [".tml", ".toml"]:
        res = toml2json(filepath)
    else:
        raise RuntimeError(f"Unknown file format: {filepath.suffix}")
    print(res)


@cli.command()
@click.option("--file", type=click.Path(exists=True), help="input file [yaml, toml]", required=True)
def to_yaml(file):
    filepath = Path(file)
    if filepath.suffix in [".json"]:
        res = json2yaml(filepath)
    elif filepath.suffix in [".tml", ".toml"]:
        res = toml2yaml(filepath)
    else:
        raise RuntimeError(f"Unknown file format: {filepath.suffix}")
    print(res)


@cli.command()
@click.option("--file", type=click.Path(exists=True), help="input file [yaml, toml]", required=True)
def to_toml(file):
    filepath = Path(file)
    if filepath.suffix in [".yaml", ".yml"]:
        res = yaml2toml(filepath)
    elif filepath.suffix in [".json"]:
        res = json2toml(filepath)
    else:
        raise RuntimeError(f"Unknown file format: {filepath.suffix}")
    print(res)


if __name__ == "__main__":
    cli()
