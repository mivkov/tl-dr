from flask import Flask, request, jsonify, json, Response
from flask_cors import CORS
from flask_session import MongoDBSessionInterface
from pymongo import MongoClient
from text_sim import parse


app = Flask(__name__)
app.secret_key = "SECRET KEY"
app.config.from_object(__name__)
CORS(app)

'''
client = MongoClient()
db = client.database
app.session_interface = MongoDBSessionInterface(client=client,
                                                db="flask_sessions",
                                                collection="sessions",
                                                key_prefix=app.secret_key,
                                                use_signer=True)
'''

# HTTP Errors handlers
@app.errorhandler(404)
def url_error(e):
    return "404 Error: Page Not Found"
@app.errorhandler(500)
def server_error(e):
    return "500 Error: Internal Server Error"

#
@app.route('/', methods = ['GET'])
def root():
    return 'Hello!'

@app.route('/apple', methods = ['GET'])
def apple():
    with open('apple_fixed.txt', 'r') as f:
        fl = f.read()
    return fl

# API route
@app.route('/api', methods = ['POST'])
def api():
    info = request.get_json()
    val1 = info.get("text")
    print("data: {}".format(val1))

    with open('apple.txt','r') as f:
        result = parse(val1, f.read())
    
    print("sending off: {}".format(result))

    return jsonify(data=result)

if __name__ == '__main__':
    app.run()
