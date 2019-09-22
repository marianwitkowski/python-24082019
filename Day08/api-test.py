from flask import Flask, jsonify, make_response
import math

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

@app.route('/api/isPrime/<number>')
def check_is_prime(number):
    try:
        number = int(number)
        if (number < 2):
            return create_reponse(jsonify({"status" : "OK", "msg" : "Not prime number"}), 409)
        else:
            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    return create_reponse(jsonify({"status" : "OK", "msg" : "Not prime number"}), 409)
            return create_reponse(jsonify({"status" : "OK"}), 200)
    except Exception as exc:
        return create_reponse(jsonify({"status" : "ERROR", "error" : str(exc) }), 500)

app.run(port=1234, debug=True)