def get_num(head):
    slow = fast = head
    
    
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if slow == fast:
            # print('slow == fast')
            # print(slow.value)
            break
    else:
        return None
    
    while head != slow:
        head = head.next_node
        slow = slow.next_node
        
    return slow

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node 
        # // reference to next node
        
node1 = Node(1)

node2 = Node(2)
node1.next_node = node2

node3 = Node(3)
node2.next_node = node3


node4 = Node(4)
node3.next_node = node4

node4.next_node = node2


    
print(get_num(node1).value)

# names = [''.join('node', i) for i in range(10000)]
# namebwio = 'something'

cur_node = Node(0)
for i in range(100000):
    next_node = Node(i+1)
    cur_node.next_node = next_node
    cur_node = next_node

    
i = 0
initial_node = Node(1)
cur_node = initial_node

while i < (100000):
    ...
    i += 1
    next_node = Node(i)
    cur_node.next_node = next_node
    cur_node = next_node

print(get_num(initial_node).value)