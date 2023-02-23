#https://towardsdatascience.com/leetcode-problem-2-python-1c59efdf3367
#https://leetcode.com/problems/add-two-numbers/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode(0)
    pointer = result
    carry = 0
    sum =0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        sum = val1 + val2 + carry
        num = sum % 10
        carry = sum // 10
        
        pointer.next = ListNode(num)
        pointer = pointer.next

        l1 = l1.next if l1 else None
        l2= l2.next if l2 else None
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
print(addTwoNumbers(l1,l2))