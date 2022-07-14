"""
Method 3

직접 거리를 다 구하는 방법

타 코드

"""

def solution(numbers, hand):
    l = 10
    r = 11
    answer = ""
    p = [[0, 4, 3, 4, 3, 2, 3, 2, 1, 2],
         [4, 0, 1, 2, 0, 2, 3, 0, 3, 4],
         [3, 1, 0, 1, 2, 1, 2, 3, 2, 3],
         [4, 2, 1, 0, 3, 2, 1, 4, 3, 2],
         [3, 0, 2, 3, 0, 1, 2, 0, 2, 3],
         [2, 2, 1, 2, 1, 0, 1, 2, 1, 2],
         [3, 3, 2, 1, 2, 1, 0, 3, 2, 1],
         [2, 0, 3, 4, 0, 2, 3, 0, 1, 2],
         [1, 3, 2, 3, 2, 1, 2, 1, 0, 1],
         [2, 4, 3, 2, 3, 2, 1, 2, 1, 0],
         [1, 0, 4, 5, 0, 3, 4, 0, 2, 3],
         [1, 5, 4, 0, 4, 3, 0, 3, 2, 0]]
    for i in numbers:
        if i in [1, 4, 7]:
            l = i
            answer += "L"
        elif i in [3, 6, 9]:
            r = i
            answer += "R"
        else:
            if p[l][i] < p[r][i]:
                l = i
                answer += "L"
            elif p[l][i] > p[r][i]:
                r = i
                answer += "R"
            elif hand == "left":
                l = i
                answer += "L"
            else:
                r = i
                answer += "R"
    return answer



"""
Method 2

타 코드

"""

def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            lhand = i
        elif i in [3,6,9]:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer

"""
Method 1

내 코드

"""


def solution(numbers, hand):
    answer = ''
    key = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    l = [3, 0]
    r = [3, 2]

    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            answer += 'L'
            l = [numbers[i] // 3, 0]
        elif numbers[i] in [3, 6, 9]:
            answer += 'R'
            r = [numbers[i] // 3 - 1, 2]
        elif numbers[i] in [2, 5, 8]:
            left_dist = abs(l[0] - numbers[i] // 3) + abs(l[1] - 1)
            rigth_dist = abs(r[0] - numbers[i] // 3) + abs(r[1] - 1)
            if left_dist > rigth_dist:
                answer += 'R'
                r = [numbers[i] // 3, 1]
            elif left_dist < rigth_dist:
                answer += 'L'
                l = [numbers[i] // 3, 1]
            else:
                if hand == 'right':
                    answer += 'R'
                    r = [numbers[i] // 3, 1]
                else:
                    answer += 'L'
                    l = [numbers[i] // 3, 1]
        # numbers[i] == 0
        else:
            left_dist = abs(l[0] - 3) + abs(l[1] - 1)
            rigth_dist = abs(r[0] - 3) + abs(r[1] - 1)
            if left_dist > rigth_dist:
                answer += 'R'
                r = [3, 1]
            elif left_dist < rigth_dist:
                answer += 'L'
                l = [3, 1]
            else:
                if hand == 'right':
                    answer += 'R'
                    r = [3, 1]
                else:
                    answer += 'L'
                    l = [3, 1]

    return answer