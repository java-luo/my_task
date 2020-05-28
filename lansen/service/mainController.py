from lansen.renwu.MeiTuan import MeiTuanTask
from lansen.renwu.Ebk import EbkTask
import time
import  threading
from lansen.renwu import  Const

def createTask(taskId,executionTime,taskName):
    if(taskId==1):
        #创建美团任务
        m=MeiTuanTask(executionTime,taskName)
        t=threading.Thread(target=m.start)
        t.name=taskName
        t.start()

    elif(taskId==2):
        eb= EbkTask(executionTime, taskName)
        t = threading.Thread(target=eb.start)
        t.name=taskName
        t.start()
#删除任务
def removeTask(taskName):
    task=Const.taskList.get(taskName)
    if(task==None):
        print("没有此任务")
        return False
    else:
        task.stop();
        return True

def getTakList():
    result_tast=[]
    for task in Const.taskList.values():
        task_dict={}
        task_dict["taskName"]=task.taskName
        task_dict["statTime"]=task.getCreateTime()
        task_dict["executeTime"]=task.executeTime()
        result_tast.append(task_dict)
    return result_tast



createTask(1,3,"监视美团订单")
time.sleep(5)
createTask(2,4,"监视EBK订单")
print(getTakList())
time.sleep(5)
removeTask("监视EBK订单")
time.sleep(5)
removeTask("监视美团订单")
