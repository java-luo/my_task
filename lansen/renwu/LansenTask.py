import  datetime
import  time
import threading
from lansen.renwu import  Const
class Task():
    def __init__(self,executionTime,taskName,**kwargs):
         self.createTime=datetime.datetime.now() #任务开始时间
         self.isStart=False #任务结束时间
         self.taskName=taskName #任务名称
         self.executionTime=executionTime

    #任务执行
    def start(self):
        self.isStart=True
        t = threading.current_thread();
        Const.taskList[t.name] = self
        self.run()

    #任务结束
    def stop(self):
        self.isStart=False

    #执行任务方法
    def run(self):
        while(True):
            if(self.isStart):
                self.runAgent()
                time.sleep(self.executionTime)
            else:
                t = threading.current_thread();
                Const.taskList.pop(t.name)
                return

    #逻辑代码
    def runAgent(self):
        pass
    #任务已经执行时间
    def executeTime(self):
         execute_time=datetime.datetime.now()-self.createTime;
         return str(execute_time)

    def getCreateTime(self):
        return self.createTime.strftime("%Y-%m-%d %H:%M:%S")

