from lansen.renwu.LansenTask import Task
from lansen.renwu import Const
import time

class MeiTuanTask(Task):
    # 执行任务方法
    def runAgent(self):
        print("执行%s........." % self.taskName, "美团.....")

