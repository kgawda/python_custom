import json
import datetime

def load_file(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    for site_name, site_data in data.items():
        insert_date = datetime.datetime.strptime(site_data["insert_date"], "%Y-%m-%d %H:%M:%S")
        print(site_name, site_data['city'], insert_date.time())

def load_string():
    s = '{"a": 1, "b": true}'
    data = json.loads(s)
    print(data)

def dump_file(path):
    # Zapis/zrzut/konwersja na json
    data = {'b': 1, 'a': True, 'c': datetime.datetime.now()}
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, default=str, sort_keys=False)

    s = json.dumps(data, indent=4, default=str, sort_keys=False)
    print(s)

    # json.dumps(data)


if __name__ == "__main__":
    path = r"C:\Users\kurs\Downloads\dane\json_example.json"
    load_file(path)
    load_string()
    dump_file(r"C:\Users\kurs\Downloads\dane\json_example-output.json")