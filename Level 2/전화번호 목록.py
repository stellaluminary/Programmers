"""
Method 2

"""

def solution(phone_book):
    phone_book.sort()
    for i,e in zip(phone_book, phone_book[1:]):
        if e.startswith(i):
            return False
    return True

"""
Method 1

정확성 테스트 : 83.3 (all)
효율성 테스트 : 8.3

91.7/100
"""


def solution(phone_book):
    answer = True
    phone_book.sort(key=len)

    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False

    return answer