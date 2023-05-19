import click

from click_aliases import ClickAliasedGroup
from bar.subcommand import bar



@click.group(cls=ClickAliasedGroup)
def cli():
    pass


cli.add_command(bar, aliases=['spam'])

if __name__ == "__main__":
    cli()
