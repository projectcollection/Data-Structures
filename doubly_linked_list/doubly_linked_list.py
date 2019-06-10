"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    self.head.insert_before(value)   
    self.head = self.head.prev
    self.length = self.length + 1

  def remove_from_head(self):
    if self.head:
      new_node = None
      if self.head.next:
        new_node = self.head.next
      self.head.delete()
      self.head = new_node

    self.length = self.length - 1

  def add_to_tail(self, value):
    self.tail.insert_after(value)  
    self.tail = self.tail.next
    self.length = self.length + 1

  def remove_from_tail(self):
    if self.tail:
      new_tail = self.tail.prev
      self.tail.delete()
      self.tail = new_tail

    self.length = self.length - 1

  def move_to_front(self, node):
    if self.tail == node:
      self.remove_from_tail()
    else:
      self.length = self.length - 1
    to_move = node.value
    self.add_to_head(to_move)
    node.delete()

  def move_to_end(self, node):
    if self.head == node:
      self.remove_from_head()
    else:
      self.length = self.length - 1
    to_move = node.value
    node.delete()
    self.add_to_tail(to_move)

  def delete(self, node):
    if self.head == node:
      self.remove_from_head()
    elif self.tail == node:
      self.remove_from_tail()
    else:
      node.delete()

    print('IN DELETE', self.head, self.tail)
    
  def get_max(self):
    curr_max = self.head.value
    curr_node = self.head
    while curr_node:
      if curr_node.value > curr_max:
        curr_max = curr_node.value
      curr_node = curr_node.next
    
    return curr_max
