mat = [[1,2,3], [4,5,6], [7,8,9]]
k = 1
m = len(mat)
n = len(mat[0])
pref_mat = [[0 for i in range(n)] for j in range(m)]

# step-1
for i in range(m):
    pref_mat[i][0] = mat[i][0]
    for j in range(1, n):
        pref_mat[i][j] = pref_mat[i][j-1] + mat[i][j]

# step-2
for i in range(n):
    pref_mat[0][i] = pref_mat[0][i]

    for j in range(1, m):
        pref_mat[j][i] = pref_mat[j-1][i] + pref_mat[j][i]

# step-3
for i in range(m):
    row_upper = max(i-k, 0)
    row_down = min(i+k, m-1)
    for j in range(n):
        col_upper = max(j-k, 0)
        col_down = min(j+k, n-1)

        value = pref_mat[row_down][col_down]

        if row_upper-1>=0:
            value -= pref_mat[row_upper-1][col_down]

        if col_upper-1 >= 0:
            value -= pref_mat[row_down][col_upper-1]

        if row_upper-1>=0 and col_upper-1>=0:
            value += pref_mat[row_upper-1][col_upper-1]
        mat[i][j] = value

print(mat)

