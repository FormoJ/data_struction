class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):  # 返回下一个节点
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):  # 设置下一个节点
        self.next = newnext


class Unorderlist:
    def __init__(self, head=None):  # 定义表头链接指向
        self.head = head

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()
        return count

    def seach(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def pop(self):
        current = self.head
        previous = None
        while current.getNext() is not None:
            previous = current
            current = current.getNext()
        previous.setNext(None)
        return current.getData()  # 返回pop掉的节点的值

        current = self.head
        previous = None
        while current.getNext() is not None:
            previous = current
            current = current.getNext()
        previous.setNext(None)
        return current.getData()