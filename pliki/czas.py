import datetime
import pytz


def main():
    s1 = "2023-10-29 02:42:46 DST"
    s2 = "2023.05.26 08:58:25 +01:00 DST"
    # strptime -> STRing Parse TIME
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

    is_dst = "DST" in s1
    s1 = s1.replace(' DST', '')
    d1 = datetime.datetime.strptime(s1, "%Y-%m-%d %H:%M:%S")
    waw = pytz.timezone("Europe/Warsaw")
    d1 = waw.localize(d1, is_dst=is_dst)
    print(repr(waw))
    print(d1)
    print(repr(d1))


if __name__ == "__main__":
    main()
