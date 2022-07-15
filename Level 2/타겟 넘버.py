"""
Method 4
내 코드
"""

def dfs(idx, numbers, res, target):
    global answer

    if idx == len(numbers):
        if res == target:
            answer += 1
        return

    dfs(idx + 1, numbers, res + numbers[idx], target)
    dfs(idx + 1, numbers, res - numbers[idx], target)

def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, numbers, 0, target)
    return answer

"""
Method 3
타 코드
"""

from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

"""
Method 2
타 코드
"""

def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

"""
Method 1
내 코드
"""

def dfs(visit, idx, numbers, res, target, cnt):
    if idx == len(numbers):
        if res == target:
            cnt += 1
        return cnt

    visit[idx] = 1

    res += numbers[idx]
    cnt = dfs(visit, idx + 1, numbers, res, target, cnt)
    res -= numbers[idx]

    res -= numbers[idx]
    cnt = dfs(visit, idx + 1, numbers, res, target, cnt)
    res += numbers[idx]

    visit[idx] = 0

    return cnt


def solution(numbers, target):
    answer = 0
    visit = [0] * len(numbers)
    answer = dfs(visit, 0, numbers, 0, target, 0)

    return answer