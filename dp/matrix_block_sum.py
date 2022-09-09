
# mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = [[1,2], [4,5]]
k = 1
# ans [[12,21,16],[27,45,33],[24,39,28]]

m = len(mat)
n = len(mat[0])

ans = [[-1 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        total = 0
        row, col = [], []
        for l in range(i-k, i+k+1):
            if l < 0 or l > m-1:
                continue
            row.append(l)
        for p in range(j-k, j+k+1):
            if p < 0 or p > n-1:
                continue
            col.append(p)

        for r in row:
            for c in col:
                total += mat[r][c]
        ans[i][j] = total

print(ans)


# def recurse(r, c, mat, ans):
#     if r == 0 and c == 0:
#         return
    
#     if r < 0 or r > len(mat)-1:
#         return 0
#     if c < 0 or c > len(mat[0])-1:
#         return 0
    
#     up = recurse(r-1, c, mat, ans)
#     up_right = recurse(r-1, c+1, mat, ans)
#     up_left = recurse(r-1, c-1, mat, ans)

#     left = recurse(r, c-1, mat, ans)
#     right = recurse(r, c+1, mat, ans)

#     ans[r][c] = up + up_right + up_left + left + right + mat[r][c]
#     return ans

# ans = recurse(m-1, n-1, mat, ans)
# print(ans)