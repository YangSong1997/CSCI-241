from Deque import Deque

class Queue:

  def __init__(self):
    self._dq = Deque()

  def __str__(self):
    #TODO
    return str(self._dq)

  def __len__(self):
    #TODO
    return len(self._dq)

  def enqueue(self, val):
    #TODO
    self._dq.push_front(val)

  def dequeue(self):
    #TODO
    return self._dq.pop_back()
  

if __name__ == '__main__':
  #TODO test cases here
  queue1 = Queue()
  print(queue1)
  print("Queue size is: " + str(len(queue1)))
  queue1.dequeue()
  print(queue1)
  print("Queue size is: " + str(len(queue1)))
  queue1.enqueue(4)
  print(queue1)
  print("Queue size is: " + str(len(queue1)))
  queue1.enqueue(5)
  print(queue1)
  print("Queue size is: " + str(len(queue1)))
  queue1.dequeue()
  print(queue1)
  print("Queue size is: " + str(len(queue1)))
  queue1.dequeue()
  print(queue1)
  print("Queue size is: " + str(len(queue1)))
  queue1.enqueue(7)
  print(queue1)
  print("Queue size is: " + str(len(queue1)))
  queue1.enqueue(11)
  print(queue1)
  print("Queue size is: " + str(len(queue1)))
  queue1.enqueue(35)
  print(queue1)
  print("Queue size is: " + str(len(queue1)))
  queue1.enqueue(8)
  print(queue1)
  print("Queue size is: " + str(len(queue1)))
  queue1.dequeue()
  print(queue1)
  print("Queue size is: " + str(len(queue1)))  
  queue1.dequeue()
  print(queue1)
  print("Queue size is: " + str(len(queue1)))  
  