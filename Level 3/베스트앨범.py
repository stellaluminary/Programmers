"""
URL : https://school.programmers.co.kr/learn/courses/30/lessons/42579
"""

"""
Method 2

타 코드
"""

def solution(genres, plays):
    answer = []
    d = {e: [] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1], e[2]])

    genreSort = sorted(list(d.keys()), key=lambda x: sum(map(lambda y: y[0], d[x])), reverse=True)

    for g in genreSort:
        temp = [e[1] for e in sorted(d[g], key=lambda x: (x[0], -x[1]), reverse=True)]
        answer += temp[:min(len(temp), 2)]
    return answer

"""
Method 1
"""

def solution(genres, plays):
    answer = []
    cnt_genres = {}
    indi = {}

    for idx, (g, p) in enumerate(zip(genres, plays)):
        if g not in cnt_genres:
            cnt_genres[g] = p
            indi[g] = [(p, idx)]
        else:
            cnt_genres[g] += p
            indi[g].append((p, idx))

    a = []
    for i in cnt_genres:
        a.append((cnt_genres[i], i))
    a.sort(reverse=True)

    for e, i in enumerate(a):
        # i[1] = genres type
        indi[i[1]].sort(key=lambda x: (-x[0], x[1]))
        if len(indi[i[1]]) == 1:
            answer.append(indi[i[1]][0][1])
        else:
            for j in range(2):
                answer.append(indi[i[1]][j][1])

    return answer