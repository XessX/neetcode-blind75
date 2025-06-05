# 🧠 NeetCode Blind 75 - Problem 12: Container With Most Water
# ✅ Goal: Find two lines that form a container which holds the most water.
# ✅ Constraints: Must run in O(n) time using the two-pointer approach

from typing import List

def maxArea(height: List[int]) -> int:
    left = 0                     # ✅ Pointer starting from the left end
    right = len(height) - 1     # ✅ Pointer starting from the right end
    max_water = 0               # ✅ Track the maximum area (water) found

    while left < right:
        width = right - left                              # ✅ Distance between the lines
        current_height = min(height[left], height[right]) # ✅ Container height is the shorter of two lines
        current_area = current_height * width             # ✅ Area = height * width
        max_water = max(max_water, current_area)          # ✅ Update max water if needed

        if height[left] < height[right]:  # ✅ Move pointer from the shorter line inward
            left += 1
        else:
            right -= 1

    return max_water

# 🔍 Example usage:
# height = [1,8,6,2,5,4,8,3,7]
# print(maxArea(height))  # Output: 49

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)
