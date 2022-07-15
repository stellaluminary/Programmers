"""
Method 3

"""

def solution(answers):
    pattern = [[1, 2, 3, 4, 5],
               [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score = [0, 0, 0]

    for e, ans in enumerate(answers):
        for i, v in enumerate(pattern):
            if ans == v[e % len(v)]:
                score[i] += 1

    return [i + 1 for i, v in enumerate(score) if v == max(score)]

"""
Method 2

"""

def solution(answers):
    answer = []
    n1_pattern = [1, 2, 3, 4, 5]
    n2_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    n3_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    for e, ans in enumerate(answers):
        if ans == n1_pattern[e % len(n1_pattern)]:
            score[0] += 1
        if ans == n2_pattern[e % len(n2_pattern)]:
            score[1] += 1
        if ans == n3_pattern[e % len(n3_pattern)]:
            score[2] += 1

    for idx, v in enumerate(score):
        if v == max(score):
            answer.append(idx + 1)

    return answer

"""
Method 1

"""


def solution(answers):
    answer = []

    n1_pattern = [1, 2, 3, 4, 5]
    n2_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    n3_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    n1, n2, n3 = [], [], []
    for i in range(len(answers)):
        n1.append(n1_pattern[i % len(n1_pattern)])
        n2.append(n2_pattern[i % len(n2_pattern)])
        n3.append(n3_pattern[i % len(n3_pattern)])

    d = {1: 0, 2: 0, 3: 0}

    for e, ans in enumerate(answers):
        if ans == n1[e]:
            d[1] += 1
        if ans == n2[e]:
            d[2] += 1
        if ans == n3[e]:
            d[3] += 1

    M = 0
    for k, v in d.items():
        if v > M:
            answer = [k]
            M = v
        elif v == M:
            answer.append(k)

    return answer