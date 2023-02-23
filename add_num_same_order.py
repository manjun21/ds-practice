from unittest import result


class ListNode:

    def __init__(self,val=0,next=None) :
        self.val = val
        self.next = next


def reverse_list(l1:ListNode):
    curr = l1
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode(0)
    pointer = result

    stack_l1 = []
    stack_l2 = []

    while l1:
        stack_l1.append(l1)
        l1 = l1.next

    while l2:
        stack_l2.append(l2)
        l2 = l2.next

    sum = 0
    carry = 0
    while stack_l1 or stack_l2 or carry:
        l1val = stack_l1.pop() if stack_l1 else 0
        l2val = stack_l2.pop() if stack_l2 else 0

        sum = l1val + l2val + carry
        num = sum %10
        carry = num //10

        pointer.next = ListNode(num)
        pointer = pointer.next

        stack_l1 = stack_l1 if len(stack_l1)>0 else None
        stack_l2 = stack_l2 if len(stack_l2)>0 else None

    return result.next



l1 = ListNode(2)
ll1 = ListNode(4)
ll2 = ListNode(4)

l1.next = ll1
ll1.next = ll2

l2 = ListNode(5)
ll11 = ListNode(6)
ll22 = ListNode(5)

l2.next = ll11
ll11.next = ll22
print(reverse_list(addTwoNumbers(l1,l2)))