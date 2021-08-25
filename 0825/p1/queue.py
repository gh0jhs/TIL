class Queue:
    # createQueue
    def __init__(self, n):
        self.length = n
        self.items = [0] * self.length
        self.rear = -1
        self.front = -1

    # 삽입
    def enQueue(self, item):
        self.rear += 1
        self.items[self.rear] = item

    # 삭제 및 반환
    def deQueue(self):
        self.front += 1
        return self.items[self.front]

    # 비어있는지 확인
    def isEmpty(self):
        return self.front == self.rear

    # 가득차 있는지 확인
    def isFull(self):
        return self.rear == self.length - 1

    # 현재 front에 있는 값 확인
    def Qpeek(self):
        return self.items[self.front]


q = Queue(3)
print(q.items)
q.enQueue(1)
print(q.items, q.front, q.rear)
q.enQueue(2)
print(q.items, q.front, q.rear)
q.enQueue(3)
print(q.items, q.front, q.rear)
print(q.isFull())
print(q.deQueue())
print(q.items, q.front, q.rear)
