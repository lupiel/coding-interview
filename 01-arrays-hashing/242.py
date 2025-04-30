
def is_anagram(s: str, t: str) -> bool:
    s_counts = {}
    t_counts = {}

    for c in s:
        s_counts[c] = 1 + s_counts.get(c, 0)

    for c in t:
        t_counts[c] = 1 + t_counts.get(c, 0)


    print("s_counts", s_counts)
    print("t_counts", t_counts)
    return s_counts == t_counts

# solution sort both strings and compare letter by letter
# time O(n logn)    2*n*logn + 2*n
# space O(1)

# create a hash map for s and t, then compare hash maps
# time O(n)
# space O(n)

def test():
    s, t = "", " "
    res = False
    assert is_anagram(s, t) == res

    s, t = "xd", "dxxdd"
    res = False
    assert is_anagram(s, t) == res

    s, t = "anagram", "nagaram"
    res = True
    assert is_anagram(s, t) == res

test()