import sys 

sys.path.append('../doubly_linked_list')
from doubly_linked_list import ListNode

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.left and value < self.value:
      self.left.insert(value)
    elif self.right and value > self.value:
      self.right.insert(value)
    else:
      new_tree = BinarySearchTree(value)
      if value > self.value:
        self.right = new_tree
      else:
        self.left = new_tree

  def contains(self, target):
    if self.value != target:
      in_left = self.left.contains(target) if self.left else False
      in_right = self.right.contains(target) if self.right else False
      if in_left or in_right:
        return True
      else:
        return False
    else:
      return True

  def get_max(self):
    if self.right:
      return self.right.get_max()
    else:
      return self.value

  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)
    else:
      cb(self.value)