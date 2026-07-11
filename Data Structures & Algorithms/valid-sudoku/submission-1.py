class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowcheck = [set() for i in range(9)]
        colcheck = [set() for i in range(9)]
        threecheck = {((i//3, j//3)):set() for i in range(9) for j in range(9)}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i][j] not in rowcheck[i]:
                        rowcheck[i].add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in colcheck[j]:
                        colcheck[j].add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in threecheck[(i//3,j//3)]:
                        threecheck[(i//3,j//3)].add(board[i][j])
                    else:
                        return False
        return True
