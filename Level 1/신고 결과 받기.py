"""
Method 3

"""

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

"""
Method 2

"""


def solution(id_list, report, k):
    report = list(set(report))
    l = {i: [] for i in id_list}
    d = {i: 0 for i in id_list}
    answer = [0] * len(id_list)

    for i in report:
        # user, report한 사람
        u, r = i.split()

        # d: 신고당한 ID의 누적 횟수 체크
        d[r] += 1

        # user가 신고한 ID 저장
        l[u].append(r)

    for id, n in d.items():
        # 만약 신고 누적 횟수가 k를 넘어간다면
        if n >= k:
            # 정지당할 id에 따른 메일 송신을 위해 각 user별 조사
            for user, rep in l.items():
                if id in rep:
                    answer[id_list.index(user)] += 1

    return answer




"""
Method 1

91.7/100
틀림 - 시간 초과
"""
def solution(id_list, report, k):
    report = list(set(report))
    l = [(i, []) for i in id_list]
    d = {i: 0 for i in id_list}

    for i in report:
        u, r = i.split()
        d[r] += 1
        for j in range(len(l)):
            if l[j][0] == u and r not in l[j][1]:
                l[j][1].append(r)

    res_s = []
    for i in d:
        if d[i] >= k:
            res_s.append(i)

    answer = [0] * len(id_list)

    for i in range(len(l)):
        for j in res_s:
            if j in l[i][1]:
                answer[i] += 1

    return answer


