"""
Method 3

"""
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

"""
Method 2

"""

def solution(lottos, win_nums):
    grade = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    correct, zero = 0, 0

    for i in range(6):
        if lottos[i] == 0:
            zero += 1
        elif lottos[i] in win_nums:
            correct += 1

    answer = [grade[correct + zero], grade[correct]]
    return answer

"""
Method 1
93.3 / 100

correct = 0, zero=0일 가능성이 있음 이 부분 때문인 듯
"""

def solution(lottos, win_nums):
    correct, zero = 0, 0

    for i in range(6):
        if lottos[i] == 0:
            zero += 1
            continue
        if lottos[i] in win_nums:
            correct += 1

    answer = [7 - (correct + zero), 0]
    if correct in [1, 0]:
        answer[1] = 6
    else:
        answer[1] = 7 - correct

    return answer