import logging
import logging.handlers

logger = logging.getLogger("alfa")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler("example.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

syslog_handler = logging.handlers.SysLogHandler(('52.50.100.255', 5014))
syslog_handler.setLevel(logging.DEBUG)
syslog_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.addHandler(syslog_handler)

import importowany2

def main():
    logger.critical("Critical")
    logger.error("Error")
    logger.warning("Warning")
    logger.info("Info")
    logger.debug("Debug")

    importowany2.przykladowa_funkcja()

if __name__ == "__main__":
    main()