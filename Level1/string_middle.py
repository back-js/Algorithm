"""
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
s	return
abcde	c
qwer	we
qweqasdaqweg
"""

def solution(s):
    lenth = len(s)
    lenth_half = int(lenth/2)
    if lenth % 2 == 0 : #짝수
        first = s[lenth_half-1]
        second = s[lenth_half]
        result = first + second


    else :
        result = s[lenth_half]

    answer = result
    return answer

###################

def string_middle(str):
    # 함수를 완성하세요

    return str[(len(str)-1)//2:len(str)//2+1]

###############
def string_middle(str):
    a = len(str)
    if a % 2 == 0 :
        a = (a-2) / 2
    else :
        a = (a-1) / 2
    return str[int(a) : -int(a)]