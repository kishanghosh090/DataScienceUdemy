from logger import logging

def add(a,b):
    logging.debug("add function called")
    return a+b


logging.debug("the addition fun is called")
add(1,2)