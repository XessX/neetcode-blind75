# 🧠 NeetCode Blind 75 - Problem 21: Reorder List
# ✅ Reorder a singly linked list so that the nodes are arranged as:
#    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
#
# Steps:
# 1. Find the middle using slow & fast pointers.
# 2. Reverse the second half of the list.
# 3. Merge the first and reversed second half alternately.
#
# Time Complexity: O(n)    (3 passes: find middle, reverse, merge)
# Space Complexity: O(1)   (In-place, only pointer variables)
# ---------------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: ListNode) -> None:
    """
    Reorders the linked list in-place as L0→Ln→L1→Ln-1→L2→Ln-2...
    Does not return anything, modifies the list in place.
    """
    if not head or not head.next:
        return  # 0 or 1 node, nothing to reorder

    # 1️⃣ Find the middle (slow/fast pointers)
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # After the loop, slow is at the middle node

    # 2️⃣ Reverse the second half
    prev = None
    curr = slow.next
    slow.next = None  # Cut the list into two halves
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    # prev is now the head of reversed second half

    # 3️⃣ Merge the two halves alternately
    first, second = head, prev
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2
    # Done! The list is now reordered in place

# ---------------------------------------------------------------
# 🔍 Example Dry Run:
# List: 1 → 2 → 3 → 4 → 5
# Step 1: Find middle (slow at 3), split into 1→2→3 and 4→5
# Step 2: Reverse second half: 5→4
# Step 3: Merge:
#   1 → 5 → 2 → 4 → 3
# ---------------------------------------------------------------
#
# Complexity:
# - Time: O(n)   Each step (find middle, reverse, merge) is O(n)
# - Space: O(1)  Only pointers used, no extra lists
# ---------------------------------------------------------------
