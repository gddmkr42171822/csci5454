'''

Sources:
---------
  Introduction to Algorithms, Third Edition (page 294)
    - Insert, rotate, delete, Search successor methods of binary tree
  https://stackoverflow.com/questions/20242479/printing-a-tree-data-structure-in-python
    - How to print a tree data structure that is understandable
  https://www.youtube.com/watch?v=FNeL18KsWPc
    - MIT video lecture on AVL trees
  https://en.wikipedia.org/wiki/AVL_tree
    - AVL Tree cases
  https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
    - Visualization of an avl tree for creating my tests
'''
import random
import matplotlib.pyplot as plt
import math

steps_executed = 0.0
space_used = 0.0

xlabel = ''
ylabel = ''
title = ''
filename = ''
c1 = 0.0
c2 = 0.0


class AVLTree(object):


  def __init__(self):
    self.root = NullAVLNode()
  

  def Insert(self,key):
    global steps_executed, space_used
     
    # Create a new node with the key argument of insert
    new_node = AVLNode(key) 

    parent_node = NullAVLNode() # This will be used to store the parent node
    current_node = self.root # Start the insert at root of the tree

    # If there are nodes in the tree
    while not isinstance(current_node, NullAVLNode):
      
      steps_executed += 1

      parent_node = current_node # Set y to the parent node

      # Insert into the left part of the tree if the key of the new node 
      # is less than the key of the current node we are looking at
      if new_node.key < current_node.key: 
        current_node = current_node.left_child
      else:
      # Insert into the right part of the tree
      # if the key of the new node is less than
      # the key of the current node we are looking at
        current_node = current_node.right_child

    new_node.parent = parent_node # Set the parent node of the new node

    # Set the root node of the tree to the new node
    # if the tree is empty
    if isinstance(parent_node, NullAVLNode):
      self.root = new_node
    # Set the left child of the parent node to the new node
    elif new_node.key < parent_node.key:
    # Set the height of the new node
      parent_node.left_child = new_node
    # Set the right child of the parent to the new node
    else:
    # Set the height of the new node
      parent_node.right_child = new_node

    # Update heights and balance of the new node and the nodes around it
    self.UpdateHeightAndBalance(new_node)
    
    space_used += 1


  def Search(self, key):
    
    global steps_executed
  
    # Check if the tree is empty
    if isinstance(self.root, NullAVLNode):
      print 'Search: Tree is empty.'
      return

    node = self.root # Start looking for the key at the root node

    while not isinstance(node, NullAVLNode):
      
      steps_executed += 1
      
      # If we Search the a node that has the same key we are looking for
      # return it
      if key == node.key:
        return node
      elif key < node.key:
        node = node.left_child
      else:
        node = node.right_child
    # If we don't find a node in the tree with the
    # key we are looking for return empty node
    return NullAVLNode()

  def Delete(self, key):
    global space_used

    # Check if the tree is empty
    if isinstance(self.root, NullAVLNode):
      print 'Delete: Tree is empty.'
      return

    # Node to be removed
    node = self.Search(key)

    if isinstance(node, NullAVLNode):
      print 'Delete: Key not found in tree %d' % key
      return

    # If the key is found in a leaf node
    if isinstance(node.right_child, NullAVLNode) and isinstance(node.left_child, NullAVLNode):
      # Check the which child of the parent the leaf node belongs to and delete it
      if node.parent.right_child is node:
        node.parent.right_child = NullAVLNode()
      else:
        node.parent.left_child = NullAVLNode()
      
      self.UpdateHeightAndBalance(node.parent)
    # If the key is found in a node with only a left child
    # Left child takes the nodes place
    elif not isinstance(node.left_child, NullAVLNode) and isinstance(node.right_child, NullAVLNode):
      self.Transplant(node, node.left_child)
      self.UpdateHeightAndBalance(node.left_child)

    # If the key is found in a node with only a right child
    # Right child takes the nodes place
    elif not isinstance(node.right_child, NullAVLNode) and isinstance(node.left_child, NullAVLNode):
      self.Transplant(node, node.right_child)
      self.UpdateHeightAndBalance(node.right_child)

    # If the key is found in a node with both a left and a right child
    # Successor node takes the nodes place
    else:
      successor = self.SearchSuccessor(node)

      # Choose the correct node to start the height update 
      # from after removing a node
      x = None
      if successor.parent is not node:
        x = successor.parent
      else:
        x = successor

      # Check if the successor is not the right child of the node we are deleting
      # This means we have to traverse down the left tree of the right child
      # to Search the successor to the node we are deleting
      if successor.parent is not node:
        # Move the right child of the successor into the successor's place
        self.Transplant(successor, successor.right_child)
        # Move successor into place of the node we are deleting
        # Set the successor's right child to the right child 
        # of the node we are deleting
        successor.right_child = node.right_child
        # Set the node's right child parent to the successor
        successor.right_child.parent = successor

      # Move the successor into the node we are going to remove's place
      self.Transplant(node,successor)
      # Set the left child of the successor to the node's left child
      successor.left_child = node.left_child
      # Set the parent of the left child to the successor
      successor.left_child.parent = successor
      
      self.UpdateHeightAndBalance(x)
      
      space_used -= 1


  def SearchSuccessor(self, node):
    global steps_executed
    
    # Set node to its right child
    node = node.right_child
    while not isinstance(node.left_child, NullAVLNode):
      
      steps_executed += 1
      
      # Traverse down left side of right child
      # to Search successor at the end
      node = node.left_child
    return node


  def Transplant(self, node, node_successor):
    global steps_executed
    steps_executed += 1
    
    # If the node we are deleting is the root
    # The root is now the child of that node (could be none)
    if isinstance(node.parent, NullAVLNode):
      self.root = node_successor

    # Check which child of the parent the current node we want to delete belongs to
    # If the node is the parent's right child
    elif node.parent.right_child is node:
      # Set the parent's right child to the child of the node to be deleted
      node.parent.right_child = node_successor

    # If the node is the parent's left child
    else:
      # Set the parent's right child to the child of the node to be deleted
      node.parent.left_child = node_successor

    # Set the parent of node that will take over
    # the deleted nodes position
    if not isinstance(node_successor, NullAVLNode):
      node_successor.parent = node.parent


  def PrintTree(self, current_node, depth):
    
    # Check if the tree is empty
    if isinstance(self.root, NullAVLNode):
      print 'PrintTree: Tree is empty.'
      return

    if not isinstance(current_node, NullAVLNode):

      # Print the left side of the parent
      if not isinstance(current_node.left_child, NullAVLNode):
        self.PrintTree(current_node.left_child, depth-1)
        print '\t' * (depth-1) + '    \\'
      
      # Print the parent node
      print '\t' * depth + str(current_node.key) + '(' + str(current_node.height) + ')'

      # Print the right side of the parent
      if not isinstance(current_node.right_child, NullAVLNode):
        print '\t' * (depth-1) + '    /'
        self.PrintTree(current_node.right_child, depth-1)


  def UpdateHeightAndBalance(self, node):
    global steps_executed
    steps_executed += 1 

    # Check if the tree is empty
    if isinstance(self.root, NullAVLNode):
      print 'UpdateHeightAndBalance: Tree is empty.'
      return

    self.UpdateBalance(node)

    # Calculate the height by taking the maximum height of the children
    # and adding 1
    node.height = max(node.left_child.height, node.right_child.height) + 1   

    if not isinstance(node.parent, NullAVLNode):
      self.UpdateHeightAndBalance(node.parent)


  def LeftRotate(self,x):
    global steps_executed
    steps_executed += 1
        
    # Check if the tree is empty
    if isinstance(self.root, NullAVLNode):
      print 'LeftRotate: Tree is empty.'
      return
    
    y = x.right_child
    x.right_child = y.left_child
    
    if not isinstance(y.left_child, NullAVLNode):
      y.left_child.parent = x
    
    y.parent = x.parent

    if isinstance(x.parent, NullAVLNode):
      self.root = y
    elif x.parent.left_child is x:
      x.parent.left_child = y
    elif x.parent.right_child is x:
      x.parent.right_child = y

    y.left_child = x
    x.parent = y

    x.height = max(x.left_child.height, x.right_child.height) + 1


  def RightRotate(self,y):  
    global steps_executed
    steps_executed += 1
      
    # Check if the tree is empty
    if isinstance(self.root, NullAVLNode):
      print 'RightRotate: Tree is empty.'
      return
    
    x = y.left_child
    y.left_child = x.right_child

    if not isinstance(x.right_child, NullAVLNode):
      x.right_child.parent = y

    x.parent = y.parent

    if isinstance(y.parent, NullAVLNode):
      self.root = x
    elif y is y.parent.left_child:
      y.parent.left_child = x
    elif y is y.parent.right_child:
      y.parent.right_child = x

    x.right_child = y
    y.parent = x
    
    y.height = max(y.left_child.height, y.right_child.height) + 1


  def UpdateBalance(self, x):
    if abs(x.left_child.height - x.right_child.height) <= 1:
      pass
    # Left heavy child sub tree
    elif x.left_child.height > x.right_child.height:
      y = x.left_child
      if y.left_child.height < y.right_child.height:
        self.LeftRotate(y)
      self.RightRotate(x)
    # Right heavy child sub tree
    elif x.left_child.height < x.right_child.height:
      y = x.right_child
      if y.left_child.height > y.right_child.height:
        self.RightRotate(y)
      self.LeftRotate(x)


