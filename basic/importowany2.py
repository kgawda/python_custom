import logging
logger = logging.getLogger("alfa.importowany")
#logger = logging.getLogger(__name__)  # tak piszemy jeśli to ma być pakiet pythonowy


def przykladowa_funkcja():
    logger.info("Rozpoczynam powitanie")
    return "No witam"


logger.info("Ładuję moduł %s", __name__)
