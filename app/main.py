import logging
import test_me

logger = logging.getLogger(__name__)


def say_hello(name: str):
    print('hello ', name)
    logger.debug('hello {}'.format(name))


if __name__ == "__main__":
    say_hello('john')
    test_me.test_version()
