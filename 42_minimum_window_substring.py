def minWindow(s, t):
    from collections import Counter

    if not t or not s:
        return ""

    need = Counter(t)       # Count each character needed
    missing = len(t)        # Total chars we need to match (including repeats)
    left = start = end = 0  # Window pointers & answer window
    min_len = float('inf')  # To keep track of minimum window length

    for right, char in enumerate(s):
        # If this char is needed, reduce missing count
        if need[char] > 0:
            missing -= 1
        need[char] -= 1  # Decrease count in window (may go negative if extra chars)

        # When all chars are matched
        while missing == 0:
            # Update answer if window is smaller
            if right - left < min_len:
                min_len = right - left
                start, end = left, right

            # Try to move left forward and see if we still have a valid window
            need[s[left]] += 1
            if need[s[left]] > 0:   # We need this char again, so window no longer valid
                missing += 1
            left += 1

    return s[start:end+1] if min_len != float('inf') else ""
