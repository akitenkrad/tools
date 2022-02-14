import click
from pathlib import Path

from tools.utils import check
from tools.formatter import Formatter
from tools.hash import HashType, get_hash

@click.group()
def cli():
    pass

@cli.command()
@click.option('--input-file', type=click.Path(exists=True), default='', help='path to input file [.json]')
@click.option('--ensure-ascii', is_flag=True, help='[.json] if True, ensure only ascii characters')
@click.option('--indent', type=int, default=2, help='[.json] indent, default=2')
def format(input_file:str, ensure_ascii, indent):
    formatted_text = Formatter.format(input_file, ensure_ascii, indent)
    print(formatted_text)

if __name__ == '__main__':
    cli()

@cli.command()
@click.option('--input', type=str, default='Answer to the Ultimate Question of Life, the Universe, and Everything', help='input text or file')
@click.option('--hash-type', type=click.Choice(['md5', 'sha1', 'sha256', 'sha512']), default='md5', help='hash type')
def hash(input:str, hash_type:str):
    if Path(input).exists():
        text = open(input).read()
    else:
        text = input
    
    target_hash = {h.value: h for h in HashType}
    hash_value = get_hash(text, target_hash[hash_type])
    print(hash_value)
