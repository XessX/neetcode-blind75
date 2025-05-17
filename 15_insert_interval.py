# 🧠 NeetCode Blind 75 - Problem 15: Insert Interval
# ✅ Goal: Insert a new interval and merge overlapping ones in sorted order
# ✅ Time Complexity: O(n)

from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    i = 0
    n = len(intervals)
    res = []

    # 1️⃣ Add intervals that end before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    # 2️⃣ Merge intervals that overlap with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    # 3️⃣ Add the merged interval
    res.append(newInterval)

    # 4️⃣ Add remaining intervals
    while i < n:
        res.append(intervals[i])
        i += 1

    return res

# 🔍 Example usage:
# intervals = [[1,3], [6,9]]
# newInterval = [2,5]
# print(insert(intervals, newInterval))  # Output: [[1,5],[6,9]]

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)
