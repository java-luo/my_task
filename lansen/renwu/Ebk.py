from lansen.renwu.LansenTask import Task
import time
class EbkTask(Task):
    # 执行任务方法
    def runAgent(self):
         print("执行%s........." % self.taskName, "Ebk.....")
         time.sleep(self.executionTime)

