# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        quick = dummyHead
        slow = dummyHead
        for i in range(n):
            quick = quick.next
        while quick.next:
            quick = quick.next
            slow = slow.next
        slow.next = slow.next.next
        return dummyHead.next