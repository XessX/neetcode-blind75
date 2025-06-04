# 🧠 NeetCode Blind 75 - Problem 24: Swap Nodes in Pairs
# ✅ Swap every two adjacent nodes in a linked list, in-place.
#
# Approach:
#   - Use a dummy node before head to handle swaps at the head.
#   - Move through the list in pairs, swapping pointers for every two nodes.
#   - Keep a pointer to the node before the pair (prev), and update links.
#
# Time Complexity: O(n)  (each node visited once)
# Space Complexity: O(1) (in-place)
# ---------------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    """
    Swaps every two adjacent nodes in the linked list and returns the head.
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next         # First node in the pair
        second = prev.next.next   # Second node in the pair

        # Swap the nodes
        prev.next = second
        first.next = second.next
        second.next = first

        # Move prev pointer forward for the next pair
        prev = first

    return dummy.next

# ---------------------------------------------------------------
# 🔍 Dry Run Example:
# Original: 1 → 2 → 3 → 4
#
# Iteration 1: prev at dummy
#   - first = 1, second = 2
#   - After swap: dummy → 2 → 1 → 3 → 4
#
# Iteration 2: prev at 1
#   - first = 3, second = 4
#   - After swap: 1 → 4 → 3
#
# Result: 2 → 1 → 4 → 3
# ---------------------------------------------------------------
#
# Complexity:
# - Time: O(n)  Each node is touched once
# - Space: O(1) Only pointers used
# ---------------------------------------------------------------

