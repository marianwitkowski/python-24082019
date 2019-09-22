from flask import Flask, jsonify, make_response

app = Flask("MyApiServer")

def create_reponse(message, code):
    resp = make_response(message, code)
    resp.mimetype = 'application/json'
    return resp

@app.route('/')
def hello():
    return "Hello world!"

@app.route('/<name>')
def papuga(name):
    return "Papuguję: "+name

@app.route('/api/ping', methods=['GET'])
def ping():
    return create_reponse(jsonify({"status" : "OK"}), 200)

app.run(port=1234, debug=True)