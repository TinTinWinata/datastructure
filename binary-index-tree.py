from typing import List

class BITree:
  def __init__(self, n):
    self.n = n + 1
    self.arr = [0] * (self.n)
    
  def update(self, i: int, v: int):
    i += 1
    while i < self.n:
      self.arr[i] += v
      i += i & (-i) 
    
  def getPrefixSum(self, i: int):
    i += 1
    temp = 0
    while i > 0:
      temp += self.arr[i]
      i -= i & (-i) 
    return temp

def arrayToBITree(arr: List[int]): 
  biTree = BITree(len(arr))
  for i, v in enumerate(arr):
    biTree.update(i, v) 
  return biTree

biTree = arrayToBITree([1,4,7,10])
print(biTree.getPrefixSum(3))

# Note : 
# The we got the parent by looking the last bit of it for example :
# 1. 3 bit is -> 011 
# 2. then we will take only the last 1 bit in 01[1] -> this the last
# 3. then it will be -> 001 (this correspond to 1)
# 4. so the parent of node (i-3) is node (i-1)

# The way we can get the last is by getting calculate using AND operator with the minus value of itself
# For example 3 -> 001 and -3 -> 101 (remember if we search for binary in minus integer it will append 1 in the last of the bits).

# print(3 & -3) # Return 1