class AVLNode(object):

  
  def __init__(self, key):
    self.left_child = NullAVLNode()
    self.right_child = NullAVLNode()
    self.parent = NullAVLNode()
    self.key = key
    self.height = 0


class NullAVLNode(object):


  def __init__(self):
    self.key = 'null'
    self.height = -1
    

def CreateAVLTree(size):
  tree = AVLTree()
  
  for i in range(size):
    tree.Insert(i)
    
#   tree.PrintTree(tree.root, tree.root.height)
  
  return tree
    

def GraphRuntime(x,y):
  global xlabel, ylabel, title, filename, c1, c2
  
  c1_y = [c1*math.log(i, 2) for i in x]
  c2_y = [c2*math.log(i, 2) for i in x]
  
  a = plt.scatter(x,y,color='r')
  b = plt.scatter(x,c1_y,color='g')
  c = plt.scatter(x,c2_y,color='b')
  
  plt.yscale('log')
  plt.xscale('log')
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.legend((a,b,c), ('f(n)', 'c1*g(n)', 'c2*g(n)'), loc=2)
  plt.title(title)
  plt.savefig(filename)
  plt.close()
  
def GraphSpace(x,y):
  global xlabel, ylabel, title, filename, c1, c2
  
  c1_y = [c1*i for i in x]
  c2_y = [c2*i for i in x]
  
  a = plt.scatter(x,y,color='r')
  b = plt.scatter(x,c1_y,color='g')
  c = plt.scatter(x,c2_y,color='b')
  
  plt.yscale('log')
  plt.xscale('log')
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.legend((a,b,c), ('f(n)', 'c1*g(n)', 'c2*g(n)'), loc=2)
  plt.title(title)
  plt.savefig(filename)
  plt.close()
  
  
