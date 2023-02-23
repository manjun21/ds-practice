#Constraint: 0<=len(s)<=1000
#Given a string:
#1.) Take all prefixes of the string and choose the longest palindrome between them.
#2.) If chosen prefix has atleast two characters, cut this from s and go back to step 1 with the updated string. Otherwise, end the algo with the current string s.


def is_palindrome(s):
    return s == s[::-1]

def solution(s):
    prefixes = []
    for i in range(0, len(s)):
        prefixes.append(s[:i+1])

    longest = None
    for prefix in prefixes:
        if is_palindrome(prefix):
            if not longest:
                longest = prefix
            elif len(prefix) > len(longest):
                longest = prefix

    while longest:
        if len(longest) >= 2:
            #print(s[len(longest):])
            s1 = s[len(longest):]
            if len(s1) == 0:
                return longest   
            else:
                return solution(s[len(longest):])
        else:
            return s
    return s

#s1 = 'aaacodedoc'
s2 = ''
print(solution(s2))