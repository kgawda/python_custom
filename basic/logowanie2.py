import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)


def main():
    logger.critical("Critical")
    logger.error("Error")
    logger.warning("Warning")
    logger.info("Info")
    logger.debug("Debug")

if __name__ == "__main__":
    main()