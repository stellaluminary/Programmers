"""
Method 2

"""

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps, x, y):
    global n, m
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
    return maps[n - 1][m - 1]


def solution(maps):
    global n, m
    n, m = len(maps), len(maps[0])

    answer = bfs(maps, 0, 0)
    return -1 if answer == 1 else answer

"""
Method 1

"""

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(maps, x, y):
    global n, m
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 0:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
    return maps[n - 1][m - 1]

def solution(maps):
    global n, m
    n, m = len(maps), len(maps[0])

    answer = bfs(maps, 0, 0)
    return -1 if answer == 1 else answer