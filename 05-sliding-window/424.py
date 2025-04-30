

def longest_repeating_character_with_replacement(s, k):

    counts = [0] * (ord('Z') - ord('A') + 1)
    left = 0
    longest = 0

    for right in range(len(s)):
        counts[ord(s[right])-ord('A')] += 1
        while right-left+1 - max(counts) > k:
            counts[ord(s[left])-ord('A')] -= 1
            left += 1
            print(left, right, counts)

        longest = max(longest, right-left+1)
        right += 1
        print(left, right, counts)
    return longest

print(longest_repeating_character_with_replacement("SSIISSIII", 2))
print(longest_repeating_character_with_replacement("", 2))
print(longest_repeating_character_with_replacement("S", 2))