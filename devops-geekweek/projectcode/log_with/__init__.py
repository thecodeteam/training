import functools,logging, collections


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def dump_args(func):
    "This decorator dumps out the arguments passed to a function before calling it"
    argnames = func.func_code.co_varnames[:func.func_code.co_argcount]
    fname = func.func_name

    def echo_func(*args, **kwargs):
        me = fname, ":", ', '.join(
            '%s=%r' % entry
            for entry in zip(argnames, args) + kwargs.items())
        log.info(me)
        return func(*args, **kwargs)

    return echo_func

class log_with(object):
    '''Logging decorator that allows you to log with a
specific logger.
'''
    # Customize these messages
    ENTRY_MESSAGE = 'Entering {}'
    EXIT_MESSAGE = 'Exiting {}'

    def __init__(self, logger=None):
        self.logger = logger

    def __call__(self, func):
        '''Returns a wrapper that wraps func.
The wrapper will log the entry and exit points of the function
with logging.INFO level.
'''
        # set logger if it was not set earlier
        if not self.logger:
            logging.basicConfig()
            self.logger = logging.getLogger(func.__module__)

        @functools.wraps(func)
        def wrapper(*args, **kwds):
            self.logger.debug(
                self.ENTRY_MESSAGE.format(func.__name__))  # logging level .info(). Set to .debug() if you want to
            f_result = func(*args, **kwds)
            self.logger.debug(
                self.EXIT_MESSAGE.format(func.__name__))  # logging level .info(). Set to .debug() if you want to
            return f_result

        return wrapper

