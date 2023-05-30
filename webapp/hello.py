from flask import Flask, render_template
import pathlib

app = Flask(__name__)

@app.route("/")
def hello_world():
    # files = pathlib.Path('..').iterdir()
    # s = "\n".join(f"<p>{f}</p>" for f in files)
    return render_template("index.html.j2", title="Hello World!")

if __name__ == '__main__':
    app.run(debug=True)
