# 🧠 NeetCode Blind 75 - Problem 11: 3Sum
# ✅ Goal: Find all unique triplets [a, b, c] such that a + b + c == 0

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()  # ✅ Step 1: Sort array to use two-pointer efficiently
    res = []     # ✅ Step 2: Store result triplets

    for i in range(len(nums)):
        # ✅ Step 3: Skip duplicate values for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1            # ✅ left starts just after i to avoid reuse
        right = len(nums) - 1   # ✅ right starts at the end

        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]

            if three_sum == 0:
                res.append([nums[i], nums[left], nums[right]])

                # ✅ Move both pointers and skip duplicates
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif three_sum < 0:
                left += 1  # Too small → need a bigger number
            else:
                right -= 1  # Too big → need a smaller number

    return res

# 🔍 Example:
# nums = [-1, 0, 1, 2, -1, -4]
# print(threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]

# ✅ Time Complexity: O(n^2)
# ✅ Space Complexity: O(1) extra (output list excluded)
