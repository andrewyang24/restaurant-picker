from flask import Flask, request, jsonify
from business_match import *

app = Flask(__name__)

@app.route('/api', methods= ['GET'])
def returndata():
    d = business_match()
    return d


if __name__ == "__main__":
    app.run(debug=True)