import click

@click.command(name='bar')
def bar():
    """Prints 'Hello, world!'."""
    click.echo('Hello, world!')
