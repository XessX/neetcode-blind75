# 🧠 NeetCode Blind 75 - Problem 09: Longest Consecutive Sequence
# ✅ Goal: Find the length of the longest sequence of consecutive numbers in an unsorted array.
# ✅ Constraint: Must run in O(n) time.

def longestConsecutive(nums):
    num_set = set(nums)      # ✅ Step 1: Use set for O(1) lookups
    longest = 0              # ✅ Step 2: Track the longest sequence found

    for num in num_set:      
        # ✅ Step 3: Only start counting from the start of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            # ✅ Step 4: Count the length of the sequence
            while current + 1 in num_set:
                current += 1
                length += 1

            # ✅ Step 5: Update the maximum length found so far
            longest = max(longest, length)

    return longest

# 🔍 Example usage:
# nums = [100, 4, 200, 1, 3, 2]
# print(longestConsecutive(nums))  # ➜ 4

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)
