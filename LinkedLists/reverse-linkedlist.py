# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        p=head
        j=p
        while head:
            res.append(head.val)
            head=head.next
        res.reverse()
        for i in res:
            p.val=i
            p=p.next
        return j