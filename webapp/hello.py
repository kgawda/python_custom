from flask import Flask, render_template, jsonify
import pathlib

app = Flask(__name__)

@app.route("/")
def hello_world():
    files = pathlib.Path('..').iterdir()  # to tylko przykłąd, typowo nie sięgamy do plików
    return render_template("index.html.j2", title="Hello World!", files=files)

@app.route("/about")
def about():
    return render_template("about.html.j2")

@app.route("/analyze/<word>")
def analyze(word):
    facts = {
        'First letter': word[0],
        'Length': len(word),
    }
    return render_template("analyze.html.j2", title=f"Analysis of {word}", facts=facts)

@app.route("/api/v1/employees")
def list_employees():
    employees = ["Adam", "Janina", "Leszek"]
    return jsonify(employees=employees, company_name="SkyNet", open_positions=5)



if __name__ == '__main__':
    app.run(debug=True)
