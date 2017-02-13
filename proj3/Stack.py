from Deque import Deque

class Stack:

  def __init__(self):
    self._dq = Deque()

  def __str__(self):
    #TODO
    return str(self._dq)

  def __len__(self):
    #TODO
    return len(self._dq)

  def push(self, val):
    #TODO
    self._dq.push_front(val)

  def pop(self):
    #TODO
    return self._dq.pop_front()

  def peek(self):
    #TODO
    return self._dq.peek_front()
    

if __name__ == '__main__':
  #TODO test cases here
  stack1 = Stack()
  print(stack1)
  print("Stack size is: " + str(len(stack1)))
  print(stack1.pop())
  print(stack1)
  print("Stack size is: " + str(len(stack1)))
  print(stack1.peek())
  print(stack1)
  print("Stack size is: " + str(len(stack1)))      
  stack1.push(4)
  print(stack1)
  print("Stack size is: " + str(len(stack1)))
  print(stack1.peek())
  print(stack1)
  print("Stack size is: " + str(len(stack1)))  
  stack1.push(5)
  print(stack1)
  print("Stack size is: " + str(len(stack1)))
  stack1.push(6)
  print(stack1)
  print("Stack size is: " + str(len(stack1)))
  stack1.pop()
  print(stack1)
  print("Stack size is: " + str(len(stack1)))
  stack1.push(7)
  print(stack1)
  print("Stack size is: " + str(len(stack1)))
  print(stack1.peek())
  print(stack1)
  print("Stack size is: " + str(len(stack1)))    
  stack1.push(11)
  print(stack1)
  print("Stack size is: " + str(len(stack1)))
  stack1.pop()
  print(stack1)
  print("Stack size is: " + str(len(stack1)))
  stack1.push(8)
  print(stack1)
  print("Stack size is: " + str(len(stack1)))
  stack1.pop()
  print(stack1)
  print("Stack size is: " + str(len(stack1))) 
  print(stack1.peek())
  print(stack1)
  print("Stack size is: " + str(len(stack1)))    
  stack1.pop()
  print(stack1)
  print("Stack size is: " + str(len(stack1)))