# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        placeValL1 = 1
        placeValL2 = 1
        num1 = 0
        num2 = 0
        
        while (l1!=None):
            num1 = num1 + placeValL1*l1.val
            placeValL1 *= 10
            l1 = l1.next
        while (l2!=None):
            num2 = num2 + placeValL2*l2.val
            placeValL2 *= 10
            l2 = l2.next
        
        num1 = str(num1+num2)
        num1 = num1[::-1]
        ans = ListNode(0)
        ptr = ans
        for x in num1:
            ans.next = ListNode(int(x))
            ans = ans.next
        
        return ptr.next