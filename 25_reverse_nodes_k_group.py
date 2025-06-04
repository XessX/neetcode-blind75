# 🧠 NeetCode Blind 75 - Problem 25: Reverse Nodes in k-Group
# ✅ Reverse nodes in linked list in groups of k.
#
# Approach:
#   - Use a dummy node before head for easy edge handling.
#   - For each group of k nodes, reverse them in-place.
#   - Connect previous group's tail to new reversed head.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    """
    Reverses nodes in k-sized groups and returns new head.
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while True:
        # Check if there are k nodes to reverse
        node = prev
        for i in range(k):
            node = node.next
            if not node:
                return dummy.next  # Not enough nodes, done

        # Reverse k nodes
        curr = prev.next
        nex = curr.next
        for i in range(k - 1):
            curr.next = nex.next
            nex.next = prev.next
            prev.next = nex
            nex = curr.next

        # Move prev to end of this chunk
        prev = curr

# -------------------------------------------------------------
# 🔍 Dry Run Example:
# List: 1 → 2 → 3 → 4 → 5, k=3
# Step 1: Reverse 1→2→3 → 3→2→1
#         List: 3→2→1→4→5
# Step 2: Remaining 4→5 (less than k), leave as is
# -------------------------------------------------------------
#
# Complexity:
# - Time: O(n) Each node is visited once
# - Space: O(1) No extra space, just pointers
# -------------------------------------------------------------
