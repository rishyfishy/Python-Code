from collections import deque

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    # level-by-level pretty-printer
    nodes = deque([self])
    answer = ''
    while len(nodes):
      node = nodes.popleft()
      if not node:
        continue
      answer += str(node.value)
      nodes.append(node.left)
      nodes.append(node.right)
    return answer

def createBalancedBST(lst:list)->Node:
    if len(lst)==0:
        return None
    elif len(lst)==1:
        return Node(lst[0])
    rootIndex = (len(lst)-1)//2
    return Node(lst[rootIndex],createBalancedBST(lst[:rootIndex]),createBalancedBST(lst[rootIndex+1:]))


    
        