class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        self.size -= 1
        return self.queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Enqueue to a full queue")
        self.queue.append(value)
        self.size += 1

    def front(self):
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        return self.queue[0]