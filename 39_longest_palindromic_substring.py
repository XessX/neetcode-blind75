# 🧠 NeetCode Blind 75 - Problem 39: Longest Palindromic Substring
# ✅ Return the longest palindromic substring in s.

def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        # Odd length palindrome
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
        # Even length palindrome
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
    return res

# ----------------------------------------------------------
# 🔍 Dry Run Example:
# s = "babad"
# Centers: i=0, i=1, ...
# Odd: expand at i=1 ("aba"), even: expand at i=2, etc.
# Output: "bab" or "aba"
# ----------------------------------------------------------
#
# Complexity:
# - Time: O(n^2)
# - Space: O(1)
# ----------------------------------------------------------
