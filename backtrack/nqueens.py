n=4
result = []
# board = [[0]*n]*n
board = [["." for i in range(n)] for j in range(n)]
# define is_safe function
def is_safe(board, row, col):
    # check the vertical position
    r,c = row, col
    while r>=0:
        if board[r][c] == 'Q':
            return False
        r-=1

    # check the diagonal position
    r,c = row, col
    while r >=0 and c>=0:
        if board[r][c] == 'Q':
            return False
        r-=1
        c-=1
    
    # check the anti-diagonal postition
    r,c = row, col
    while r>=0 and c < len(board):
        if board[r][c] == 'Q':
            return False
        r-=1
        c+=1
    return True

def convert_solution(board, n):
    return [''.join(row) for row in board]

def nqueens(board, row, n):
    if row > len(board):
        add_solution(board, n)
    
    for i in range(n):
        if is_safe(board, row, i):
            board[row][i] = 'Q'
            nqueens(board, row+1, i)
            board[row][i] = '.'

nqueens(board, 0, n)
print(result)