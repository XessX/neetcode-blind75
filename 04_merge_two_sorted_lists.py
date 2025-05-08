# Problem: Merge Two Sorted Lists
# You are given the heads of two sorted linked lists.
# Merge them into a new sorted linked list and return the head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Step 1: Create a dummy node to simplify the logic
    dummy = ListNode()
    tail = dummy  # Step 2: Tail keeps track of the end of the merged list

    # Step 3: Traverse both lists until one is exhausted
    while list1 and list2:
        # Step 4: Compare values and pick the smaller one
        if list1.val < list2.val:
            tail.next = list1        # Step 5: Attach list1 node
            list1 = list1.next       # Step 6: Move list1 forward
        else:
            tail.next = list2        # Step 7: Attach list2 node
            list2 = list2.next       # Step 8: Move list2 forward
        tail = tail.next             # Step 9: Advance the tail pointer

    # Step 10: Attach the remaining nodes
    if list1:
        tail.next = list1
    else:
        tail.next = list2

    # Step 11: Return the head of the merged list (skipping dummy node)
    return dummy.next
