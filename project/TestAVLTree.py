from AVLTree import AVLTree
from AVLTree import NullAVLNode

def CreateBasicTree():
  tree = AVLTree()
  tree.Insert(5) # Root node
  tree.Insert(3)
  tree.Insert(4)
  tree.Insert(6)
  tree.Insert(5.5)
  tree.Insert(7)
  tree.Insert(6.6)
  tree.Insert(6.5)
  tree.Insert(8)
  tree.Insert(2)
  tree.Insert(1)
  
  return tree

def CreateRightUnBalancedTree():
  tree = AVLTree()
  tree.Insert(3)
  tree.Insert(5)
  tree.Insert(7)

  return tree

def CreateLeftUnBalancedTree():
  tree = AVLTree()
  tree.Insert(7)
  tree.Insert(5)
  tree.Insert(3)

  return tree

def TestInsert():
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: Insert Nodes into tree' + bcolors.ENDC
  tree = CreateBasicTree()
  #tree.PrintTree(tree.root, tree.root.height)
  
  root = tree.Find(5)
  Test('Insert method root is 5', tree.root.key == root.key)

  Test('Insert method right child of root is 6', root.right_child.key == tree.root.right_child.key)
  Test('Insert method left child of root is 3', root.left_child.key == tree.root.left_child.key)
  

def TestLeftRotate():
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: Left Rotate Tree' + bcolors.ENDC
  tree = CreateRightUnBalancedTree()
  #tree.PrintTree(tree.root, tree.root.height)

  tree.LeftRotate(tree.root)

  #tree.PrintTree(tree.root, tree.root.height)

  root = tree.Find(5)
  Test('Rotate method new root node is 5', tree.root.key == root.key)
  Test('Rotate method height of root node is 1', root.height == 1)
  
  Test('Rotate method left child of root is 3', tree.root.left_child.key == 3)
  Test('Rotate method right child of root is 7', tree.root.right_child.key == 7)

  Test('Rotate method height of left child of new root is 0', tree.root.left_child.height == 0)

def TestRightRotate():
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: Right Rotate Tree' + bcolors.ENDC
  tree = CreateLeftUnBalancedTree()
  #tree.PrintTree(tree.root, tree.root.height)

  tree.RightRotate(tree.root)

  #tree.PrintTree(tree.root, tree.root.height)

  root = tree.Find(5)
  Test('Rotate method new root node is 5', tree.root.key == root.key)
  Test('Rotate method height of root node is 1', root.height == 1)
  
  Test('Rotate method left child of root is 3', tree.root.left_child.key == 3)
  Test('Rotate method right child of root is 7', tree.root.right_child.key == 7)
  
  Test('Rotate method height of right child of new root is 0', tree.root.right_child.height == 0)


def TestFind():

	#
  # Tests for finding a node
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: Find a node' + bcolors.ENDC
  
  tree = CreateBasicTree()

  node = tree.Find(10)
  Test('Find method with key 10 not in tree.', isinstance(node, NullAVLNode))

  node = tree.Find(2)
  Test('Find method with key 2 in tree.', node.key == 2)

def TestFindSuccessor():
	print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: FindSuccessor of a node' + bcolors.ENDC
	tree = CreateBasicTree()
	#tree.PrintTree(tree.root)

	node = tree.Find(6)
	successor = tree.FindSuccessor(node)
	node = tree.Find(6.5)
	Test('Successor of 6 is 6.5.', successor is node)

	node = tree.Find(5)
	successor = tree.FindSuccessor(node)
	node = tree.Find(5.5)
	Test('Successor of 5 is 5.5.', successor is node)


