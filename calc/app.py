from flask import Flask, request
from operations import add, sub, div, mult

app = Flask(__name__)

@app.route('/add')
def addition():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a,b))

@app.route('/sub')
def subtration():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a,b))

@app.route('/div')
def division():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a,b))

@app.route('/mult')
def multiplication():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a,b))

math_operations = {
    "add": add,
    "sub": sub,
    "div": div,
    "mult": mult
}

@app.route('/math/<solve>')
def math(solve):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(math_operations[solve](a,b))



