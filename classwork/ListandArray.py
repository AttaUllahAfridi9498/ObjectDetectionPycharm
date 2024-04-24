
""""
row = []

for i in range(8):
    row.append("WHITE_PAWN")
print(row)


arr={"A","B","C"
        "D","E","F"
    "G","H","I"
}

accessElement= arr[1],[1]
print(accessElement)
"""
EMPTY = "-"
ROOK = "R"
KING = "K"
PAWN = "P"

board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[3][3] = KING
board[3][0] = PAWN
board[3][7] = PAWN
board[7][0] = ROOK
board[7][7] = ROOK
board[6][7] = KING

# Print the board in matrix form
for i in range(8):
    for j in range(8):
        print(board[i][j],end="\t\t")
    print()



