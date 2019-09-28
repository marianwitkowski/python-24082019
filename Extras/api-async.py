from flask import Flask, jsonify, make_response, request
import uuid
import threading
import time

# deklaracja aplikacji Flask
app = Flask("MyAsyncApiServer")

# generyczna odpowiedz zwracana przez API
def create_reponse(message, code):
    resp = make_response(message, code)
    resp.mimetype = 'application/json'
    return resp

def generate_file(filename, delay):
    time.sleep(delay)
    with open(filename, "wt") as fh:
        fh.write("A"*5)


# deklaracja routingu
@app.route('/api/gettask/<token>')
def check_task(token):
    try:
        with open(token, "rt") as fp:
            line = fp.read(-1).strip()
            if line=="AAAAA":
                return create_reponse(jsonify({"status" : "OK"}), 200)
            else:
                return create_reponse(jsonify({"status": "ERROR"}), 200)
    except Exception as exc:
        return create_reponse(jsonify({"status" : "ERROR", "error" : str(exc) }), 500)


# deklaracja routingu
@app.route('/api/newtask', methods=['GET'])
def new_task():
    try:
        token = str(uuid.uuid4())
        response = dict()
        response["status"] = "OK"
        response["token"] = token
        threading.Thread(target=generate_file, args=(token, 60)).start()
        return create_reponse(jsonify(response), 200)
    except Exception as exc:
        return create_reponse(jsonify({"status" : "ERROR", "error" : str(exc) }), 500)



@app.after_request
def add_headers(response):
    response.headers["Server"] = "My own API Server"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    response.headers["App-Id"] = "Async API"
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

# uruchom aplikację na localhost, port 1234 w trybie DEBUG
app.run(port=5000, debug=True)