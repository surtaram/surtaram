import threading

import time


def print_number():
    for i in range(1, 6):
        print(f"number:{i}")
        time.sleep(1)


# thread1 = threading.Thread(target=print_number())
# thread1.start()
# print("Main thread ka kaam continue ho raha hai.")


# Stack  :- LIFO

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("STACK IS EMPTY")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

stack =Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.peek())

