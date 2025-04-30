def len_of_longest(s):

    left = 0
    longest = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        length = right - left + 1
        longest = max(longest, length)
        seen.add(s[right])
        right += 1

    return longest
s="abcdefcbabb"
print(len_of_longest(s))

