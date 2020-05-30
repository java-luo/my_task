from flask import Flask,request
from lansen.service import mainController
import json
from  lansen.renwu import Const
app = Flask(__name__)

@app.route('/createTask',methods=['POST'])
def createTask():
    id= request.form.get("id")
    executionTime = request.form.get("executionTime")
    taskName=request.form.get("taskName")
    if(getTask(taskName)):
        mainController.createTask(int(id),int(executionTime),taskName)
        return "OK"
    else:
        return "任务名称重复,请重新输入"

@app.route('/getTaskList')
def getTaskList():
    return json.dumps(mainController.getTakList())


@app.route('/removeTask')
def removeTask():
    taskName=request.args.get("taskName")
    isOk=mainController.removeTask(taskName)
    return str(isOk)

def getTask(taskName):
    task = Const.taskList.get(taskName)
    if(task==None):
        return True
    else:
        return False


if __name__ == '__main__':
    app.run()
