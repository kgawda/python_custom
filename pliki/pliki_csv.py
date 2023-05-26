import csv


def csv_reader(path):
    with open(path, newline="") as f:
        reader = csv.reader(f, delimiter=";")  # skipinitailspace=True
        for row in reader:
            row = list(map(str.rstrip, row))
            print(row)

def csv_dict_reader(path):
    with open(path, newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            row = {...}
            print(row)

if __name__ == "__main__":
    path = r"C:\Users\kurs\Downloads\dane\csv_example1.csv"
    csv_reader(path)
    csv_dict_reader(path)
