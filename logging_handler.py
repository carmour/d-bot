import logging
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

error_logger = setup_logger('error_logging', 'errors.log')
# error_logger.setLevel(logging.INFO)
posts_logger = setup_logger('post_logging', 'posts.log')
posts_logger.setLevel(logging.INFO)