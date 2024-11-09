class Stack:
    def __init__(self):
        self.items = []
<<<<<<< HEAD

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
=======
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    s.push(4)
    print(s.isEmpty())
    print(s.items)
    s.push(True)
    s.push('dog')
    s.push('2.2')
    print(s.peek())
    print(s.items)
    s.pop()
    print(s.size())
    print(s.items)
>>>>>>> origin/main
