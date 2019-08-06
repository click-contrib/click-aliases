import click
from click.testing import CliRunner

from click_aliases import ClickAliasedGroup, _click7

import pytest


@pytest.fixture(scope="function")
def runner():
    return CliRunner()


@click.group(cls=ClickAliasedGroup)
def cli():
    pass


@cli.command()
def foo():
    click.echo('foo')


TEST_HELP = """Usage: cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  foo
"""


def test_help(runner):
    result = runner.invoke(cli)
    assert result.output == TEST_HELP


def test_foobar(runner):
    result = runner.invoke(cli, ['foo'])
    assert result.output == 'foo\n'


TEST_INVALID = """Usage: cli [OPTIONS] COMMAND [ARGS]...
{}
Error: No such command "bar".
""".format('Try "cli --help" for help.\n' if _click7 else '')


def test_invalid(runner):
    result = runner.invoke(cli, ['bar'])
    assert result.output == TEST_INVALID
