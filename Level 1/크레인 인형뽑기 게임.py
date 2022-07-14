"""
Method 3

"""


"""
Method 2

내 코드
"""

def solution(board, moves):
    stack = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if stack and stack[-1] == board[j][i-1]:
                    stack.pop(-1)
                    answer += 2
                else:
                    stack.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
    return answer

"""
Method 1

내 코드
"""

def solution(board, moves):
    stack = []
    answer = 0
    row = len(board)
    col = len(board[0])
    d = {i: [] for i in range(1, col + 1)}

    for i in range(row):
        for j in range(col):
            d[j + 1].append(board[i][j])

    for k in moves:
        if sum(d[k]) == 0:
            continue
        for j in range(len(d[k])):
            if d[k][j] == 0:
                continue
            else:
                if stack and stack[-1] == d[k][j]:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(d[k][j])
                d[k][j] = 0
                break

    return answer

