# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

    
class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self,data):
        
        cur = self.head
        while (cur.next!=None):
            cur=cur.next
        cur.next = Node(data)
    
    def length(self):
        total = 0
        cur = self.head
        while (cur.next !=None):
            total+=1
            cur=cur.next

        return total
    
    def display(self):
        elems = []
        cur=self.head
        while(cur.next!=None):
            cur=cur.next
            elems.append(cur.data)
            
        print (elems)
    
    def get(self, index):

        if (index>=self.length() or index<0):
            print ("ERROR, 'get' index out of range")
            return None
        curIndex = 0
        cur = self.head.next
        while (curIndex != index):
            curIndex+=1
            cur=cur.next
        return cur.data

    def erase(self, index):

        if (index>=self.length() or index<0):
            print ("ERROR, 'erase' index out of range")
            return None
        last = self.head
        cur = last.next
        nextIndex = 0
        while (nextIndex != index):
            last = cur
            cur=cur.next
            nextIndex+=1
        last.next = cur.next

    def eraseInstance(self, data):
        last = self.head
        cur = last.next
        nextIndex = 0
        while (cur.data != data):
            last = cur
            cur=cur.next
            nextIndex += 1
        last.next = cur.next

           


# # Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, x):
#     self.val = x
#     self.next = None

# class Solution:
#   def addTwoNumbers(self, l1, l2, c = 0):
#     # Fill this in.
#     sum = 0
#     x=1
#     l = l1
#     while (l!=None):
#         sum+=x*l.val
#         x*=10
#         l=l.next
#     l = l2
#     while (l!=None):
#         sum+=x*l.val
#         x*=10
#         l=l.next 


# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# result = Solution().addTwoNumbers(l1, l2)
# while result:
#   print result.val,
#   result = 
