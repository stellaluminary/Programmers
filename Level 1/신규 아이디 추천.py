"""
Method 3

"""

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3 - len(st))])

    return st


"""
Method 2

"""

def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'

    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]

    if answer[-1] == '.':
        answer = answer[:-1]

    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer

"""
Method 1

"""


def solution(new_id):
    tmp = ''
    answer = ''

    for i in range(len(new_id)):
        if new_id[i].isnumeric() or new_id[i] in ['-', '_', '.']:
            tmp += new_id[i]
        elif new_id[i].isalpha():
            tmp += new_id[i].lower()

    for i in range(len(tmp)):
        if i > 0 and tmp[i] == '.' and tmp[i - 1] == '.':
            continue
        else:
            answer += tmp[i]

    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'

    if len(answer) == 0:
        answer += 'a'
    elif len(answer) > 15:
        answer = answer[:15]

    if answer[-1] == '.':
        answer = answer[:-1]

    if len(answer) < 3:
        answer += answer[-1] * (3 - len(answer))

    return answer