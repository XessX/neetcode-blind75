# 🧠 NeetCode Blind 75 - Problem 42: Minimum Window Substring
# ✅ Return the smallest substring of s containing all characters of t.

def minWindow(s, t):
    from collections import Counter

    if not t or not s:
        return ""
    
    count_t = Counter(t)
    window = {}
    have, need = 0, len(count_t)
    res, res_len = [-1, -1], float('inf')
    left = 0

    for right in range(len(s)):
        c = s[right]
        window[c] = window.get(c, 0) + 1

        if c in count_t and window[c] == count_t[c]:
            have += 1

        while have == need:
            # Update result if this window is smaller
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1
            # Shrink window from left
            window[s[left]] -= 1
            if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                have -= 1
            left += 1

    l, r = res
    return s[l:r+1] if res_len != float('inf') else ""
