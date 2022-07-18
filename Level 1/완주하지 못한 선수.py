"""
Method 4
타 코드
"""

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

"""
Method 3
타 코드
"""

from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer)[0]

"""
Method 2

"""

def solution(participant, completion):
    p = {}

    for i in participant:
        if i not in p:
            p[i] = 1
        else:
            p[i] += 1

    for i in completion:
        if i in p:
            p[i] -= 1

    for i in p:
        if p[i] != 0:
            return i

"""
Method 1

정확성 테스트 - 50점
효율성 테스트 - 0점 시간 초과

50/100


추가 테스트 
["mislav", "stanko", "mislav", "ana"]
["stanko", "mislav", "mislav"]
"ana"
"""


def solution(participant, completion):
    answer = ''
    p = {i: participant.count(i) for i in participant}

    for i in completion:
        if i in p:
            p[i] -= 1

    for i in p:
        if p[i] != 0:
            return i