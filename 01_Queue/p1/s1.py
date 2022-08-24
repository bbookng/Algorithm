Queue = []

front = 0
rear = 0

for i in range(1, 4):
    Queue.insert(rear, i)
    rear += 1

for i in range(3):
    print(Queue[front])
    front += 1


