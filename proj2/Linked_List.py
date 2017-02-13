class Linked_List:
  
  class _Node:
    
    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      self._val = val
      self._next = None
      self._prev = None

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    self._header = Linked_List._Node(None)
    self._trailer = Linked_List._Node(None)
    self._header._prev = None
    self._header._next = self._trailer
    self._trailer._prev = self._header
    self._trailer._next = None
    self._size = 0

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    return self._size

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the tail position.
    newNode = Linked_List._Node(val)
    newNode._next = self._trailer
    newNode._prev = self._trailer._prev
    self._trailer._prev._next = newNode
    self._trailer._prev = newNode
    self._size += 1
    
  def insert_element_at(self, val, index):
    # assuming the head position is indexed 0, add a
    # node containing val at the specified index. If 
    # the index is not a valid position within the list,
    # ignore the request. This method cannot be used
    # to add an item at the tail position.
    if index >= self._size or index < 0:
      return
    
    newNode = Linked_List._Node(val)
    
    if index == 0:
      newNode._next = self._header._next
      self._header._next._prev = newNode
      newNode._prev = self._header
      self._header._next = newNode
    else:
      current = self._header
      for i in range(index):
          current = current._next
        
      newNode._next = current._next
      current._next._prev = newNode
      current._next = newNode
      newNode._prev = current 
    self._size += 1

  def remove_element_at(self, index):
    # assuming the head position is indexed 0, remove
    # and return the value stored in the node at the 
    # specified index. If the index is invalid, ignore
    # the request.
    if index >= self._size or index < 0:
      return
    
    if index == 0:
      current = self._header._next
      self._header._next = current._next
      current._next._prev = self._header
    else:
      current = self._header
      for i in range(index):
          current = current._next
      current._next._next._prev = current
      current._next = current._next._next
      
    self._size -= 1

  def get_element_at(self, index):
    # assuming the head position is indexed 0, return
    # the value stored in the node at the specified
    # index, but do not unlink it from the list.
    if index >= self._size or index < 0:
      return
    if self._size == 0:
      return
    current = self._header
    for i in range(index):
      current = current._next
    current = current._next
    return current._val
      

  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    
    current = self._header._next
    returnstring = '[ '
    while current is not self._trailer:
      if current == self._trailer._prev:
        returnstring = str(returnstring) + str(current._val) + ' '
      else:
        returnstring = str(returnstring) + str(current._val) + ', '
      current = current._next
    returnstring = str(returnstring) + ']'
    return returnstring
    

class Poly_Val:
  def __init__(self, coef, exp):
    self._coefficient = coef
    self._exponent = exp

  def get_coefficient(self):
    return self._coefficient

  def get_exponent(self):
    return self._exponent

  def __str__(self):
    return str(self._coefficient) + 'x^' + str(self._exponent)
  
