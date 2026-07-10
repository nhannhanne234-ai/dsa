def question_five(A, k):
    dq = []
    result = []
    for i in range(len(A)):
        while dq and dq[0] <= i - k:
            dq.pop(0)
        while dq and A[dq[-1]] > A[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(A[dq[0]])
    return result

A = [4, 2, 12, 11, -5, 8, 1, 5, 6]
k = 3
print(question_five(A, k))