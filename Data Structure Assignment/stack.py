class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.isEmpty():
            print("Popped Element: ", self.stack.pop())
        else:
            print("Stack is empty.")

    def peek(self):
        if not self.isEmpty():
            print("Peeked Element: ", self.stack[-1])
        else:
            print("Stack is empty.")

myStack = Stack()
myStack.push(23)
myStack.push(32)
myStack.push(42)

myStack.peek()
myStack.pop()
myStack.peek()
myStack.pop()
myStack.peek()