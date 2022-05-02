import json
from os import PathLike
from pathlib import Path

import toml
import yaml


def json2toml(filepath: PathLike):
    content_json = json.load(open(filepath))
    content_toml = toml.dumps(content_json)
    print(content_toml)


def toml2yaml(filepath: PathLike):
    content_toml = toml.load(open(filepath))
    content_yaml = yaml.safe_dump(content_toml)
    print(content_yaml)


def yaml2json(filepath: PathLike):
    content_yaml = yaml.safe_load(open(filepath))
    content_json = json.dumps(content_yaml)
    print(content_json)


def json2yaml(filepath: PathLike):
    content_json = json.load(open(filepath))
    content_yaml = yaml.safe_dump(content_json)
    print(content_yaml)


def yaml2toml(filepath: PathLike):
    content_yaml = yaml.safe_load(open(filepath))
    content_toml = toml.dumps(content_yaml)
    print(content_toml)


def toml2json(filepath: PathLike):
    content_toml = toml.load(open(filepath))
    content_json = json.dumps(content_toml)
    print(content_json)
