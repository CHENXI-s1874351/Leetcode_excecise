# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:


    # This function has two functions:
    # first it cuts off the list from head to the node that is length away from head;
    # then it returns the node which is length+1 away from head.
    def cut(self, head, length):

    	while length > 1:
    		if head:
    			head = head.next
    			length -= 1
    		else:
    			return None

    	if head == None:
    		return None

    	nextNode = head.next
    	head.next = None
    	return nextNode

    # Merge two ordered lists into one ordered list
    def merge(self, head1, head2):

    	dummyhead = ListNode(0)
    	res = dummyhead

    	while head1 != None and head2 != None:

    		if head1.val >= head2.val:
    			res.next = head2
    			res = head2
    			head2 = head2.next
    		else:
    			res.next = head1
    			res = head1
    			head1 = head1.next

    	if head1 == None:
    		res.next = head2
    	else:
    		res.next = head1

    	return dummyhead.next


    def sortList(self, head: ListNode) -> ListNode:

    	if head == None:
    		return None

    	interval = 1
    	list_length = 1
    	p = head
    	while p.next != None:
    		p = p.next
    		list_length += 1

    	dummyhead = ListNode(0)
    	dummyhead.next = head

    	while interval < list_length:

    		res = dummyhead

    		while res.next != None:

    			head1 = res.next
    			head2 = self.cut(head1, interval)
    			head3 = self.cut(head2, interval)

    			new_head = self.merge(head1, head2)
    			res.next = new_head

    			tail = new_head
    			while tail.next != None:
    				tail = tail.next
    			tail.next = head3

    			res = tail
    		interval *= 2

    	return dummyhead.next













        