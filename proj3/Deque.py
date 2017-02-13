from Linked_List import Linked_List

class Deque:

  def __init__(self):
    self._list = Linked_List()

  def __str__(self):
    return str(self._list)

  def __len__(self):
    return len(self._list)

  def push_front(self, val):
    #TODO
    if len(self._list) == 0:
      self._list.append_element(val)
    else:
      self._list.insert_element_at(val, 0)
  
  def pop_front(self):
    #TODO
    return self._list.remove_element_at(0)

  def peek_front(self):
    #TODO
    return self._list.get_element_at(0)
    
  def push_back(self, val):
    #TODO
    self._list.append_element(val)
  
  def pop_back(self):
    #TODO
    return self._list.remove_element_at(len(self._list) - 1)

  def peek_back(self):
    #TODO
    return self._list.get_element_at(len(self._list) - 1)

if __name__ == '__main__':
  #TODO test cases here

  
  deque2 = Deque()
  deque2.push_front(4)
  print(deque2)
  print("Deque size is: " + str(len(deque2)))  

  #prints an empty deque and shows correct size
  deque1 = Deque()
  print(deque1)
  print("Deque size is: " + str(len(deque1)))
  deque1.pop_back()
  #adds four elements, prints the list, and shows correct size
  deque1.push_back(4)
  print(deque1)
  print("Deque size is: " + str(len(deque1)))
  deque1.push_back(5)
  print(deque1)
  print("Deque size is: " + str(len(deque1)))
  deque1.push_front(2)
  print(deque1)
  print("Deque size is: " + str(len(deque1)))
  deque1.push_front(1)
  print(deque1)
  print("Deque size is: " + str(len(deque1)))
  deque1.push_back(7)
  print(deque1)
  print("Deque size is: " + str(len(deque1)))
  deque1.push_front(11)
  print(deque1)
  print("Deque size is: " + str(len(deque1)))
  deque1.pop_front()
  print(deque1)
  print("Deque size is: " + str(len(deque1)))
  deque1.pop_back()
  print(deque1)
  print("Deque size is: " + str(len(deque1)))
  print(deque1.peek_back())
  print("Deque size is: " + str(len(deque1)))
  print(deque1.peek_front())
  print("Deque size is: " + str(len(deque1)))
  
  print("------------------------------------------------------")  
  
  deque2 = Deque()
  deque2.pop_front()
  print(deque2)
  print("Deque size is: " + str(len(deque2)))  
  print(deque2.peek_front())
  print("Deque size is: " + str(len(deque2)))
  print(deque2.peek_back())
  print("Deque size is: " + str(len(deque2)))  
  deque2.push_front(4)
  print(deque2)
  print("Deque size is: " + str(len(deque2)))    
  

  