from quene1 import Queue
<<<<<<< HEAD


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num-1):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))  # 输出: Susan
=======
def HotPotato(names,num):
    q = Queue()
    for name in names:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(num-1):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()



print(HotPotato(['Bill','David','Susan','Jane','Kent','Brad'],7))

>>>>>>> origin/main
