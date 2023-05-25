def typowe_linijki(path):
    with open(path) as f:
        for line in f:
            line = line.rstrip()
            if not line:  # pusta linia
                continue
            if line.lstrip().startswith('#'):  # komentarze
                continue
            print(line)

def main():
    path = "C:/Users/kurs/Downloads/dane/txt_example1.txt"
    # path = "C:\\Users\\kurs\\Downloads\\dane\\txt_example1.txt"
    # path = r"C:\Users\kurs\Downloads\dane\txt_example1.txt"  # nie działa dla ścieżek kończących się backslashem
    # path = r"C:\"  <-- tak się nie da

    # dane = open(path).read()  # bardzo nieelegancko, ale dla krótko działających programów ujdzie

    #with open(path) as f:  # Context manager
    #    s = f.read()   # wczytanie całości pliku do zmiennej

    with open(path) as f:
        f_iterator = iter(f)
        line1 = next(f_iterator)
        _, site_name, file_date = line1.rstrip().split(maxsplit=2)

        for line in f_iterator:
            if line.startswith('-----------------------------------'):
                break
        column_names = next(f_iterator)

        for line in f_iterator:
            line = line.rstrip()
            if line.startswith("(Number of results"):
                break
            columns = line.split("  ")
            columns = filter(None, columns)  # odrzuć elementy o bool(x) == False
            columns = map(str.lstrip, columns)  # usuń spacje z początków
            print(list(columns))


if __name__ == "__main__":
    main()
