import requests
from requests.exceptions import SSLError

def wp():
    response = requests.get("http://wp.pl")
            # headers={"User-Agent": "..."}
            # timeout=10  # w sekundach
    print(response.status_code, response.url)
    # response.headers
    print(len(response.text), response.headers.get('content-type'))

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


def bez_requestsow(url):
    import urllib3
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return(response.data)

def rest():
    r = requests.get("https://restcountries.com/v3.1/name/poland")
    r.raise_for_status()
    print(r.text)
    print(r.headers.get('content-type'))
    print(r.json())
    # wyciągnąć str zawierającego nazwę karaju po estońsku ("est")

if __name__ == "__main__":
    #wp()
    #badssl()
    #errors()
    rest()