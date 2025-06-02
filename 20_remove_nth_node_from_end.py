# 🧠 NeetCode Blind 75 - Problem 20: Remove Nth Node From End of List
# ✅ Remove the n-th node from the end of a singly linked list in one pass.
#
# Approach:
#   1. Use a dummy node before head (to handle edge cases, like removing the first node).
#   2. Move 'fast' pointer n+1 steps ahead (so there's exactly n nodes between slow and fast).
#   3. Move both 'slow' and 'fast' one step at a time until fast is at the end.
#   4. Now, 'slow' is just before the node to remove. Do slow.next = slow.next.next.
#
# Time Complexity: O(n)    (One pass through the list)
# Space Complexity: O(1)   (No extra data structures)
# ------------------------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    """
    Removes the n-th node from the end of the list and returns the new head.
    """
    # 1️⃣ Dummy node handles edge cases (e.g. deleting first node)
    dummy = ListNode(0, head)
    slow = dummy
    fast = dummy

    # 2️⃣ Move 'fast' pointer n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # 3️⃣ Move both pointers until 'fast' is at the end
    while fast:
        slow = slow.next
        fast = fast.next

    # 4️⃣ 'slow.next' is the node to remove; skip it
    slow.next = slow.next.next

    # 5️⃣ Return the real head (could have changed if first node was deleted)
    return dummy.next

# ------------------------------------------------------------------------
# 🔍 Step-by-step Dry Run:
# List: 1 -> 2 -> 3 -> 4 -> 5, n = 2
# Goal: Remove 4th node (value 4) from the end.
#
# 1. dummy -> 1 -> 2 -> 3 -> 4 -> 5
#    slow   ^
#    fast   ^
#
# Move fast 2+1 = 3 steps ahead:
#    fast at node 3
#
# Move both slow & fast until fast reaches the end:
#    slow at node 3, fast at end (None)
#
# slow.next = 4 (to be removed)
# Do slow.next = slow.next.next
# List is now: 1 -> 2 -> 3 -> 5
# ------------------------------------------------------------------------
#
# Complexity:
# - Time: O(n)   Each node visited once
# - Space: O(1)  No extra structures
# ------------------------------------------------------------------------
