from typing import List

def encode(strs: List[str]) -> str:
    ret = ""
    for s in strs:
        ret = ret + str(len(s)) + "$" + s

    return ret

def decode(s: str) -> List[str]:
    ret = []
    i = 0
    size_str = ""
    while i < len(s):
        c = s[i]
        if c != "$":
            size_str = size_str + c
            i = i + 1
        else:
            size_int = int(size_str)
            word_start_i = i + 1
            word_end_i = i + 1 + size_int
            word = s[word_start_i:word_end_i]
            ret.append(word)
            i = word_end_i
            size_str = ""
    return ret

strs = ["neet","code","love","you"]
print(encode(strs))
print(decode(encode(strs)))
#4$neet4$code4$love3$you