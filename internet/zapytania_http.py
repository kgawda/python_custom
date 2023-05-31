import requests
from requests.exceptions import SSLError

def wp():
    response = requests.get("http://wp.pl")
            # headers={"User-Agent": "..."}
            # timeout=10  # w sekundach
    print(response.status_code, response.url)
    print(len(response.text), response.headers)

def badssl():
    # https://badssl.com/ -- fajna strona do testowania https
    try:
        response = requests.get("https://expired.badssl.com/")
                    # nie weryfikuj certyfikatów: verify=False
    except SSLError:
        response = None  # przykładowa reakcja

def errors():
    response = requests.get("https://github.com/asdasdasdasdsa/asdasdsa")
    response.raise_for_status()  # requests.exceptions.HTTPError
    print(response.text)


if __name__ == "__main__":
    #wp()
    #badssl()
    errors()