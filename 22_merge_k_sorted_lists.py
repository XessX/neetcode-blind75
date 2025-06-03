# 🧠 NeetCode Blind 75 - Problem 22: Merge k Sorted Lists
# ✅ Merge k sorted linked lists into one sorted list using a min-heap.
#
# Approach:
#   - Use Python's heapq to always extract the minimum node.
#   - Initialize the heap with the head of each list.
#   - Pop the smallest, add it to result, and push its next (if exists).
#
# Time Complexity: O(N log k), where N = total nodes, k = number of lists
# Space Complexity: O(k) for the heap, plus output list
# -------------------------------------------------------------------

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # For heapq to compare nodes
    def __lt__(self, other):
        return self.val < other.val

def mergeKLists(lists):
    """
    Merges k sorted linked lists into one sorted linked list.
    """
    min_heap = []

    # 1️⃣ Add the head of each list to the heap (if not empty)
    for node in lists:
        if node:
            heapq.heappush(min_heap, node)

    # 2️⃣ Create a dummy node to build the result list
    dummy = ListNode(0)
    curr = dummy

    # 3️⃣ Extract min node, add to result, push its next (if exists)
    while min_heap:
        node = heapq.heappop(min_heap)  # Smallest node
        curr.next = node                # Add to merged list
        curr = curr.next                # Move pointer

        if node.next:                   # If more nodes, push next node
            heapq.heappush(min_heap, node.next)

    # 4️⃣ Return head of the merged list
    return dummy.next

# -------------------------------------------------------------------
# 🔍 Dry Run Example:
# Input lists:
#   [1→4→5, 1→3→4, 2→6]
#
# Heap starts with [1, 1, 2]
# Pop 1 → add to result, push 4 (from first list)
# Pop 1 → add to result, push 3 (from second list)
# Pop 2 → add to result, push 6
# Continue: always pop min, push next from that list if exists
#
# Output: 1→1→2→3→4→4→5→6
# -------------------------------------------------------------------
#
# Complexity:
# - Time: O(N log k)
#      - Each pop/push is log k; do N such operations.
# - Space: O(k) for the heap, O(1) extra for pointers
# -------------------------------------------------------------------
