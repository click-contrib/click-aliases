# click-aliases

[![build](https://travis-ci.org/click-contrib/click-aliases.svg?branch=master)](https://travis-ci.org/click-contrib/click-aliases)
[![license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://raw.githubusercontent.com/click-contrib/click-aliases/master/LICENSE)
[![coverage](https://coveralls.io/repos/github/click-contrib/click-aliases/badge.svg?branch=master)](https://coveralls.io/github/click-contrib/click-aliases?branch=master)

Add (multiple) aliases to a click_ group or command.

In your [click](http://click.pocoo.org/) app:

```python
import click
from click_aliases import ClickAliasedGroup

@click.group(cls=ClickAliasedGroup)
def cli():
    pass

@cli.command(aliases=['bar', 'baz', 'qux'])
def foo():
    """Run a command."""
    click.echo('foo')
```

Will result in:
```
Usage: cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  foo (bar,baz,qux)  Run a command.
```
