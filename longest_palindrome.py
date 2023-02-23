from collections import Counter

def longestPalindrome(words:list[str]) -> int:
    c = Counter(words)
    found = 0
    l = 0
    for w in c.keys():
        print(w[::-1])
        if w == w[::-1]:
            if c[w] %2 == 1:
                found = 2

words = ["lc","cl","gg"]
longestPalindrome(words)