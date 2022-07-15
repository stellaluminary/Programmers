"""
Method 3

"""

def dfs(computers, visit, start, n):
    visit[start] = 1

    for i in range(n):
        if visit[i] == 0 and computers[start][i] == 1:
            dfs(computers, visit, i, n)

def solution(n, computers):
    answer = 0
    visit = [0] * n

    for i in range(n):
        if visit[i] == 0:
            dfs(computers, visit, i, n)
            answer += 1

    return answer

"""
Method 2

"""

def parent(p, x):
    if p[x] != x:
        p[x] = parent(p, p[x])
    return p[x]


def union(p, a, b):
    a = parent(p, a)
    b = parent(p, b)
    p[max(a, b)] = min(a, b)


def solution(n, computers):
    p = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                union(p, i, j)

    a = []
    for i in range(n):
        a.append(parent(p, i))
    answer = len(set(a))

    return answer

"""
Method 1

92.3/100
"""


def parent(p, x):
    if p[x] != x:
        p[x] = parent(p, p[x])
    return p[x]

def union(p, a, b):
    a = parent(p, a)
    b = parent(p, b)
    p[max(a, b)] = min(a, b)

def solution(n, computers):
    p = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                union(p, i, j)
    answer = len(list(set(p)))

    return answer