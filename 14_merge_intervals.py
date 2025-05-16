# 🧠 NeetCode Blind 75 - Problem 14: Merge Intervals
# ✅ Goal: Merge all overlapping intervals in a list of intervals
# ✅ Time Complexity: O(n log n) due to sorting

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    # ✅ Step 1: Sort intervals by start time
    intervals.sort()

    res = []  # ✅ This will store the merged intervals

    for start, end in intervals:
        # ✅ If res is not empty AND current start overlaps with last interval in res
        if res and start <= res[-1][1]:
            # ✅ Merge by updating the end of the last interval
            res[-1][1] = max(res[-1][1], end)
        else:
            # ✅ No overlap: just add the interval
            res.append([start, end])

    return res

# 🔍 Example usage:
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# print(merge(intervals))  # Output: [[1,6],[8,10],[15,18]]

# ✅ Time Complexity: O(n log n)
# ✅ Space Complexity: O(n)