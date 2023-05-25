import importowany

def test_list():
    l = [1, 2, 3, 4]
    assert l[0] == 1
    assert len(l) == 4
    assert l[-1] == 4  # ostatni element
    l.append(5)
    assert l.pop() == 5  # opcjonalnie indeks elementu jako argument

    # slice
    assert l[0:2] == [1, 2]
    assert l[1:4] == [2, 3, 4]
    assert l[1:100] == [2, 3, 4]  # tu wychodzenie poza zakres nie powoduje błędu
    assert l[:2] == [1, 2]
    assert l[1:] == [2, 3, 4]  # pust po dwukropku -> jedź do końca listy

    kopia = l[:]
    # lub: kopia = l.copy()
    kopia.pop()
    kopia[0] = 100
    assert l == [1, 2, 3, 4]

    l2 = [1, 2, 3, 4, 5, 6, 7, 8]
    assert l2[::2] == [1, 3, 5, 7]
    assert l2[1::2] == [2, 4, 6, 8]
    assert l2[6:1:-1] == [7, 6, 5, 4, 3]
    assert l2[::-1] == [8, 7, 6, 5, 4, 3, 2, 1]
    assert list(reversed(l2)) == l2[::-1]
    # odwrócenie "w miejscu"
    l2.reverse()  # zwraca None
    assert l2 == [8, 7, 6, 5, 4, 3, 2, 1]

    # podmiana elementów
    l = [1, 2, 3, 4]
    l[1] = "Dwa"
    assert l == [1, "Dwa", 3, 4]
    l[1:4] = ["Dwójka", "Trójka", "Czwórka"]  # odpowiada: l[1]=.., l[2]=.., l[3]=...
    assert l == [1, 'Dwójka', 'Trójka', 'Czwórka']

def test_tuple():
    t = (1, 2, 3, 4)
    assert t[0] == 1
    # t[0] = "Jeden" --> Błąd
    # t.append(5) --> Błąd
    l = list(t)  # tak tworzymy listę z tupli

    # pakowanie
    t2 = 1, 2, 3, 4  # t2 to będzie tuple
    assert t2 == (1, 2, 3, 4)
    zmienna = 1,  # <-- trudny do wykrycia błąd! tupla
    assert zmienna != 1
    assert zmienna == (1,)

    # rozpakowywanie
    n1, n2, n3, n4 = t2  # tu po prawej stronie może być np. lista
    assert n1 == 1

    # zamiana miejsc (sawp)
    a = 1
    b = 2
    a, b = b, a
    assert a == 2

def test_str():
    s = "Ala ma kota"
    assert s[0] == "A"
    # s[0] = "a"  --> Błąd!

    assert "loading:Kernel..."[8:-3] == "Kernel"
    assert "loading:Shell..."[8:-3] == "Shell"

    assert "uwaga:sZAzGAyDKfOWrYY!..."[6:19:3] == "szyfr"


def test_dict():
    d = {1: "alfa", 2: "bravo"}

    d2 = {
        1: "jeden",
        "dwa": 2,
        "lista": [1, 2, 3],
        True: (1, 2, 3),
        2: test_str,
        test_str: "jasne"
    }

    assert 1 in d  # sprawdzamy czy jest taki klucz
    assert d[1] == "alfa"
    assert d2[True] == (1, 2, 3)

    liczba_ludnosci = {
        "Warszawa": 2_000_000,
        "Kraków": 800_000,
        "Bagienkowice": 5,
    }
    liczba_ludnosci["Radom"] = 200_000

    assert liczba_ludnosci["Warszawa"] == 2000000

    # pętla for po słowniku "jedzie" po kluczach
    #for x in liczba_ludnosci:
    #    print(x) # Warszawa, ...

    # values() -> obiekt zwracający kolejne wartości
    #for x in liczba_ludnosci.values():
    #    print(x)

    # items() -> tuple (klucz, wartość)
    for k, v in liczba_ludnosci.items():
        if v > 500_000:
            # print(k, ":", v)
            # print(k + ":", v)
            print(f"{k}: {v}")


if __name__ == "__main__":
    test_list()
    test_tuple()
    test_dict()
    print("Wszystko OK")

