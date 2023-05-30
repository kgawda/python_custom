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

    path = "C:/Users/kurs/Downloads/dane/txt_example1.txt"
    with open(path) as f:
        s = f.read()

    pattern = r"(?P<region>\d)\d_(?P<site>[A-Z]{3}\d{4})(?P<prio>[A-Z])_\d{3}.\d\d_._[A-Z0-9]*"
    # for line in s.splitlines():
    #     match = re.search(pattern, line)
    #     if match:
    #         print(match.groupdict())

    # print(re.findall(pattern, s)) # lista tupli z grupami

    for match in re.finditer(pattern, s):
        print(match.groupdict())

    # użycie kilku flag:
    # re.findall(pattern, s, re.DOTALL | re.MULTILINE)

if __name__ == "__main__":
    main()

"""
Escaped:  . ^ $ * + - ? ( ) [ ] { } \ |
No need to escape: _ ! % " ' , / : ; < = > @ `
"""
