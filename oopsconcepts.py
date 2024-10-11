from collections import deque
import time
# stack = []
# #LIFO
# # Pushing elements onto the stack
# stack.append(1)
# stack.append(2)
# stack.append(3)

# print(stack)
# # Popping elements from the stack
# top_element = stack.pop()  # Removes and returns 3
# print(top_element)

# FIFO
#
# from collections import deque
#
# queue = deque()
#
# # Enqueuing elements into the queue
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)
# # Dequeuing elements from the queue
# front_element = queue.popleft()  # Removes and returns 1
# print(front_element)


input_string = "Hello"
stack = []
for char in input_string:
    stack.append(char)
reversed_string = ""
while stack:
    reversed_string += stack.pop()
print(reversed_string)



class TaskScheduler:
    def __init__(self):
        self.queue = deque()

    def add_task(self, task):
        self.queue.append(task)

    def execute_tasks(self):
        while self.queue:
            task = self.queue.popleft()
            print(f"Executing task: {task}")
            time.sleep(1)  # Simulate task execution time


# Using the TaskScheduler
scheduler = TaskScheduler()

# Adding tasks to the scheduler
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")

# Executing tasks
scheduler.execute_tasks()
