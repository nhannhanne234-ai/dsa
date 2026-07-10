def question_four(T):
    n = len(T)
    result = [0] * n
    stack = []
    for i in range(n):
        while stack and T[i] > T[stack[-1]]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result

T = [73, 74, 75, 71, 69, 72, 76, 73]
print(question_four(T))