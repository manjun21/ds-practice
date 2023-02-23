#https://leetcode.com/problems/add-two-numbers-ii/
class ListNode:
    def __init__(self,val,next=None) -> None:
        self.value = val
        self.next = next

def reverse_list(l1: ListNode):
    curr = l1
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    stack_l1 = []
    stack_l2 = []
    tempnode = ListNode(0)
    pointer = tempnode
    while l1:
        stack_l1.append(l1.value)
        l1= l1.next
    
    while l2:
        stack_l2.append(l2.value)
        l2= l2.next

    #print(stack_l1)
    #print(stack_l2)
    while stack_l1 or stack_l2 or carry:
        l1val = stack_l1.pop() if stack_l1 else 0
        l2val = stack_l2.pop() if stack_l2 else 0

        sum_val = l1val + l2val + carry
        rem    = sum_val % 10
        carry   = sum_val //10
        newnode = ListNode(rem)
        pointer.next = newnode
        pointer = pointer.next
        #print(stack_l1)
        stack_l1 = stack_l1 if stack_l1!=None and len(stack_l1) != 0 else None
        stack_l2 = stack_l2 if stack_l2!=None and len(stack_l2) != 0 else None

    return tempnode.next


l = ListNode(7)
l1 = ListNode(2)
ll1 = ListNode(4)
ll2 = ListNode(3)

l.next = l1
l1.next = ll1
ll1.next = ll2

l2 = ListNode(5)
ll11 = ListNode(6)
ll22 = ListNode(4)

l2.next = ll11
ll11.next = ll22
print(reverse_list(addTwoNumbers(l1,l2)))

