def main():
    # list comprehension
    l = [x**2 for x in range(10)]
    assert l == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    l = [s.upper() for s in ('ala', 'kot', 'pies')]
    assert l == ['ALA', 'KOT', 'PIES']

    t = tuple(str(x) for x in range(10))

    d = {x: x+1 for x in range(10)}
    # Zadanie:
    # d = { ...... ('ala', 'kotek', 'piesek')}
    # chcemy uzyskać:
    # {
    #     "Ala": 3,
    #     "Kotek": 5,
    #     "Piesek": 6,
    # }
    print(d)

if __name__ == "__main__":
    main()
