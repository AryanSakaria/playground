from queue import PriorityQueue
import random 

q = PriorityQueue()
for i in range(10):
	q.put(random.randint(-50,100))

while not q.empty():
	print(q.get())