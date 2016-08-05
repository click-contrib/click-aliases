=============
click-aliases
=============

|build|


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

.. |build|  image:: https://travis-ci.org/rbonthond/click-aliases.svg?branch=master
    :target: https://travis-ci.org/rbonthond/click-aliases
    :alt: Build status of the master branch
