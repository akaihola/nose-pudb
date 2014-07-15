====================================================================
 nose-pudb -- pudb integration for the nose python testing framework
====================================================================

.. image:: https://travis-ci.org/AntoineD/nose-pudb.png?branch=master
    :target: https://travis-ci.org/AntoineD/nose-pudb

The nose-pudb plugin provides the integration between the `nose <https://nose.readthedocs.org>`_ testing framework and the `pudb <http://pypi.python.org/pypi/pudb>`_ console-based visual debugger.
Instead of collecting and displaying the test results, the test runner can drop into the debugger on test errors and/or failures.

This is similar to the nose's built-in `pdb <https://nose.readthedocs.org/en/latest/plugins/debug.html>`_ plugin which uses the debugger from the python standard library.

Please submit bugs and patches on https://github.com/AntoineD/nose-pudb/issues.

This plugin has been originally developed by `Antti Kaihola <https://github.com/akaihola>`_.

Installation
============

Install nose-pudb using pip::

    $ pip nose-pudb

Or you can clone the source using `git <http://git-scm.com/>`_ from http://github.com/AntoineD/nose-pudb.git and install it with::

    $ python setup.py install

Usage
=====

To run nose and drop into pudb on test failures and errors, use::

    $ nosetests --pudb

or set the environment variable ``NOSE_PUDB``::

    $ NOSE_PUDB=1 nosetests

To drop into pudb on failures, use::

    $ nosetests --pudb-failures

or set the environment variable ``NOSE_PUDB_FAILURES``::

    $ NOSE_PUDB_FAILURES=1 nosetests

To drop into pudb on errors, use::

    $ nosetests --pudb-errors

or set the environment variable ``NOSE_PUDB_ERRORS``::

    $ NOSE_PUDB_ERRORS=1 nosetests

License
=======

This plugin is released under the GNU Lesser General Public license (LGPL).
See the file ``LICENSE`` for details.
