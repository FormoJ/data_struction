from quene1 import Queue
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

