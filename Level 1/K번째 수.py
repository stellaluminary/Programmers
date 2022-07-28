"""
URL : https://school.programmers.co.kr/learn/courses/30/lessons/42748
"""

"""
Method 2

"""
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

"""
Method 1

"""

def solution(array, commands):
    answer = []

    for c in commands:
        a = [array[i - 1] for i in range(c[0], c[1] + 1)]
        a.sort()
        answer.append(a[c[2] - 1])

    return answer