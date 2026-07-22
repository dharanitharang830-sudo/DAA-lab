def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(board, row, n):
    if row == n:
        for i in range(n):
            for j in range(n):
                if board[i] == j:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve(board, row + 1, n):
                return True
            board[row] = -1
    return False

n = int(input("Enter N: "))
board = [-1] * n

if not solve(board, 0, n):
    print("No solution exists")
