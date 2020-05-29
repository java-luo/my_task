from flask import Flask,request
from lansen.service import mainController
import json
app = Flask(__name__)

@app.route('/createTask')
def createTask():
    id= request.args.get("id")
    executionTime = request.args.get("executionTime")
    taskName=request.args.get("taskName")
    mainController.createTask(int(id),int(executionTime),taskName)
    return 'ok'

@app.route('/getTaskList')
def getTaskList():
    return json.dumps(mainController.getTakList())


@app.route('/removeTask')
def removeTask():
    taskName=request.args.get("taskName")
    isOk=mainController.removeTask(taskName)
    return str(isOk)




@app.route('/index')
def index():
    return json.dumps(mainController.getTakList())



if __name__ == '__main__':
    app.run()
