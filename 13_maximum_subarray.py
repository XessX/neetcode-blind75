# 🧠 NeetCode Blind 75 - Problem 13: Maximum Subarray
# ✅ Goal: Find the contiguous subarray with the largest sum (Kadane's Algorithm)
# ✅ Constraint: Time complexity must be O(n)

from typing import List

def maxSubArray(nums: List[int]) -> int:
    current_sum = nums[0]   # ✅ Start with the first element
    max_sum = nums[0]       # ✅ Track the maximum subarray sum so far

    for i in range(1, len(nums)):
        # ✅ Decide: extend the current subarray or start new from current element
        current_sum = max(current_sum + nums[i], nums[i])

        # ✅ Update the max sum found so far
        max_sum = max(max_sum, current_sum)

    return max_sum

# 🔍 Example usage:
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubArray(nums))  # Output: 6

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)
