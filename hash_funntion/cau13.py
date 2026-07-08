def matrix_hash(matrix, p_row=31, p_col=37):
    h = 0
    for i in range(len(matrix)):
        row_hash = 0
        for j in range(len(matrix[0])):
            row_hash = row_hash * p_row + matrix[i][j]
        h = h * p_col + row_hash
    return h

big = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 1, 2, 3],
    [4, 5, 6, 7]
]
pattern = [
    [6, 7],
    [1, 2]
]
pattern_hash = matrix_hash(pattern)
found = False
for i in range(len(big) - len(pattern) + 1):
    for j in range(len(big[0]) - len(pattern[0]) + 1):
        sub = []
        for r in range(len(pattern)):
            row = []
            for c in range(len(pattern[0])):
                row.append(big[i + r][j + c])
            sub.append(row)
        if matrix_hash(sub) == pattern_hash:
            print("Tìm thấy tại:", (i, j))
            found = True
if not found:
    print("Không tìm thấy")