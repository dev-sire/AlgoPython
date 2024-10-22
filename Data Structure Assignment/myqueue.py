class MyQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print("Enqueud Element: ", item)

    def dequeue(self):
        if not self.is_empty():
            print("Dequeued Element: ", self.items.pop(0))
        else:
            print("Cannot dequeue from an empty queue.")

    def is_empty(self):
        return len(self.items) == 0

queue = MyQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Current Queue:", queue.items)
queue.dequeue()
print("Current Queue:", queue.items)
