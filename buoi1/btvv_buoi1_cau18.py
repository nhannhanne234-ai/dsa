def search_matrix(M, x):
    for row_idx in range(len(M)):
        for col_idx in range(len(M[row_idx])):
            if M[row_idx][col_idx] == x:
                return (row_idx, col_idx)
    return (-1, -1)

M18 = [[5, 8, 1], [3, 9, 7], [2, 6, 4]]
x18 = 9
print(search_matrix(M18, x18))