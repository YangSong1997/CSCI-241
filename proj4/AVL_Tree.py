class AVL_Tree:                                                                
  # I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class _AVL_Node:                                                              
    # The Node class is private. You may add any attributes and
    # methods you need.

    def __init__(self, value):
      # -1 as left high, 1 as right high, and 0 as balanced
      self._value = value
      self._left = None
      self._right = None
      self._height = 0
      self._balance = 0

  def __init__(self):
    self._root = None

  def insert_element(self, value):                                                 
    # Insert the value specified into the tree, ensuring that
    # the tree remains balanced after the operation. Your solution
    # must be recursive. This will involve the introduction of
    # additional private methods.
    
    self._root = self.__insert(self._root, value)
    
  def __insert(self, node, value):                                              
    if node == None:             # Base case, insert at the deepest position
      node = self._AVL_Node(value)
      self._rebalance(node)
      return node
    if (value < node._value):                            
      node._left = self.__insert(node._left, value)
    if (value > node._value):
      node._right = self.__insert(node._right, value)
      
    return self._rebalance(node)                        # rebalance if needed
    
  def remove_element(self, value):                                                 
    # Remove the value specified from the tree, ensuring that
    # the tree remains balanced after the operation. Your solution
    # must be recursive. This will involve the introduction of
    # additional private methods.
    self._root = self.__remove(self._root, value) 
    # replace pass with your implementation
    
  def __remove(self, node, value):                                               
    if node == None:
      return
    if value < node._value:
      node._left = self.__remove(node._left, value)  
    if value > node._value:
      node._right = self.__remove(node._right, value)
    if value == node._value:
      if (node._left is None and node._right is None):
        return None
      if (node._left is None and node._right is not None):
        return node._right
      if (node._left is not None and node._right is None):
        return node._left
      if (node._left is not None and node._right is not None):                 
        minnode = self._findmin(node._right)
        node._value = minnode._value
        node._right = self.__remove(node._right, minnode._value)
 
    return self._rebalance(node)
        
  def _rebalance(self, node):                                                  
    # rebalance the subtree rooted at some node if needed
    self._updateheight(node)
    self._updatebalance(node)
    
    if node._balance < -1:
      if node._left._balance <= 0 :      #left/left or left/balance
        node = self.__rotateRight(node)
		
      if node._left._balance > 0 :     # left/right
        node._left = self.__rotateLeft(node._left)
        node = self.__rotateRight(node)
		
    if node._balance > 1:
      if node._right._balance >= 0:     # right/right or right/balance
        node = self.__rotateLeft(node)
	
      if node._right._balance < 0:      # right/left
        node._right = self.__rotateRight(node._right)
        node = self.__rotateLeft(node)
	
    return node
    
    
  def _updateheight(self, node):                                              
    if node._left is None and node._right is None:
      node._height = 1
    if node._left is not None and node._right is not None:
      node._height = 1 + max(node._left._height,node._right._height)
    if node._left is None and node._right is not None:
      node._height = 1 + node._right._height
    if node._left is not None and node._right is None:
      node._height = 1 + node._left._height
    return node._height
    
    
  def _updatebalance(self,node):                                              
    if node._left is None and node._right is None:
      node._balance = 0
    if node._left is not None and node._right is not None:
      node._balance =  node._right._height - node._left._height
    if node._left is None and node._right is not None:
      node._balance = node._right._height
    if node._left is not None and node._right is None:
      node._balance =  - node._left._height

  def __rotateLeft(self, node):                                               
    p = node._right
    node._right = p._left
    p._left = node
    self._updateheight(node) 
    self._updateheight(p)
    self._updatebalance(node)
    self._updatebalance(p)
    return p
	  
  def __rotateRight(self, node):                                              
    q = node._left
    node._left = q._right
    q._right = node
    self._updateheight(node) 
    self._updateheight(q)
    self._updatebalance(node)
    self._updatebalance(q)
    return q  
  
  def _findmin(self, node):                                                 
    if node is None:
      return
    elif node._left is None:
      return node
    else:
      return self._findmin(node._left)

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # TODO replace pass with your implementation
    if self._root is not None:
      stringoutput = self._inorder(self._root)
      stringoutput = "[ " + stringoutput[:len(stringoutput)-2] + " ]"
      return stringoutput
    else:
      return "[ ]"
    
  def _inorder(self, node):
    output=""
    if node is not None:
      
      if node._left is not None:
        output += self._inorder(node._left)
	
      output += str(node._value) + ", "
      
      if node._right is not None:
        output += self._inorder(node._right)
      
      return output    
  
  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # TODO replace pass with your implementation
    if self._root is not None:
      stringoutput = self._preorder(self._root)
      stringoutput = "[ " + stringoutput[:len(stringoutput)-2] + " ]"
      return stringoutput
    else:
      return "[ ]"
  
  def _preorder(self, node):
    output=""
    if node is not None:
      output += str(node._value) + ", "
      
      if node._left is not None:
        output += self._preorder(node._left)
      
      if node._right is not None:
        output += self._preorder(node._right)
      
      return output    

  def post_order(self):
    # Construct and return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # TODO replace pass with your implementation
    if self._root is not None:
      stringoutput = self._postorder(self._root)
      stringoutput = "[ " + stringoutput[:len(stringoutput)-2] + " ]"
      return stringoutput
    else:
      return "[ ]"
  
  def _postorder(self, node):
    output=""
    if node is not None:
      
      if node._left is not None:
        output += self._postorder(node._left)
      
      if node._right is not None:
        output += self._postorder(node._right)
	
      output += str(node._value) + ", "
      
      return output    

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1.
    # TODO replace pass with your implementation
    return self.__height(self._root)

  def __height(self, node):
    if node != None:
      return node._height
    else:
      return 0  

  def __str__(self):
    return self.in_order()






