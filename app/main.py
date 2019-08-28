import logging

logger = logging.getLogger(__name__)


def say_hello(name: str):
    print('hello ', name)
    logger.debug('hello {}'.format(name))


if __name__ == "__main__":
    say_hello('john')
