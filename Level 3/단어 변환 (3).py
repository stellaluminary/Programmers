"""
URL : https://school.programmers.co.kr/learn/courses/30/lessons/43163
"""

"""
Method 2

"""

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    q = deque()
    q.append([begin, 0])
    v = [0] * len(words)

    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            diff = 0
            if not v[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        diff += 1
                if diff == 1:
                    v[i] = 1
                    q.append([words[i], cnt + 1])
    return 0

"""
Method 1

-> 수정 diff_check 함수 속 
if a[i] in b:
    l += 1    
에서 
if a[i] == b[i]:
    l += 1    
로 변환함. 수정 전 방법은 틀린 방법

이유 : 위치적 정보 없이 그냥 있냐만 묻는 것과 위치적 정보까지 묻는 것의 차이

"""

def diff_check(a, b):
    l = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            l += 1
    if l == len(a) - 1:
        return True
    else:
        return False


def dfs(current, target, words, visit, depth, ans):
    if current == target:
        ans.append(depth)
        return

    for i in range(len(words)):
        if not visit[i]:
            if diff_check(current, words[i]):
                visit[i] = 1
                dfs(words[i], target, words, visit, depth + 1, ans)
                visit[i] = 0


def solution(begin, target, words):
    if target not in words:
        return 0

    visit = [0] * len(words)
    ans = []
    dfs(begin, target, words, visit, 0, ans)
    if ans:
        return min(ans)
    else:
        return 0