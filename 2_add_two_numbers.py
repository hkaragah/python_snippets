from typing import Optional
from xml.dom.minicompat import NodeList # "Optional" means it could be either of the given type or None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
        
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        
        sum = l1.val + l2.val
        
         
        result = ListNode(sum % 10)
        
        if sum >= 10:
            result.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
        else:
            result.next = self.addTwoNumbers(l1.next, l2.next)
        
        return result

        
def main():
    
    # Initialize the dummy parent node
    l1Parent = ListNode() # This helps in easily returning the head of the list later.
    l1 = l1Parent # "l1" is used as a pointer to build the list.
    
    # Iterate through values, 
    # linking each new node to the current node's 'next'
    for val in [2,4,3]:
        l1.next = ListNode(val) # Set the next of the current node to the new node
        l1 = l1.next # Move to the new node
  
    
        
    l2Parent = ListNode()
    l2 = l2Parent
    for val in [5,6,4]:
        l2.next = ListNode(val)
        l2 = l2.next
        
        
    s = Solution()
    node = s.addTwoNumbers(l1Parent.next,l2Parent.next)
    while(node):
        print(node.val)
        node = node.next
    
    
import os
if __name__=="__main__":
    os.system('cls') if os.name == 'nt' else os.system('clear')
    main()
    
        
        
