from flask import Flask, render_template
import pathlib

app = Flask(__name__)

@app.route("/")
def hello_world():
    files = pathlib.Path('..').iterdir()
    return render_template("index.html.j2", title="Hello World!", files=files)

if __name__ == '__main__':
    app.run(debug=True)
