# 🧠 NeetCode Blind 75 - Problem 41: Longest Substring Without Repeating Characters
# ✅ Return the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):
    char_index = {}  # Dictionary to store last seen index of chars
    left = 0         # Left edge of the window
    res = 0          # Result (max length found)

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            # Move left pointer just after the last occurrence
            left = char_index[s[right]] + 1
        char_index[s[right]] = right
        res = max(res, right - left + 1)
    return res

# ----------------------------------------------------------
# 🔍 Dry Run Example:
# s = "abcabcbb"
# As window slides, left pointer moves after repeats, res updated to max.
# Output: 3 ("abc")
# ----------------------------------------------------------
#
# Complexity:
# - Time: O(n)
# - Space: O(min(n, m)) (n = length of string, m = size of alphabet)
# ----------------------------------------------------------
