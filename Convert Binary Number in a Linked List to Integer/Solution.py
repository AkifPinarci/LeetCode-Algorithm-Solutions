# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        increment=1
        value=0
        nlist=[]
        while(head!=None):
            nlist.append(head.val)
            head=head.next
        for i in reversed(nlist):
            value+=i*increment
            increment*=2
            
        return value
