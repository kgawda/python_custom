import datetime
import pytz


def main():
    s1 = "2023-10-29 02:42:46 DST"
    s2 = "2023.10.29 02:58:25 +01:00 DST"
    # strptime -> STRing Parse TIME
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

    is_dst = "DST" in s1
    s1 = s1.replace(' DST', '')
    d1 = datetime.datetime.strptime(s1, "%Y-%m-%d %H:%M:%S")
    waw = pytz.timezone("Europe/Warsaw")
    d1 = waw.localize(d1, is_dst=is_dst)
    print(repr(d1))

    # parsowanie s2
    # is_dst = "DST" in s2  # tego na razie nie używamy
    s2 = s2.replace(' DST', '')
    d2 = datetime.datetime.strptime(s2, "%Y.%m.%d %H:%M:%S %z")
    d2 = d2.astimezone(waw)
    print(repr(d2))

    print(d2 - d1)


if __name__ == "__main__":
    main()
