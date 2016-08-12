=============
click-aliases
=============

|build| |license| |coverage|


**This is experimental, which is why it's not on PyPI**

Add (multiple) aliases to a click_ group or command.

In your click_ app:

.. code:: python

    import click
    from click_aliases import ClickAliasedGroup

    @click.group(cls=ClickAliasedGroup)
    def cli():
        pass

    @cli.command(aliases=['bar', 'baz', 'qux'])
    def foo():
        """Run a command."""
        click.echo('foo')

Will result in:

.. code::

    Usage: cli [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      foo (bar,baz,qux)  Run a command.


.. _click: http://click.pocoo.org/

.. |build|  image:: https://travis-ci.org/click-contrib/click-aliases.svg?branch=master
    :target: https://travis-ci.org/click-contrib/click-aliases
    :alt: Build status of the master branch

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat
    :target: https://raw.githubusercontent.com/click-contrib/click-aliases/master/LICENSE
    :alt: Package license

.. |coverage| image:: https://coveralls.io/repos/github/click-contrib/click-aliases/badge.svg?branch=master
    :target: https://coveralls.io/github/click-contrib/click-aliases?branch=master
    :alt: Coverage report
