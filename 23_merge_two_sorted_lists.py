# 🧠 NeetCode Blind 75 - Problem 23: Merge Two Sorted Lists
# ✅ Merge two sorted linked lists and return the new sorted list.
#
# Approach:
#   - Use a dummy node and a pointer to build the new list.
#   - At each step, pick the smaller node and append it.
#   - When one list is done, append the rest of the other list.
#
# Time Complexity: O(n + m), n/m = length of the lists
# Space Complexity: O(1) (no extra data structures, just pointers)
# -------------------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merges two sorted linked lists into one sorted linked list.
    """
    dummy = ListNode(0)  # Dummy node for result list
    curr = dummy         # Pointer to build result

    # 1️⃣ While both lists have nodes, pick the smaller node
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    # 2️⃣ Append the rest of whichever list is not empty
    if list1:
        curr.next = list1
    else:
        curr.next = list2

    # 3️⃣ Return the merged list, skipping the dummy node
    return dummy.next

# -------------------------------------------------------------------
# 🔍 Dry Run Example:
# list1: 1 → 2 → 4
# list2: 1 → 3 → 4
# Step 1: 1 (from list1), 1 (from list2), pick either, say list1.
# Step 2: 1 (from list2), 2 (from list1), pick list2.
# Step 3: 2 (from list1), 3 (from list2), pick list1.
# Step 4: 4 (from list1), 3 (from list2), pick list2.
# Step 5: 4 (from list1), 4 (from list2), pick either.
# Step 6: Append the rest (if any).
# Output: 1 → 1 → 2 → 3 → 4 → 4
# -------------------------------------------------------------------
#
# Complexity:
# - Time: O(n + m) - Each node is visited once
# - Space: O(1)    - Only pointer variables used
# -------------------------------------------------------------------
