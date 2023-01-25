import logging
import sys

FORMATTER = logging.Formatter(
    '%(asctime)s [%(name)s] %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')


def get_console_handler():
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler(log_name: str):
    file_handler = logging.FileHandler(filename=log_name + '.log')
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler(log_name=name))
    logger.propagate = False
    return logger
