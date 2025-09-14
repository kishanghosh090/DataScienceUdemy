import logging

## logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a+b
    logger.debug(f"adding {a} and {b} result is {result}")
    return result


def sub(a,b):
    result = a-b
    logger.debug(f"subtract {a} and {b} result is {result}")
    return result


add(12,45)
sub(23,434)