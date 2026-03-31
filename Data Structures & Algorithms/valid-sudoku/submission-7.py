class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        for i in range(9):
            row = {}
            col = {}
            for j in range(9):
                
                # if board[i][j] == '.' or board[j][i] == '.':
                #     continue
                
                # Col checking 
                
                # if i == 3:
                    # print(board[j][i])
                    # print(col)
                    # print(board[j][i] not in col, board[j][i] != '.')
                if board[j][i] not in col and board[j][i] != '.':
                    
                    if i == 3: print(board[j][i])
                    key = board[j][i]
                    col[key] = 1
                elif board[j][i] in col: 
                    print(1, i,j)
                    return False

                if board[i][j] not in row and board[i][j] != '.':
                    row[board[i][j]] = 1
                elif board[i][j] in row:
                    print(2, i,j)
                    return False

                if i % 3 == 0 and j % 3 == 0:
                    # print(board[i:i+3][j:j+3])
                    three = defaultdict()

                    for k in range(3):
                        
                        for l in range(3):
                            # print(board[j][i] == )
                            # print(i,k,j,l)
                            if board[i+k][j+l] == '.':
                                continue
                            
                            if board[i+k][j+l] not in three:
                                three[board[i+k][j+l]] = 1
                            else: 
                                # print(three[board[j][i]])
                                print("3 by 3", i, j)
                                return False

        return True


"""
board=[[".",".","4",".",".",".","6","3","."],
       [".",".",".",".",".",".",".",".","."], 
       ["5",".",".",".",".",".",".","9","."],
       [".",".",".","5","6",".",".",".","."],
       ["4",".","3",".",".",".",".",".","1"],
       [".",".",".","7",".",".",".",".","."],
       [".",".",".","5",".",".",".",".","."],
       [".",".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".",".","."]]

"""