from flask import Flask, request, jsonify
from flask_restful import Resource, Api
#from clean import *

app = Flask(__name__)

@app.route('/api', methods= ['GET'])
def returnascii():
    d = {}
    inputchr = str(request.args['query'])  
    answer = str(ord(inputchr))
    d['output'] = answer
    return d


if __name__ == "__main__":
    app.run(debug=True)