def TestDelete():

  #
  # Tests for deleting a leaf node
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: Delete a leaf node' + bcolors.ENDC

  tree = CreateBasicTree()
  #tree.PrintTree(tree.root, tree.root.height)

  tree.Delete(8)
  #tree.PrintTree(tree.root, tree.root.height)
  node = tree.Find(8)
  Test('Delete method with leaf node: 8 is removed.', isinstance(node, NullAVLNode))

  tree.Delete(4)
  #tree.PrintTree(tree.root)
  node = tree.Find(4)
  Test('Delete method with leaf node: 4 is removed.', isinstance(node, NullAVLNode))

  tree.Delete(1)
  #tree.PrintTree(tree.root, tree.root.height)
  node = tree.Find(1)
  Test('Delete method with leaf node: 1 is removed.', isinstance(node, NullAVLNode))

  #
  # Tests for deleting node with single child
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: Delete node with single child' + bcolors.ENDC

  tree = CreateBasicTree()
  #tree.PrintTree(tree.root, tree.root.height)
  tree.Delete(2)
  #tree.PrintTree(tree.root, tree.root.height)
  node = tree.Find(2)
  Test('Delete method with left child: 2 is removed.', isinstance(node, NullAVLNode))
  parent = tree.Find(3)
  child = tree.Find(1)
  Test('Delete method with left child: Left child of 3 is 1.', parent.left_child is child)
  Test('Delete method with left child: Parent of 1 is 3.', child.parent is parent)
  tree.Delete(7)
  #tree.PrintTree(tree.root, tree.root.height)
  node = tree.Find(7)
  Test('Delete method with right child: 7 is removed.', isinstance(node, NullAVLNode))
  parent = tree.Find(6)
  child = tree.Find(8)
  Test('Delete method with right child: Right child of 6 is 8.', parent.right_child is child)
  Test('Delete method with right child: Parent of 8 is 6.', child.parent is parent)

  node = tree.Find(6.6)

  Test('Delete method with right child: Left child of 8 is 6.6.', child.left_child is node)  
  Test('Delete method with right child: Height of 8 is 2.', child.height == 2)


  #
  # Tests for deleting node with both children
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: Delete node with two children' + bcolors.ENDC

  tree = CreateBasicTree()
  #tree.PrintTree(tree.root, tree.root.height)

  tree.Delete(6)
  #tree.PrintTree(tree.root, tree.root.height)

  node = tree.Find(6)
  Test('Delete method with both children: 6 no longer exists.', isinstance(node, NullAVLNode))
  parent = tree.Find(5)
  child = tree.Find(6.5)
  Test('Delete method with both children: Right child of 5 is 6.5.', parent.right_child is child)
  Test('Delete method with both children: Parent of 6.5 is 5', child.parent is parent)

  parent = tree.Find(6.5)
  child = tree.Find(5.5)
  Test('Delete method with both children: Left child of 6.5 is 5.5.', parent.left_child is child)
  Test('Delete method with both children: Parent of 5.5 is 6.5.', child.parent is parent)

  parent = tree.Find(6.5)
  child = tree.Find(7)
  Test('Delete method with both children: Right child of 6.5 is 7.', parent.right_child is child)
  Test('Delete method with both children: Parent of 7 is 6.5.', child.parent is parent)

  #
  # Tests for deleting node with both children
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: Delete root node' + bcolors.ENDC
  tree = CreateBasicTree()
  #tree.PrintTree(tree.root, tree.root.height)
  tree.Delete(5)
  #tree.PrintTree(tree.root, tree.root.height)
  n = tree.Find(5.5)

  Test('Delete method with root: 5.5 is new root.', tree.root.key == n.key)
  Test('Delete method with root: height of 5.5 is now 4.', n.height == 4)
  Test('Delete method with root: parent of 5.5 is none.', isinstance(n.parent, NullAVLNode))
  Test('Delete method with root: right child of 5.5 is 6.', n.right_child.key == 6)
  Test('Delete method with root: left child of 5.5 is 3.', n.left_child.key == 3)
  

def TestUpdateHeight():
	#
  # Tests for updating the heights in a tree after a deletion of a node
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: UpdateHeights after node is deleted' + bcolors.ENDC
  tree = CreateBasicTree()
  #tree.PrintTree(tree.root, tree.root.height)
  tree.Delete(6)
  #tree.PrintTree(tree.root, tree.root.height)

  n = tree.Find(6.5)
  Test('Height of node with key 6.5 should be 2.', n.height == 2)

  n = tree.Find(7)
  Test('Height of node with key 7 should be 1.', n.height == 1)

  n = tree.Find(5.5)
  Test('Height of node with key 5.5 should be 0.', n.height == 0)

  n = tree.root
  Test('Height of root node should be 3.', n.height == 3)

  n = tree.Find(4)
  Test('Height of node with key 4 should be 0.', n.height == 0)

def TestBalance():
  
  # Tests for balancing a tree
  
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: Balance left heavy child tree' + bcolors.ENDC
 
  tree = AVLTree()
  tree.Insert(7)
  tree.Insert(5)
  tree.Insert(6)

  #tree.PrintTree(tree.root, tree.root.height)

  parent = tree.Find(6)
  n = tree.Find(7)
  Test('Right child of 6 should be 7', parent.right_child is n)
  Test('7 should have 6 as the parent', n.parent is parent)
  Test('Height of 7 should be 0', n.height == 0)

  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: Balance left heavy child tree' + bcolors.ENDC

  tree = AVLTree()
  tree.Insert(3)
  tree.Insert(5)
  tree.Insert(4)
  #tree.PrintTree(tree.root, tree.root.height)

  root = tree.Find(4)
  n = tree.Find(5)
  Test('Right child of 4 should be 5', root.right_child is n)
  Test('5 should have 4 as the parent', n.parent is root)
  Test('Height of 5 should be 0', n.height == 0)
  Test('Root of tree should be 4', tree.root is root)
  

class bcolors:
  HEADER = '\033[95m' # Purple
  OKBLUE = '\033[94m' # Blue
  OKGREEN = '\033[92m' # Green
  WARNING = '\033[93m' # Yellow
  FAIL = '\033[91m' # Red
  ENDC = '\033[0m' # Black
  BOLD = '\033[1m' # Bold
  UNDERLINE = '\033[4m' # Underline

def Test(testName, bool):
  if bool:
    print bcolors.OKGREEN + testName + " Passed." + bcolors.ENDC
  else:
    print bcolors.FAIL + testName + " Failed." + bcolors.ENDC


def main():

  # TestFind()
  # TestFindSuccessor()
  # TestDelete()
  # TestUpdateHeight()
  # TestInsert()
  # TestLeftRotate()
  # TestRightRotate()
  TestBalance()


if __name__ == '__main__':
  main()