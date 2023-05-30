from fabric import Connection

def example_parsing(s):
    files = []
    for line in s.splitlines():
        if not line.startswith("total"):
            files.append(line.split()[-1])
    print("Files to process:", ", ".join(files))

def main():
    with Connection("52.50.100.255", user="kurs", connect_kwargs={"password": ""}) as conn:
        with conn.cd("/tmp"):  # sprytny context manager
            conn.run("ls -al")
        # conn.put(), conn.get()  # proste operacje na plikach
        conn.run("touch Konrad")  # polecenie touch tworzy pusty plik o zadanej nazwie
        result = conn.run("ls -al")

    # przykład obróbki wyniku tekstowego z result.stdout
    if result.exited == 0:
        example_parsing(result.stdout)
        # result.stderr  # informacje o błędach


if __name__ == "__main__":
    main()