if __name__ == '__main__':

  ## Test 1
  ## Inserting several numbers into a tree
  ## Doing three kinds of traversals and returning the height of the tree
  
  print("test 1")
  test1 = AVL_Tree()
  print(test1.in_order())
  print(test1.pre_order())
  print(test1.post_order())
  print(test1)
  test1.insert_element(3)
  print(test1.in_order())
  print(test1.pre_order())
  print(test1.post_order())
  print(test1.get_height())
  
  test1.insert_element(2)
  print(test1.in_order())
  print(test1.pre_order())
  print(test1.post_order())
  print(test1.get_height())
  
  test1.insert_element(1)
  print(test1.in_order())
  print(test1.pre_order())
  print(test1.post_order())
  print(test1.get_height())
  
  test1.insert_element(4)
  print(test1.in_order())
  print(test1.pre_order())
  print(test1.post_order())
  print(test1.get_height())
  
  test1.insert_element(5)
  print(test1.in_order())
  print(test1.pre_order())
  print(test1.post_order())
  print(test1.get_height())
  
  print("--------------------------------------------------")
  
  
  ## Test 2
  ## Inserting and removing several numbers into a tree
  ## Doing three kinds of traversals and returning the height of the tree
  ## Removals remove leaf nodes
  print("test 2")
  test2 = AVL_Tree()
  test2.insert_element(4)
  test2.insert_element(2)
  test2.insert_element(6)
  test2.insert_element(1)
  test2.insert_element(3)
  test2.insert_element(5)
  test2.insert_element(7)
  print(test2.in_order())
  
  test2.remove_element(5)
  print(test2.in_order())
  test2.remove_element(3)
  print(test2.in_order())
  test2.remove_element(7)
  print(test2.in_order())
  test2.remove_element(1)
  print(test2.in_order())
  test2.remove_element(2)
  
  print(test2.in_order())
  
  print("--------------------------------------------------")
  
  
  ## Test 3
  ## Inserting and removing several numbers into a tree
  ## Doing three kinds of traversals and returning the height of the tree
  print("test 3")
  test3 = AVL_Tree()
  test3.insert_element(8)
  test3.insert_element(4)
  test3.insert_element(12)
  test3.insert_element(2)
  test3.insert_element(6)
  test3.insert_element(10)
  test3.insert_element(14)
  test3.insert_element(1)
  test3.insert_element(3)
  test3.insert_element(5)
  test3.insert_element(7)
  test3.insert_element(9)
  test3.insert_element(11)
  test3.insert_element(13)
  test3.insert_element(15)
  
  print(test3.in_order())
  
  test3.remove_element(5)
  print(test3.in_order())
  test3.remove_element(1)
  print(test3.in_order())
  
  print("--------------------------------------------------")
  
  
  ## Test 4
  ## Inserting and removing several numbers into a tree
  ## Doing three kinds of traversals and returning the height of the tree
  print("test 4")
  test4 = AVL_Tree()
  test4.insert_element(30)
  print(test4.in_order())
  print(test4.pre_order())
  print(test4.post_order())
  print(test4.get_height())
  
  test4.insert_element(40)
  print(test4.in_order())
  print(test4.pre_order())
  print(test4.post_order())
  print(test4.get_height())
  
  test4.insert_element(15)
  print(test4.in_order())
  print(test4.pre_order())
  print(test4.post_order())
  print(test4.get_height())
  
  test4.insert_element(25)
  print(test4.in_order())
  print(test4.pre_order())
  print(test4.post_order())
  print(test4.get_height())
  
  test4.insert_element(90)
  print(test4.in_order())
  print(test4.pre_order())
  print(test4.post_order())
  print(test4.get_height())
  
  test4.insert_element(80)
  print(test4.in_order())
  print(test4.pre_order())
  print(test4.post_order())
  print(test4.get_height())
  
  test4.insert_element(70)
  print(test4.in_order())
  print(test4.pre_order())
  print(test4.post_order())
  print(test4.get_height())
  
  test4.insert_element(85)
  print(test4.in_order())
  print(test4.pre_order())
  print(test4.post_order())
  print(test4.get_height())
  
  test4.insert_element(15)
  print(test4.in_order())
  print(test4.pre_order())
  print(test4.post_order())
  print(test4.get_height())
  
  test4.insert_element(72)
  print(test4.in_order())
  print(test4.pre_order())
  print(test4.post_order())
  print(test4.get_height())
  
  test4.remove_element(80)
  print(test4.in_order())
  print(test4.pre_order())
  print(test4.post_order())
  print(test4.get_height())
  
  
  test4.remove_element(85)
  print(test4.in_order())
  print(test4.pre_order())
  print(test4.post_order())
  print(test4.get_height())
  
  
  ##test4.remove_element(90)
  ##print(test4.in_order())
  ##print(test4.pre_order())
  ##print(test4.post_order())
  ##print(test4.get_height())
  
  
  test4.remove_element(30)
  print(test4.in_order())
  print(test4.pre_order())
  print(test4.post_order())
  print(test4.get_height())
  
  test4.remove_element(100)
  print(test4.in_order())
  print(test4.pre_order())
  print(test4.post_order())
  print(test4.get_height())  
  
  print("--------------------------------------------------")
  
