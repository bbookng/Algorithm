N = 3
q = [0] * 3
front = 0
rear = 0

rear = (rear+1) % N
q[rear] = 1

rear = (rear+1) % N
q[rear] = 2

rear = (rear+1) % N
q[rear] = 3

front = (front+1) % N
print(q[front])

front = (front+1) % N
print(q[front])

front = (front+1) % N
print(q[front])