class Heap:
  def __init__(self, comparator = lambda x, y: x > y):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    self.storage.append(value)
    storage_len = len(self.storage)
    self._sift_down(0)
    self._bubble_up(storage_len - 1)
    self._bubble_up(storage_len - 2)

  def delete(self):
    storage = self.storage
    deleted = storage.pop(0)    
    if len(storage) > 0:
      self.insert(storage.pop())
    return deleted

  def get_priority(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent_index = (index-1)//2
    storage = self.storage
    if parent_index >= 0 and index > 0:
      if self.comparator(storage[index], storage[parent_index]):
        storage[index], storage[parent_index] =  storage[parent_index], storage[index]
        self._bubble_up(parent_index)
    else:
      return

  def _sift_down(self, index):
    l = 2*index + 1
    r = l + 1
    storage = self.storage
    if r < len(self.storage):
      greater_index = l if self.comparator(storage[l], storage[r]) else r
      if self.comparator(storage[greater_index], storage[index]):
        storage[index], storage[greater_index] = storage[greater_index], storage[index] 
        self._sift_down(greater_index)
    else:
      return
