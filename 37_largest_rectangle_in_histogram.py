# 🧠 NeetCode Blind 75 - Problem 37: Largest Rectangle in Histogram
# ✅ Return area of largest rectangle in histogram bars.

def largestRectangleArea(heights):
    stack = []         # Store indices of bars
    max_area = 0
    heights.append(0)  # Add a dummy bar to clear the stack at the end

    for i, h in enumerate(heights):
        # If the current bar is lower than the stack top, calculate area
        while stack and h < heights[stack[-1]]:
            top = stack.pop()
            height = heights[top]
            # If stack is empty, width = i (from beginning)
            width = i if not stack else i - stack[-1] - 1
            area = height * width
            max_area = max(max_area, area)
        stack.append(i)

    heights.pop()  # Remove the dummy bar
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
