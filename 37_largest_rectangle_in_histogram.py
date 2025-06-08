# 🧠 NeetCode Blind 75 - Problem 37: Largest Rectangle in Histogram
# ✅ Return area of largest rectangle in histogram bars.

def largestRectangleArea(heights):
    stack = []        # Stack to store indices
    max_area = 0      # Maximum area found
    heights.append(0) # Sentinel bar to pop all bars at the end

    for i, h in enumerate(heights):
        # Keep popping while the current bar is shorter than stack top
        while stack and h < heights[stack[-1]]:
            top_idx = stack.pop()
            height = heights[top_idx]
            # If stack is empty, rectangle extends to beginning
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    heights.pop()  # Remove the sentinel
    return max_area

# ----------------------------------------------------------
# 🔍 Dry Run Example:
# heights = [2,1,5,6,2,3]
# At index 2 (5), stack: [1,2]; at index 4 (2), pop 6 and 5, calculate area.
# Largest rectangle is from [5,6], area = 2*5 = 10.
# ----------------------------------------------------------
#
# Complexity:
# - Time: O(n)
# - Space: O(n)
# ----------------------------------------------------------
