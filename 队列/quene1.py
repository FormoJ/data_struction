class Queue:
    def __init__(self):
        self.items = []

<<<<<<< HEAD
    def isEmpty(self):
=======
    def is_empty(self):
>>>>>>> origin/main
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
<<<<<<< HEAD

    def size(self):
        return len(self.items)
=======
    def size(self):
        return len(self.items)
>>>>>>> origin/main
