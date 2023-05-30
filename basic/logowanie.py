import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

import importowany

def main():
    logging.critical("Critical")
    logging.error("Error")
    logging.warning("Warning")
    logging.info("Info")
    logging.debug("Debug")

    a, b = 1, 0
    try:
        a / b
    except ZeroDivisionError:
        logging.exception("Zero division: %s / %s", a, b)  # to wydrukuje tracebak


if __name__ == "__main__":
    main()


# === dekodowanie nazw poziomów ===
# loglevel = "Debug"
# numeric_level = getattr(logging, loglevel.upper(), None)
# if not isinstance(numeric_level, int):
#     raise ValueError('Invalid log level: %s' % loglevel)
# logging.basicConfig(level=numeric_level, ...)

# === dla argparse ===
# parser.add_argument('--verbose', '-v', action='count', default=0, help="Increase verbosity. Use -vvv for DEBUG level.")
# args = parser.parse_args()
#
# args.verbose = logging.ERROR - (10 * args.verbose)
# logging.basicConfig(level=args.verbose, ...)