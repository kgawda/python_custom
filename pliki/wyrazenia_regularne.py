import re


def main():
    s = "34_XYZ1234A_101L18_O_ABC"  # region, _, nazwa_stacji, priorytet, cell, pasmo, adres
    result = re.findall(r"XYZ.*?_", s)  # dodanie "?" po operatorze zmienia go w leniwy
    result = re.findall(r"XYZ[a-zA-Z0-9]*", s)
    print(result)

    #match = re.search(r"(\d)\d_([A-Z]{3}\d{4})([A-Z])_101L18_O_ABC", s)
    #print(match.groups())
    match = re.search(r"(?P<region>\d)\d_(?P<site>[A-Z]{3}\d{4})(?P<prio>[A-Z])_101L18_O_ABC", s)
    if match:
        print(match[0])  # cały zmatchowany string
        print(match.groupdict())





if __name__ == "__main__":
    main()