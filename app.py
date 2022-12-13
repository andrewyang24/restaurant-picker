from flask import Flask, request, jsonify
from business_match import *
from business_search import *

app = Flask(__name__)

@app.route('/api', methods= ['GET'])
def returndata():
    inputloc = str(request.args['query'])
    business_search(inputloc)
    d = business_match()
    return d


if __name__ == "__main__":
    app.run(debug=True)