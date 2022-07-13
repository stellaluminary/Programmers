"""
Method 3

"""

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)


"""
Method 2

"""

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

"""
Method 1

"""


def solution(s):
    d = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
         'eight': '8', 'nine': '9'}
    answer = ''
    tmp = ''
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]

        elif s[i].isalpha():
            tmp += s[i]

            if tmp in d:
                answer += d[tmp]
                tmp = ''

    return int(answer)