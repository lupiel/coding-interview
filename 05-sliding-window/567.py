
def is_permutation_in(s1, s2):
    n_letters = ord('z') - ord('a')
    s1_freq = [0] * n_letters
    for c in s1:
        s1_freq[ord(c)-ord('a')] += 1

    s1_len = len(s1)
    s2_len = len(s2)

    for i in range(s1_len, s2_len + 1):
        # create frequency array for s2[i - s1_len:i]
        window_freq = [0] * n_letters    
        for c in s2[i - s1_len:i]:
            window_freq[ord(c)-ord('a')] += 1

        if s1_freq == window_freq:
            return True
    return False



s1 = "ab"
s2 = "eidbaooo"
print(is_permutation_in(s1, s2))

s2 = "eidboaooo"
print(is_permutation_in(s1, s2))

s2 = "eidboaooba"
print(is_permutation_in(s1, s2))

s2 = "abeidboaoo"
print(is_permutation_in(s1, s2))

s2 = "a"
print(is_permutation_in(s1, s2))
