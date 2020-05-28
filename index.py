from flask import Flask,request

app = Flask(__name__)

@app.route('/createTask')
def hello_world():
    id= request.args.get("id")
    print(id)
    return id
