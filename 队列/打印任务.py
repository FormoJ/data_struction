from quene1 import Queue
import random


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印速度,每分钟处理多少页
        self.currentTask = None
        self.timeRemaining = 0  # 还差几秒打印完

    def tick(self):  # 打印
        if self.currentTask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None  # 打印完了

    def busy(self):  # 返回打印机是否忙，忙则返回True
        return self.currentTask is not None

    def startNext(self, newtask):  # 打印新任务
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time  # 当前时间
        self.pages = random.randrange(1, 21)  # 随机生成1-20页

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):  # 返回等待时间
        return currenttime - self.timestamp


def new_print_task():  # 是否生成新任务
    num = random.randrange(1, 721)
    return num == 180


def simulation(numSeconds, pagesPerMinute):  # 模拟  打印秒数加上每分钟打几页
    labprinter = Printer(pagesPerMinute)
    printQuene = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):  # 在一个小时内的某一秒
        if new_print_task():
            task = Task(currentSecond)
            printQuene.enqueue(task)

        if (not labprinter.busy()) and (not printQuene.isEmpty()):
            nexttask = printQuene.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()  # 忙就要过秒

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print(f"Average Wait {averageWait:6.2f} secs {printQuene.size():3d} tasks remaining.")


if __name__ == '__main__':
    for i in range(10):
        simulation(3600, 10)
