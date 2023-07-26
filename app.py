from flask import Flask, request
from business_match import *
from business_search import *

app = Flask(__name__)

@app.route("/")
def home():
    return "200 OK"

@app.route("/test")
def test():
    return "test endpoint"

@app.route('/api')
def returndata():
    
    inputloc = str(request.args['query'])
    business_search(inputloc)
    d = business_match()
    
    return d


if __name__ == "__main__":
    app.run(debug=True)