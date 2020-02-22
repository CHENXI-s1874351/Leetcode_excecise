# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 这段代码可以大大简化，虽然这样写也可以过
        root = ListNode(0)
        pre = root
        flag = False
        while l1 and l2:
            if flag:
                add = l1.val + l2.val + 1
            else:
                add = l1.val + l2.val
            if add < 10:
                node = ListNode(add)
                flag = False
            else:
                node = ListNode(add - 10)
                flag = True
            pre.next = node
            pre = pre.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            while l1:
                if flag:
                    add = l1.val + 1
                else:
                    add = l1.val
                if add < 10:
                    node = ListNode(add)
                    flag = False
                else:
                    node = ListNode(add - 10)
                    flag = True
                pre.next = node
                pre = pre.next  
                l1 = l1.next        
        
        if l2:
            while l2:
                if flag:
                    add = l2.val + 1
                else:
                    add = l2.val
                if add < 10:
                    node = ListNode(add)
                    flag = False
                else:
                    node = ListNode(add - 10)
                    flag = True
                pre.next = node
                pre = pre.next
                l2 = l2.next
        
        if flag:
            pre.next = ListNode(1)
        
        return root.next




