#!/usr/bin/env python
import click
from click_aliases import ClickAliasedGroup

@click.group(cls=ClickAliasedGroup)
def cli():
    pass

@click.command()
def foo():
    """Run a command."""
    click.echo('foo')

# Original case that didn't work - should now show aliases
cli.add_command(foo, name='foo2', aliases=['bar', 'baz', 'qux'])

# Original working case for reference
@cli.command(aliases=['test2', 'test3'])
def test():
    """Test command."""
    click.echo('test')

if __name__ == '__main__':
    cli()
