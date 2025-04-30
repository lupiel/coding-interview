from typing import List
from collections import defaultdict

def group_anagrams(strs: List[str]) -> List[List[str]]:
    res = {}
    
    for s in strs:
        key = str(sorted(s))
        curr_group = res.get(key, [])
        curr_group.append(s)
        res[key] = curr_group

    return list(res.values())





# n - number of strings
# m - longest string length

# naive solution
# sort letters in a string
# sort strings
# return groups

# Time O(n * mlogm)
# Space O(n * m)

strs = ["eat","tea","tan","ate","nat","bat"]
ret = [["bat"],["nat","tan"],["ate","eat","tea"]]

print(group_anagrams(strs))




strs = [""]
print(group_anagrams(strs))



strs = []
print(group_anagrams(strs))
