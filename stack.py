class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        self.size -= 1
        return self.stack.pop()

    def push(self, value):
        if self.is_full():
            raise OverflowError("Push to a full stack")
        self.stack.append(value)
        self.size += 1

    def top(self):
        if self.is_empty():
            raise IndexError("Top from an empty stack")
        return self.stack[-1]