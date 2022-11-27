from flask import Flask, jsonify
from flask_restful import Resource, Api
#from clean import *

app = Flask(__name__)

@app.route('/', methods= ['GET'])
def index():
    return jsonify({'greetings': "Hi this is python"})

if __name__ == "__main__":
    app.run(debug=True)