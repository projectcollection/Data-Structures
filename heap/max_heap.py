import math
class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._sift_down(0)
    self._bubble_up(len(self.storage) - 1)
    self._bubble_up(len(self.storage) - 2)
    
  def delete(self):
    deleted = self.storage.pop(0)    
    if len(self.storage) > 0:
      self.insert(self.storage.pop())
    return deleted

  def get_max(self):
    return self.storage[0] if len(self.storage) > 0 else None

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if(index < 1):
      return
    if math.floor((index-1)/2) >= 0:
      if self.storage[index] > self.storage[math.floor((index-1)/2)]:
        temp = self.storage[index]
        self.storage[index] = self.storage[math.floor((index-1)/2)]
        self.storage[math.floor((index-1)/2)] = temp
        self._bubble_up(math.floor((index-1)/2))
      else:
        return
    else:
      return

  def _sift_down(self, index):
    l = 2*index + 1
    r = 2*index + 2
    if l < len(self.storage) and r < len(self.storage):
      greater_index = l if self.storage[l] > self.storage[r] else r
      if self.storage[index] < self.storage[greater_index]:
        temp = self.storage[index]
        self.storage[index] = self.storage[greater_index]
        self.storage[greater_index] = temp
        self._sift_down(l if greater_index == l else r)
      else:
        return
    else:
      return