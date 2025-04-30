
def is_palindrome(s):

    l, r = 0, len(s) - 1

    while l < r:
        while not s[l].isalnum():
            l = l + 1
        while not s[r].isalnum():
            r = r - 1
        if s[l].lower() != s[r].lower():
            return False
        l = l + 1
        r = r - 1

    return True

# Time O(n)
# Space O(1)


def test():
    print("running tests")
    s = "A man, a plan, a canal: Panama"
    r = True
    assert is_palindrome(s) == r


    s = "banana"
    r = False
    assert is_palindrome(s) == r


test()