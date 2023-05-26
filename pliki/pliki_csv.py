import csv


def csv_reader(path):
    with open(path, newline="") as f:
        reader = csv.reader(f, delimiter=";")  # skipinitailspace=True
        for row in reader:
            row = list(map(str.rstrip, row))
            print(row)

def csv_dict_reader(path):
    with open(path, newline="") as f:
        reader = csv.DictReader(f, delimiter=";")  # Jeśli nie ma nagłówka, trzeba podać tutaj fieldnames=[...]
        for row in reader:
            row = {k.rstrip(): v.rstrip() for k, v in row.items()}
            # row2 = {}
            # for k, v in row.items():
            #     row2[k.rstrip()] = v.rstrip()

            print(row)

def csv_writer(path):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(("Aaaa", "Bbbb", "Cccc", "Żółć łódź"))
        writer.writerow(("Cccc", "Dddd", "Cccc", "Żółć łódź"))

if __name__ == "__main__":
    path = r"C:\Users\kurs\Downloads\dane\csv_example1.csv"
    csv_reader(path)
    csv_dict_reader(path)
    csv_writer(r"C:\Users\kurs\Downloads\dane\csv_example-output.csv")

