# LC148.Sort_List.py
# Topics: Sort, Linked List
# Given the head of a linked list, return the list after sorting it in ascending order.

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        temp = []
        while head and head.next:
            temp.append(head.val)
            head = head.next
            
        temp.append(head.val)
        
        temp.sort()
        
        dummy_head = dummy = ListNode(0)
        
        for i in range(len(temp)):
            dummy.next = ListNode(temp[i])
            dummy = dummy.next
        
        return dummy_head.next