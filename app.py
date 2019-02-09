from flask import Flask, request, jsonify, json, Response
from flask_cors import CORS
from flask_session import MongoDBSessionInterface
from pymongo import MongoClient


app = Flask(__name__)
app.secret_key = "SECRET KEY"
app.config.from_object(__name__)
CORS(app)

client = MongoClient()
db = client.database
app.session_interface = MongoDBSessionInterface(client=client,
                                                db="flask_sessions",
                                                collection="sessions",
                                                key_prefix=app.secret_key,
                                                use_signer=True)

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

# API route
@app.route('/api', methods = ['POST'])
def api():
    info = jsonify(data=request.data)
    resp = Response(js, status=200, mimetype='application/json')

    return resp

if __name__ == '__main__':
    app.run()