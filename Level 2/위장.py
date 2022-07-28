"""
URL : https://school.programmers.co.kr/learn/courses/30/lessons/42578
"""

"""
Method 3
"""

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    # Noramlly use like "reduce(function, list or dict)"
    # However, we can use with additional initial value
    # "reduce(function, list or dict, initial value)"

    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

"""
Method 2
"""

def solution(clothes):
    answer = 1
    d = {}

    for name, type in clothes:
        if type not in d:
            d[type] = 2
        else:
            d[type] += 1

    for i in d.values():
        answer *= i
    return answer - 1

"""
Method 1
"""

def solution(clothes):
    answer = 1
    d = {}

    for name, type in clothes:
        if type not in d:
            d[type] = ['', name]
        else:
            d[type].append(name)

    for i in d:
        answer *= len(d[i])
    return answer - 1