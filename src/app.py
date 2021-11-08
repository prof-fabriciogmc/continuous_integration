from flask import Flask
from flask import jsonify
from model.model import to_uppercase


app = Flask(__name__)

@app.route('/')
def index():
    word = 'fabricio'
    word_upper = to_uppercase(word)
    word_upper_json = {'word_upper': word_upper}
    return jsonify(word_upper_json)    

if __name__ == "__main__":

    app.run('0.0.0.0', port=5000)
