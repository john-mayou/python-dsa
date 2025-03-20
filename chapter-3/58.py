"""
For each of the three algorithms, unique1, unique2, and unique3, which
solve the element uniqueness problem, perform an experimental analysis
to determine the largest value of n such that the given algorithm runs in
one minute or less.

DNA
"""

def unique1(S):
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
    return True

def unique2(S):
    temp = sorted(S)
    for j in range(1, len(temp)):
        if S[j-1] == S[j]:
            return False
    return True