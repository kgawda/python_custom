from lxml import etree
from lxml import objectify

def load_xml(path):
    # r = etree.fromstring(s)
    r = etree.parse(path).getroot()  # to będzie tag Object
    print(r[0])  # jeśli potraktujemy obiekt etree jako liste - dostajemy potomków
    print(repr(r.get("total")))  # przez get pobieramy atrybuty

def xml_details():
    print()
    s = """
    <country name="Polska">
        <population>
            37000000
        </population>
        <flag>
            Biało-czerwona
        </flag>
        <city name="Warszawa">
            <district name="Wola"/>
            <district name="Praga"/>
        </city>
        <city name="Kraków">
            <district name="Krowodrza"/>
            <district name="Nowa Huta"/>
        </city>
    </country>
    """

    r = etree.fromstring(s)
    for x in r.iter("district"):  # nazwa tagu
        print(x.get("name"))
    print()

    # simple XPath-like path language called ElementPath
    print(r.find("city"))
    print(r.findall("city"))
    print(r.findall("district"))  # nic nie znajdzie
    print(r.findall(".//district"))  # użycie składni ElementPath

    print(etree.tostring(r.find("city"), pretty_print=True).decode('utf-8'))

    print(repr(r.find("population").text))

    r = etree.fromstring("<a></a>")
    print("Prosty przypadek:", r, repr(r), bool(r), len(r))
    assert r.find("asdasdsa") is None
    # dlatego nie piszemy tak:
    # x = r.find("x")
    # if x:
    #    ... # instrukcje jeżeli znaleziono


    ### objectify
    print()
    obj = objectify.fromstring(s)
    print(repr(obj), repr(str(obj)))
    print(repr(obj.city.district.get("name")))  # po kropce nazwy tagów
    print(list(obj.city))  # iteracja po obiekcie zwraca jego rodzeństwo!
    print(repr(obj.population))  # prawdziwy int

if __name__ == "__main__":
    path = r"C:\Users\kurs\Downloads\dane\xml_example.xml"
    load_xml(path)
    xml_details()