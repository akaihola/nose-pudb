import pudb
from nose.plugins.debug import Pdb

class Pudb(Pdb):
    """
    Provides the ``--pudb`` and ``--pudb-failures`` options that cause
    the test runner to drop into pudb if it encounters an error or
    failure, respectively.
    """

    def options(self, parser, env):
        """Register commandline options.
        """
        parser.add_option(
            "--pudb", action="store_true", dest="pudbDebugErrors",
            default=env.get('NOSE_PUDB', False),
            help="Drop into the pudb debugger on errors")
        parser.add_option(
            "--pudb-failures", action="store_true",
            dest="pudbDebugFailures",
            default=env.get('NOSE_PUDB_FAILURES', False),
            help="Drop into the pudb debugger on failures")

    def configure(self, options, conf):
        """Configure which kinds of exceptions trigger plugin.
        """
        self.conf = conf
        self.enabled = options.pudbDebugErrors or options.pudbDebugFailures
        self.enabled_for_errors = options.pudbDebugErrors
        self.enabled_for_failures = options.pudbDebugFailures

    def debug(self, err):
        import sys # FIXME why is this import here?
        ec, ev, tb = err
        stdout = sys.stdout
        sys.stdout = sys.__stdout__
        try:
            pudb.post_mortem((ec, ev,tb))
        finally:
            sys.stdout = stdout
