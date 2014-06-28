"""
This plugin provides ``--pudb``, ``--pudb-errors`` and ``--pudb-failures`` options.
The ``--pudb`` option will drop the test runner into pudb when it encounters an error or a failure.
To drop into pudb on error, use ``--pudb-errors``.
To drop into pudb on failure, use ``--pudb-failures``.
"""

import sys
import pudb

from nose.plugins.debug import Pdb


class Pudb(Pdb):
    """
    Provides --pudb-errors, --pudb-failures and --pudb options that cause the
    test runner to drop into pudb if it encounters an error or failure or both,
    respectively.
    """

    def options(self, parser, env):
        """Register command line options."""
        parser.add_option(
            "--pudb",
            action="store_true",
            dest="pudbDebugBoth",
            default=env.get('NOSE_PUDB', False),
            help="Drop into pudb debugger on failures or errors")
        parser.add_option(
            "--pudb-failures",
            action="store_true",
            dest="pudbDebugFailures",
            default=env.get('NOSE_PUDB_FAILURES', False),
            help="Drop into pudb debugger on failures")
        parser.add_option(
            "--pudb-errors",
            action="store_true",
            dest="pudbDebugErrors",
            default=env.get('NOSE_PUDB_ERRORS', False),
            help="Drop into pudb debugger on errors")

    def configure(self, options, conf):
        """Configure which kinds of exceptions trigger plugin."""
        self.conf = conf
        self.enabled_for_errors = options.pudbDebugErrors or \
            options.pudbDebugBoth
        self.enabled_for_failures = options.pudbDebugFailures or \
            options.pudbDebugBoth
        self.enabled = self.enabled_for_failures or self.enabled_for_errors

    def debug(self, err):
        ec, ev, tb = err
        stdout = sys.stdout
        sys.stdout = sys.__stdout__
        try:
            pudb.post_mortem(tb)
        finally:
            sys.stdout = stdout
