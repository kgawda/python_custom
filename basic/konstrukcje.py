import collections

def main():
    # list comprehension
    l = [x**2 for x in range(10)]
    assert l == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    l = [s.upper() for s in ('ala', 'kot', 'pies')]
    assert l == ['ALA', 'KOT', 'PIES']

    t = tuple(str(x) for x in range(10))

    d = {x: x+1 for x in range(10)}
    # d = { x[0].upper() + x[1:]: len(x) for x in ('ala', 'kotek', 'piesek')}
    d = {x.capitalize(): len(x) for x in ('ala', 'kotek', 'piesek')}
    # chcemy uzyskać:
    assert d == {
        "Ala": 3,
        "Kotek": 5,
        "Piesek": 6,
    }

    # Lambda
    # dwa równoważne sposoby zdefiniowania funkcji f:

    def f(x):
        ...
        return x ** 2

    f = lambda x: x ** 2


    # rzeczy = ("Szafa", "album", "Biurko")
    # print(list(sorted(rzeczy, key=str.lower)))  # str.lower("Biurko")
    # print(list(sorted(rzeczy, key=lambda s: s.lower())))  # "Biurko".lower()

    # rzeczy = (".szafa", "!album", "-biurko")
    # print(list(sorted(rzeczy, key=lambda s: s[1:])))


if __name__ == "__main__":
    main()
    print("Wszystko ok")
