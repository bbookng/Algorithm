class Queue:
    def __init__(self, n):
        self.size = n
        self.items = [None] * n
        self.front = -1
        self.rear = -1

    def isfull(self):
        return True if self.rear == self.size -1 else False

    def deQueue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            self.front += 1
            item = self.items[self.front]



    def enQueue(self, item):
        if self.isfull():
            print("Queue is full")
        else:
            self.rear += 1
            self.items[self.rear] = item

    def isEmpty(self):
        return True if self.front == self.rear else False

    def Qpeek(self):
        return self.items[self.front]


q = Queue(3)
q.enQueue(1)
q.enQueue(3)
q.enQueue(2)

print(q.items)
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())