def SpaceUsed():
  global space_used
  global xlabel, ylabel, title, filename, c1, c2
  input_size_and_space_used = {}
  
  for i in range(4, 16):
    n = 50
    average_space_used = 0.0
    for _ in range(n):
      size = 2**i
      space_used = 0.0
      CreateAVLTree(size)
      average_space_used += space_used
      space_used = 0.0
    
    average_space_used = average_space_used/n
    input_size_and_space_used[size] = average_space_used
    print 'Size of tree %d nodes and average space used %f' % (size, average_space_used)
  
  
  
  xlabel = 'Number of nodes in the avl tree'
  ylabel = 'Number of operations'
  title = 'Space used by an avl tree'
  filename = 'space_used.png'
  c1 = .5
  c2 = 2  
  
  GraphSpace(input_size_and_space_used.keys(), input_size_and_space_used.values())
  
  
def RuntimeOfDelete():
  global steps_executed
  global xlabel, ylabel, title, filename, c1, c2
  
  input_size_and_steps_executed = {}
  
  for i in range(4, 16):
    n = 50
    average_delete_steps_executed = 0.0
    for _ in range(n):
      size = 2**i
      tree = CreateAVLTree(size)
      steps_executed = 0.0
      key = random.randint(0,size-1)
      tree.Delete(key)
      average_delete_steps_executed += steps_executed
      steps_executed = 0.0
     
    average_delete_steps_executed = average_delete_steps_executed/n
    input_size_and_steps_executed[size] = average_delete_steps_executed
    print 'Size of tree %d nodes and average insert steps executed %f' % (size, average_delete_steps_executed)
      
