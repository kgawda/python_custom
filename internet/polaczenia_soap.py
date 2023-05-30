import zeep

def main():
    url = "http://www.dneonline.com/calculator.asmx?WSDL"
    soap = zeep.Client(url, service_name="Calculator", port_name="CalculatorSoap")
    print(soap.service.Add(1, 3))
    print(soap.service.Divide(1234, 100))


if __name__ == "__main__":
    main()

# python -m zeep http://www.dneonline.com/calculator.asmx?WSDL