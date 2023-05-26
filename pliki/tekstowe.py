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
            if not line:
                continue
            columns = line.split("  ")
            columns = filter(None, columns)  # odrzuć elementy o bool(x) == False
            # filter zwraca generator
            columns = map(str.lstrip, columns)  # usuń spacje z początków
            # map zwraca generator
            columns = list(columns)  # przerabiamy generator na listę, bo nie można się odwołać do elementu generatora przez generator[0]
            print(columns)


        # Zadanie: stworzyć (i wydrukować) słownik, gdzie kluczem będzie Cell local ID, a wartością technologia
        # Przykład wydruku:
        # {0: "L18", 1: "L18", ...}

if __name__ == "__main__":
    main()
