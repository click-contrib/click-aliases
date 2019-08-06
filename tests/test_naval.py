import click
from click.testing import CliRunner

from click_aliases import ClickAliasedGroup

import pytest


@pytest.fixture(scope="function")
def runner():
    return CliRunner()


@click.group(cls=ClickAliasedGroup)
def cli():
    """Naval Fate."""


@cli.group('ship', cls=ClickAliasedGroup, aliases=['boat'])
def fleet():
    """Manages ships."""


@fleet.command('new', aliases=['create', 'add', 'build'])
@click.argument('name')
def ship_new(name):
    """Creates a new ship."""
    click.echo('Created ship %s' % name)


@fleet.command('move', aliases=['float', 'navigate'])
@click.argument('ship')
@click.argument('x', type=float)
@click.argument('y', type=float)
@click.option('--speed', metavar='KN', default=10, help='Speed in knots.')
def ship_move(ship, x, y, speed):
    """Moves SHIP to the new location X,Y."""
    click.echo('Moving ship %s to %s,%s with speed %s' % (ship, x, y, speed))


@fleet.command('shoot', aliases=['fire'])
@click.argument('ship')
@click.argument('x', type=float)
@click.argument('y', type=float)
def ship_shoot(ship, x, y):
    """Makes SHIP fire to X,Y."""
    click.echo('Ship %s fires to %s,%s' % (ship, x, y))


@cli.group('mine', cls=ClickAliasedGroup, aliases=['bomb'])
def mine():
    """Manages mines."""


@mine.command('set')
@click.argument('x', type=float)
@click.argument('y', type=float)
@click.option('ty', '--moored', flag_value='moored', default=True,
              help='Moored (anchored) mine. Default.')
@click.option('ty', '--drifting', flag_value='drifting',
              help='Drifting mine.')
def mine_set(x, y, ty):
    """Sets a mine at a specific coordinate."""
    click.echo('Set %s mine at %s,%s' % (ty, x, y))


@mine.command('remove', aliases=['rm', 'delete', 'remove'])
@click.argument('x', type=float)
@click.argument('y', type=float)
def mine_remove(x, y):
    """Removes a mine at a specific coordinate."""
    click.echo('Removed mine at %s,%s' % (x, y))


TEST_CLI = """Usage: cli [OPTIONS] COMMAND [ARGS]...

  Naval Fate.

Options:
  --help  Show this message and exit.

Commands:
  mine (bomb)  Manages mines.
  ship (boat)  Manages ships.
"""


def test_cli(runner):
    result = runner.invoke(cli)
    assert result.output == TEST_CLI


TEST_SHIP_HELP = """Usage: cli {cmd} [OPTIONS] COMMAND [ARGS]...

  Manages ships.

Options:
  --help  Show this message and exit.

Commands:
  move (float,navigate)   Moves SHIP to the new location X,Y.
  new (add,build,create)  Creates a new ship.
  shoot (fire)            Makes SHIP fire to X,Y.
"""


def test_ship_help(runner):
    for cmd in ['ship', 'boat']:
        result = runner.invoke(cli, [cmd])
        assert result.output == TEST_SHIP_HELP.format(cmd=cmd)


def test_ship_move(runner):
    TEST = 'Moving ship mcboat to 1.0,1.0 with speed 10\n'
    for cmd in ['ship', 'boat']:
        for subcmd in ['move', 'float', 'navigate']:
            result = runner.invoke(cli, [cmd, subcmd, 'mcboat', "1", "1"])
            assert result.output == TEST
