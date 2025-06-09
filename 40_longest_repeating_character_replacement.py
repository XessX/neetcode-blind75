# 🧠 NeetCode Blind 75 - Problem 40: Longest Repeating Character Replacement
# ✅ Sliding window, replace up to k chars to make max-length same-letter substring.

def characterReplacement(s, k):
    count = {}      # Dictionary to count chars in window
    left = 0        # Left pointer of window
    max_count = 0   # Max freq of a single char in window
    res = 0         # Result (max window size found)

    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)
        max_count = max(max_count, count[s[right]])
        # If more than k replacements needed, move left pointer
        if (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res

# ----------------------------------------------------------
# 🔍 Dry Run Example:
# s = "AABABBA", k = 1
# Window slides, updating char counts and max_count, res updated if longer.
# Output: 4 ("AABA" or "ABBA")
# ----------------------------------------------------------
#
# Complexity:
# - Time: O(n)
# - Space: O(1) (alphabet size fixed)
# ----------------------------------------------------------