#   print 'Input size and number of steps executed', input_size_and_steps_executed
  
  xlabel = 'Number of nodes in the avl tree'
  ylabel = 'Number of operations'
  title = 'Runtime of deleting a node from an avl tree'
  filename = 'delete_runtime.png'
  c1 = 1
  c2 = 4
  
  GraphRuntime(input_size_and_steps_executed.keys(), input_size_and_steps_executed.values())


def RuntimeOfInsert():
  global steps_executed
  global xlabel, ylabel, title, filename, c1, c2
    
  input_size_and_steps_executed = {}
  
  for i in range(4, 16):
    n = 50
    average_insert_steps_executed = 0.0
    for _ in range(n):
      size = 2**i
      tree = CreateAVLTree(size)
      steps_executed = 0.0
      key = random.randint(0,size-1)
      tree.Insert(key)
      average_insert_steps_executed += steps_executed
      steps_executed = 0.0
     
    average_insert_steps_executed = average_insert_steps_executed/n
    input_size_and_steps_executed[size] = average_insert_steps_executed
    print 'Size of tree %d nodes and average insert steps executed %f' % (size, average_insert_steps_executed)
      
#   print 'Input size and number of steps executed', input_size_and_steps_executed
  
  xlabel = 'Number of nodes in the avl tree'
  ylabel = 'Number of operations'
  title = 'Runtime of inserting a node into an avl tree'
  filename = 'insert_runtime.png'
  c1 = 1
  c2 = 4
  
  GraphRuntime(input_size_and_steps_executed.keys(), input_size_and_steps_executed.values())


def RuntimeOfSearch():
  global steps_executed
  global xlabel, ylabel, title, filename, c1, c2
  
  input_size_and_steps_executed = {}

  
  for i in range(4, 16):
    n = 50
    average_search_steps_executed = 0.0
    for _ in range(n):
      size = 2**i
      tree = CreateAVLTree(size)
      steps_executed = 0.0
      key = random.randint(0,size-1)
      tree.Search(key)
      average_search_steps_executed += steps_executed
      steps_executed = 0.0
    
    average_search_steps_executed = average_search_steps_executed/n
    input_size_and_steps_executed[size] = average_search_steps_executed
    print 'Size of tree %d nodes and average search steps executed %f' % (size, average_search_steps_executed)
    
#   print 'Input size and number of steps executed', input_size_and_steps_executed
  
  xlabel = 'Number of nodes in the avl tree'
  ylabel = 'Number of operations'
  title = 'Runtime of searching for a node in an avl tree'
  filename = 'search_runtime.png'
  c1 = .5
  c2 = 2
  
  GraphRuntime(input_size_and_steps_executed.keys(), input_size_and_steps_executed.values())
  

def Main():
#   RuntimeOfSearch()
#   RuntimeOfInsert()
#   RuntimeOfDelete()
  SpaceUsed()
  
  
if __name__ == '__main__':
  Main()
