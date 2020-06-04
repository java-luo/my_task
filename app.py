from flask import Flask,request
from lansen.service import mainController
import json
from lansen.util import SpiderUtil
from  lansen.renwu import Const
import  requests
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

@app.route('/getTicket')
def getTicket():
    headers = {
        "Referer": "http://ticket.chnmuseum.cn/yuyue/index",
        "Origin": "http://ticket.chnmuseum.cn",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "User-Agent": SpiderUtil.get_user_agent()
    }
    r=requests.get("https://ticketapi.chnmuseum.cn/api/ticket/calendar?p=w",headers=headers)
    return r.json()

def getTask(taskName):
    task = Const.taskList.get(taskName)
    if(task==None):
        return True
    else:
        return False



if __name__ == '__main__':
    app.run()
