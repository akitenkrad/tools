import click

from tools.utils import check
from tools.formatter import Formatter

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
