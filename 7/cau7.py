def question_seven(A, S):
    prefix = 0
    count = 0
    mp = {0:1}
    for x in A:
        prefix += x
        if prefix - S in mp:
            count += mp[prefix - S]
        mp[prefix] = mp.get(prefix, 0) + 1
    return count

A = [3, 4, 7, 2, -3, 1, 4, 2]
S = 7
print(question_seven(A, S))