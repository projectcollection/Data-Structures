import math
class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)

    for i in range(1,len(self.storage),-1):
      print(i)
      
    
  def delete(self):
    pass

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if self.storage[index] > self.storage[math.floor((index-1)/2)]:
      temp = self.storage[index]
      self.storage[index] = self.storage[math.floor((index-1)/2)]
      self.storage[math.floor((index-1)/2)] = temp

  def _sift_down(self, index):
    l = 2*index + 1
    r = 2*index + 2
    greater_index = l if self.storage[l] > self.storage[r] else r
    if self.storage[index] < self.storage[greater_index]:
      temp = self.storage[index]
      self.storage[index] = self.storage[greater_index]
      self.storage[greater_index] = temp

