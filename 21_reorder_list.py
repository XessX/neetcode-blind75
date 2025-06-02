# 🧠 NeetCode Blind 75 - Problem 21: Reorder List
# ✅ Reorder a linked list as L0→Ln→L1→Ln-1→L2→Ln-2...
#
# Steps:
#   1. Find the middle using slow & fast pointers.
#   2. Reverse the second half of the list.
#   3. Merge first and reversed second half alternately.
#
# Time Complexity: O(n)    (3 passes: find middle, reverse, merge)
# Space Complexity: O(1)   (In-place, only pointer variables)
# -------------------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: ListNode) -> None:
    """
    Reorders the linked list in-place as per the problem statement.
    Returns nothing (modifies the list).
    """
    if not head or not head.next:
        return

    # 1️⃣ Find the middle (slow/fast pointers)
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2️⃣ Reverse the second half
    prev = None
    curr = slow.next
    slow.next = None   # Split list into two halves
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    second = prev  # Head of reversed second half

    # 3️⃣ Merge both halves
    first = head
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2

# -------------------------------------------------------------------
# 🔍 Dry Run Example:
# List: 1 → 2 → 3 → 4 → 5
# 1. Find middle: slow at 3
#    List is split into: 1→2→3 and 4→5
# 2. Reverse second half: 5→4
# 3. Merge: 1→5→2→4→3
# -------------------------------------------------------------------
#
# Complexity:
# - Time: O(n)   Three O(n) passes over the list
# - Space: O(1)  Only pointers used
# -------------------------------------------------------------------
