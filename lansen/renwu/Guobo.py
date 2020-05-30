from lansen.renwu.LansenTask import Task
from  lansen.spider import  Guobo_Spider
import datetime
import time
class Guobo(Task):
    def __init__(self,executionTime,taskName,**kwargs):
        self.createTime = datetime.datetime.now()  # 任务开始时间
        self.isStart = False  # 任务结束时间
        self.taskName = taskName  # 任务名称
        self.executionTime = executionTime
        Guobo_Spider.init()

    # 执行任务方法
    def runAgent(self):
         self.isStart=Guobo_Spider.spider_is_ok
         Guobo_Spider.start()
         time.sleep(self.executionTime)

