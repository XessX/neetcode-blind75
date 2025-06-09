# 🧠 NeetCode Blind 75 - Problem 38: Trapping Rain Water
# ✅ Compute total water trapped between elevation bars.

def trap(height):
    left, right = 0, len(height) - 1  # Two pointers
    left_max, right_max = 0, 0        # Max height to the left/right
    total = 0                         # Total water trapped

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                total += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                total += right_max - height[right]
            right -= 1

    return total

# ----------------------------------------------------------
# 🔍 Dry Run Example:
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Water is trapped in valleys; sum up at each step.
# Output: 6
# ----------------------------------------------------------
#
# Complexity:
# - Time: O(n)
# - Space: O(1)
# ----------------------------------------------------------
