import sys



class SysStdRedirection:
    """Any change done to `sys.std<in|out|err>` inside this context manager will
       be reverted upon exit."""

    def __init__(self):
        for x in ('stdin', 'stdout', 'stderr'):
            setattr(self, x, getattr(sys, x))

    def __enter__(self):
        pass

    def __exit__(self, error_type=None, value=None, traceback=None):
        for x in ('stderr', 'stdout', 'stdin'):
            setattr(sys, x, getattr(self, x))
