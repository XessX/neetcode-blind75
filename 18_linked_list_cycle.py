# 🧠 NeetCode Blind 75 - Problem 18: Linked List Cycle
# ✅ Detect if a singly linked list has a cycle (returns True or False)
#
# Approach: Floyd's Tortoise and Hare (Two Pointer)
# - Use two pointers (slow and fast).
# - Move slow by 1 step, fast by 2 steps.
# - If fast and slow meet, there is a cycle.
# - If fast reaches the end (None), no cycle.
#
# Time Complexity: O(n)     (Each node visited at most twice)
# Space Complexity: O(1)    (No extra data structures)
# -------------------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    """
    Detects if the linked list has a cycle using two pointers.

    Args:
        head (ListNode): Head node of the linked list.

    Returns:
        bool: True if cycle exists, False otherwise.
    """
    slow = head     # Moves 1 step each time
    fast = head     # Moves 2 steps each time

    # Only loop if fast and fast.next exist (prevents crash at end of list)
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True  # Found a cycle!

    return False         # No cycle found

# -------------------------------------------------------------------
# 🔍 Dry Run Example:
# Example 1: Cycle exists
# 1 -> 2 -> 3 -> 4
#      ^         |
#      |_________|
#
# slow and fast will eventually meet at node 3 or 4 and return True.
#
# Example 2: No cycle
# 1 -> 2 -> 3 -> None
#
# fast pointer will reach None, loop ends, return False.
# -------------------------------------------------------------------
#
# Complexity Analysis:
# -------------------
# Time: O(n)
#   - Each pointer travels at most around the length of the list.
# Space: O(1)
#   - Only a couple of pointers, no extra space.
# -------------------------------------------------------------------
