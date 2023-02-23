#https://www.educative.io/courses/grokking-coding-interview-patterns-python/mE6KynXWR8O
#https://leetcode.com/problems/reverse-nodes-in-k-group/

from __future__ import print_function


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# reverse will reverse the k number of nodes in the linked list
def reverse(head, k):
    previous, current, next = None, head, None
    index = 0
    while current and index < k:
        # temporarily store the next node
        next = current.next
        # reverse the current node
        current.next = previous
        # before we move to the next node, point previous to the
        # current node
        previous = current
        # move on the next node 
        current = next  
        index += 1
    return previous, current, next


# find_length will find the total length of the linked list
def find_length(start):
    current = start
    count = 0
    # count the number of nodes from start to the end of the list
    while current:
        current = current.next
        count += 1
    return count


# reverse_linked_list is our challenge function that will reverse
# the group of k nodes in the linked list
def reverse_linked_list(head, k):
    if k <= 1 or not head:
        return head
    i, count = 0, 0
    current, previous = head, None
    total_length = find_length(head)
    max_possible_grp = int(total_length/k)
    while True:
        i += 1
        next = None  # will be used to temporarily store the next node
        last_node_of_previous_part = previous
        last_node_of_current_part = current
        previous, current, next = reverse(last_node_of_current_part, k)
        #head = current
        count = count +1
        print("\n\n", i, ". Part of the list reversed is: ", sep="", end=" ")
        #print_list_with_forward_arrow(previous)
        #print("\n\t Pointers after reversing k =", k, "elements:")
        #print("\t current:", current.data if current else "null")
        #print("\t next:", next.data if next else "null")
        #print("\t previous:", previous.data if previous else "null")
        #print("Current state of list:", end=" ")
        #print_list_with_forward_arrow(head)
         # connect with the previous part
        if last_node_of_previous_part:
            last_node_of_previous_part.next = previous
        else:
            head = previous

        # connect with the next part
        last_node_of_current_part.next = current
        print()
        if current is None or count >= max_possible_grp:
            break
        previous = last_node_of_current_part
    return head


def main():
    #input_list = [1, 2, 3, 4, 5, 6, 7, 8]
    input_linked_list = ListNode(1)
    ll2 = ListNode(2)
    ll3 = ListNode(3)
    ll4 = ListNode(4)
    ll5 = ListNode(5)
    ll6 = ListNode(6)
    ll7 = ListNode(7)
    ll8 = ListNode(8)
    input_linked_list.next = ll2
    ll2.next = ll3
    ll3.next = ll4
    ll4.next = ll5
    ll5.next = ll6
    ll6.next = ll7
    ll7.next = ll8
    ll8.next = None


    #print("The original linked list: ", end='')
    #print_list_with_forward_arrow(input_linked_list.head)
    result = reverse_linked_list(input_linked_list, 3)
    #print("\nReversed linked list, with k = ", 3, ": ", sep='', end='')
    #print_list_with_forward_arrow(result)
    print('---')
    print(result)


if __name__ == '__main__':
    main()

            
    
