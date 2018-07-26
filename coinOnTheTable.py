import copy



def coinOntheTable(m, k, board):
    star = findstar(m, board)
    if sum(star) > k:
        return -1
    else:
        for change in range(sum(star)):
            if miniChange(m, k, board, change):
                return change
        print("should not reach here, something wrong!")
        return -1

    board_temp = copy.deepcopy(board)
    board_temp[1][1]='*'









row = 2
column = 2
k = 3
board = [['R','D'],['*','L']]
coinOntheTable(column, k, board)
print(board)