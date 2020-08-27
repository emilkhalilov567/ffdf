from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])

def home():

   return 'Всё, что можем сделать с числами, дайте нам: /calc/<число 1>/<число 2>'


@app.route('/calc/<int:num1>/<int:num2>', methods = ['GET'])

def square(num1,num2):

   return jsonify({"+": num1+num2,

                   "-": num1-num2,

                   "*": num1*num2,

                   "/": num1 / num2 })


if __name__ == '__main__':

   app.run(debug = True)
