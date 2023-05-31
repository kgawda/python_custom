from flask import Flask, jsonify

app = Flask(__name__)
call_server_address = "http://3.249.183.211:5000"

@app.route("/status")
def status():
    # return jsonify({"status": "OK"})
    return jsonify(status="OK")


if __name__ == '__main__':
    app.run(debug=True)
