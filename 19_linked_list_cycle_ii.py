# 🧠 NeetCode Blind 75 - Problem 19: Linked List Cycle II
# ✅ Return the node where the cycle begins, or None if no cycle.
#
# Approach:
# 1. Use Floyd’s cycle detection (slow & fast pointers) to detect a cycle.
# 2. When slow and fast meet, put one pointer at head.
# 3. Move both pointers one step at a time.
# 4. The point where they meet again is the start of the cycle.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle(head: ListNode) -> ListNode:
    """
    Returns the node where the cycle starts, or None if no cycle.
    """
    slow = head
    fast = head

    # 1️⃣ First, check if a cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # 2️⃣ Cycle detected; now find the entry point
            pointer = head
            while pointer != slow:
                pointer = pointer.next
                slow = slow.next
            return pointer  # Both meet at cycle start

    return None  # No cycle found

# -----------------------------------------------------------------------
# 🔍 Dry Run Example:
# 1 -> 2 -> 3 -> 4 -> 5
#           ^         |
#           |_________|
#
# Suppose cycle starts at node 3.
# Step 1: Detect cycle (slow and fast meet in the loop).
# Step 2: Move one pointer to head. Now move both 1 step at a time.
#         They meet at node 3, the cycle start.
#
# No cycle? Returns None.
# -----------------------------------------------------------------------
#
# Complexity Analysis:
# -------------------
# Time: O(n)
#   - Each node is visited at most twice.
# Space: O(1)
#   - Only pointers are used.
# -----------------------------------------------------------------------
