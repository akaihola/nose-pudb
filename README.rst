=====================================================================
 nose-pudb -- pudb integration for the nose Python testing framework
=====================================================================

The nose-pudb plugin provides integration between the `Nose`_ testing
framework and the `pudb`_ console-based visual debugger.  Instead of
collecting and displaying test results, the test runner can drop into
the debugger on errors and/or test failures.

This is similar to Nose's built-in Debug plugin which uses the pdb
debugger from the Python standard library.

.. contents::

Overview
========

The plugin provides ``--pudb`` and ``--pudb-failures`` options. The
``--pudb`` option will drop the test runner into `pudb`_ when it
encounters an error. To drop into pudb on failure, use
``--pudb-failures``.

.. _Nose: http://www.somethingaboutorange.com/mrl/projects/nose/
.. _pudb: http://pypi.python.org/pypi/pudb

A `script`_ introduced in the pudb wiki provides a simple way to drop
into pudb instead of pdb when running nose tests.  However, when using
that script, pudb fails to show information about the exception object
along with the traceback when hitting the 'e' key.

This plugin passes the exception type and value to pudb's
``post_mortem()`` function so that they are displayed with the
traceback.

.. _script: http://wiki.tiker.net/PuDB/NoseWrapper

Install
=======

You can get nose-pudb with
`easy_install <http://peak.telecommunity.com/DevCenter/EasyInstall>`_ ::
    
    $ easy_install nose-pudb

Or you can clone the source using `git <http://git-scm.com/>`_ from
http://github.com/akaihola/nose-pudb.git and install it with ::
    
    $ python setup.py develop

Usage
-----

To run nose tests and drop into pudb on errors, type::
    
    $ nosetests --pudb

To drop into pudb on failures, type::
    
    $ nosetests --pudb-failures

Contributing
============

Please submit 
`bugs and patches <http://github.com/akaihoa/nose-pudb/issues>`_.  
All contributors will be acknowledged.  Thanks!

Changelog
=========

- 0.1
 
  - Initial release

To Do
=====

- nothing at this point
