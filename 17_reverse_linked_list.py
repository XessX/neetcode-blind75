# 🧠 NeetCode Blind 75 - Problem 17: Reverse Linked List
# ✅ Reverse a singly linked list (in-place, iteratively)
#
# Approach:
#   - Use two pointers, prev and curr, to reverse the list node by node.
#   - At each step, reverse curr.next to point to prev.
#   - Move both pointers forward.
#
# Time Complexity: O(n)   (Each node is visited once)
# Space Complexity: O(1)  (No extra data structures; reversal is in-place)
# ------------------------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    """
    Reverses the linked list and returns the new head.

    Args:
        head (ListNode): The head node of the linked list.

    Returns:
        ListNode: The head node of the reversed list.
    """
    prev = None        # At start, nothing comes before head
    curr = head        # Begin at the head node

    while curr:
        next_temp = curr.next   # Store next node before changing
        curr.next = prev        # Reverse pointer
        prev = curr             # Move prev forward
        curr = next_temp        # Move curr forward

    # prev now points to the new head (old tail)
    return prev

# ------------------------------------------------------------------------
# 🔍 Example Usage / Dry Run:
#
# Let's say the original list is: 1 -> 2 -> 3 -> None
#
# Step-by-step:
# prev = None, curr = 1
#   Save next_temp = 2
#   1.next = prev (None), so 1 -> None
#   Move prev to 1, curr to 2
#
# prev = 1, curr = 2
#   Save next_temp = 3
#   2.next = prev (1), so 2 -> 1
#   Move prev to 2, curr to 3
#
# prev = 2, curr = 3
#   Save next_temp = None
#   3.next = prev (2), so 3 -> 2
#   Move prev to 3, curr to None
#
# Final: prev is 3, list is 3 -> 2 -> 1 -> None
#
# To test:
# def print_list(node):
#     while node:
#         print(node.val, end=" -> ")
#         node = node.next
#     print("None")
#
# head = ListNode(1, ListNode(2, ListNode(3)))
# reversed_head = reverseList(head)
# print_list(reversed_head)  # Output: 3 -> 2 -> 1 -> None
# ------------------------------------------------------------------------
#
# Complexity Analysis:
# --------------------
# Time Complexity: O(n)
#   - Each node is visited and its .next pointer is reversed once
#
# Space Complexity: O(1)
#   - No extra arrays/lists; only pointers used
#
# This is the optimal solution for reversing a singly linked list!
# ------------------------------------------------------------------------
