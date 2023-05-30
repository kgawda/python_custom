import sys
import contextlib

class ExampleException(Exception):
    pass


def f(x):
    if x == 0:
        raise ExampleException("Funkcja f wywołana z niedozwolonym argumentem x == 0")
    return x/0

def main():
    print("Początek")
    # Wydruki na stderr:
    #print("Środek", file=sys.stderr)
    #sys.stderr.write("Środek2\n")

    try:
        f(0)  # rzuca błędem
        print("To się nie wykona")
    except (ZeroDivisionError, ExampleException, KeyError) as e:
        print("Złapano wyjątek")
        # Prościutkie "logowanie"
        #import traceback
        #traceback.print_exc()
        #print(type(e).__name__+":", str(e))

        #raise  # Rzucamy dalej ten wyjątek
    finally:
        print("Koniec")

    with contextlib.suppress(ExampleException):
        f(0)

    # ... to odpowiada temu:
    # try:
    #     f(0)
    # except ExampleException:
    #     pass


if __name__ == "__main__":
    main()
