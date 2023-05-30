from fabric import Connection

def main():
    with Connection("52.50.100.255", user="kurs", connect_kwargs={"password": ""}) as conn:
        # conn.put(), conn.get()  # proste operacje na plikach
        conn.run("touch Konrad")
        result = conn.run("ls -al")

    # przykład obróbki wyniku tekstowego z result.stdout
    if result.exited == 0:
        files = []
        for line in result.stdout.splitlines():
            if not line.startswith("total"):
                files.append(line.split()[-1])
        print("Files to process:", ", ".join(files))

        # result.stderr  # informacje o błędach

if __name__ == "__main__":
    main()