if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods ignore your
  # requests when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location?

  # The following code should appear after your tests for your
  # linked list class.

  #A test for adding to a list
  print("Test 1:")
  #prints an empty list and shows correct size
  List1 = Linked_List()
  print(List1)
  print("List size is: " + str(List1._size))
  #adds four elements, prints the list, and shows correct size
  List1.append_element(4)
  print(List1)
  print("List size is: " + str(List1._size))
  List1.append_element(5)
  print(List1)
  print("List size is: " + str(List1._size))
  List1.append_element(2)
  print(List1)
  print("List size is: " + str(List1._size))
  #inserts an element at the beginning and shows correct size
  List1.insert_element_at(1,0)
  print(List1)
  print("List size is: " + str(List1._size))
  #inserts an element in the middle and shows correct size
  List1.insert_element_at(7,3)
  print(List1)
  print("List size is: " + str(List1._size))
  #tries to insert an element out of bounds, is unsuccesful
  List1.insert_element_at(11,10)
  print(List1)
  print("List size is: " + str(List1._size))
  List1.append_element(10)
  print(List1)
  print("List size is: " + str(List1._size))
  #attempts to append an element using the insert element method, it's succesfully unsuccesful
  List1.insert_element_at(11,6)
  print(List1)
  print("List size is: " + str(List1._size))

  #A test for removing from the list
  print()
  print("Test 2:")
  List2 = List1
  print(List2)
  print("List size is: " + str(List2._size))
  #removes the beginning element and prints the correct size
  List2.remove_element_at(0)
  print(List2)
  print("List size is: " + str(List2._size))
  #removes an element from the middle and prints the correct size
  List2.remove_element_at(3)
  print(List2)
  print("List size is: " + str(List2._size))
  #tries to remove from an index larger than the list size, is unsuccesful
  List2.remove_element_at(10)
  print(List2)
  print("List size is: " + str(List2._size))
  #removes the last element in the list and prints correct size
  List2.remove_element_at(3)
  print(List2)
  print("List size is: " + str(List2._size))

  #Shows the printing of the elements within the list
  print()
  print("Test 3:")
  List3 = List2
  print("Node at 0 is: ")
  print(List3.get_element_at(0))
  print("Node at 1 is: ")
  print(List3.get_element_at(1))
  print("Node at 2 is: ")
  print(List3.get_element_at(2))
  #tries to get a Node at an index that is out of bounds, is unsuccesful
  print("Node at 10 is: ")
  print(List3.get_element_at(10))


    

  # here, create the Poly_Val objects that should comprise p3
  # and add them to the list. Make sure that p3 is constructed
  # correctly regardless of the contents of p1 and p2. Try
  # building different polynomials for p1 and p2 and ensure that
  # they sum correctly.

  #creates an ordered list of polynomials off of two lists of polynomials
  p1 = Linked_List()
  p1.append_element(Poly_Val(10,1012))
  p1.append_element(Poly_Val(5,14))
  p1.append_element(Poly_Val(1,0))
  p2 = Linked_List()
  p2.append_element(Poly_Val(3,1990))
  p2.append_element(Poly_Val(-2,14))
  p2.append_element(Poly_Val(11,1))
  p2.append_element(Poly_Val(5,0))
  
  
  print()
  print("Test 4:")
  p3 = Linked_List()    
  k = 0
  p1size = p1._size
  p2size = p2._size
  for i in range(p1size):
    p1element = p1.get_element_at(i)
    for j in range(k,p2size):
      p2element = p2.get_element_at(j)
      if p2element.get_exponent() > p1element.get_exponent():
        p3.append_element(p2element)
        k += 1
        temp = p2element.get_exponent()
      if p2element.get_exponent() == p1element.get_exponent():
        coefficient = p2element.get_coefficient() + p1element.get_coefficient()
        exponent = p2element.get_exponent()
        p3.append_element(Poly_Val(coefficient,exponent))
        k += 1
        temp = p2element.get_exponent()

    if temp > p1element.get_exponent():
      p3.append_element(p1element)
  print(p3)


  #creates an ordered list of polynomials off of two lists of polynomials
  p1 = Linked_List()
  p1.append_element(Poly_Val(11,100))
  p1.append_element(Poly_Val(6,50))
  p1.append_element(Poly_Val(7,2))
  p1.append_element(Poly_Val(7,1))
  p1.append_element(Poly_Val(7,0))
  p2 = Linked_List()
  p2.append_element(Poly_Val(3,100))
  p2.append_element(Poly_Val(4,75))
  p2.append_element(Poly_Val(-11,2))
  
  
  print()
  print("Test 5:")
  p3 = Linked_List()    
  k = 0
  p1size = p1._size
  p2size = p2._size
  for i in range(p1size):
    p1element = p1.get_element_at(i)
    for j in range(k,p2size):
      p2element = p2.get_element_at(j)
      if p2element.get_exponent() > p1element.get_exponent():
        p3.append_element(p2element)
        k += 1
        temp = p2element.get_exponent()
      if p2element.get_exponent() == p1element.get_exponent():
        coefficient = p2element.get_coefficient() + p1element.get_coefficient()
        exponent = p2element.get_exponent()
        p3.append_element(Poly_Val(coefficient,exponent))
        k += 1
        temp = p2element.get_exponent()

    if temp > p1element.get_exponent():
      p3.append_element(p1element)
  print(p3)


#creates an ordered list of polynomials off of two lists of polynomials
  p1 = Linked_List()
  p1.append_element(Poly_Val(16,150))
  p1.append_element(Poly_Val(-8,75))
  p1.append_element(Poly_Val(8,40))
  p1.append_element(Poly_Val(1,0))
  p2 = Linked_List()
  p2.append_element(Poly_Val(3,100))
  p2.append_element(Poly_Val(-2,75))
  p2.append_element(Poly_Val(22,40))
  p2.append_element(Poly_Val(11,11))
  p2.append_element(Poly_Val(5,5))
  p2.append_element(Poly_Val(5,4))
  p2.append_element(Poly_Val(5,2))
  
  
  print()
  print("Test 6:")
  p3 = Linked_List()    
  k = 0
  p1size = p1._size
  p2size = p2._size
  for i in range(p1size):
    p1element = p1.get_element_at(i)
    for j in range(k,p2size):
      p2element = p2.get_element_at(j)
      if p2element.get_exponent() > p1element.get_exponent():
        p3.append_element(p2element)
        k += 1
        temp = p2element.get_exponent()
      if p2element.get_exponent() == p1element.get_exponent():
        coefficient = p2element.get_coefficient() + p1element.get_coefficient()
        exponent = p2element.get_exponent()
        p3.append_element(Poly_Val(coefficient,exponent))
        k += 1
        temp = p2element.get_exponent()
    if temp > p1element.get_exponent():
      p3.append_element(p1element)
  print(p3)
