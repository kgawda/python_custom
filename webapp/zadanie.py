from flask import Flask, jsonify
import requests

app = Flask(__name__)
call_server_address = "http://3.249.183.211:5000"

@app.route("/status")
def status():
    # return jsonify({"status": "OK"})
    return jsonify(status="OK")

@app.route("/call_server_status/<data_name>")
def call_server_status(data_name):
    r = requests.get(call_server_address + '/status')
    j = r.json()
    value = j[data_name]
    return jsonify({data_name: value})


if __name__ == '__main__':
    app.run(debug=True)
