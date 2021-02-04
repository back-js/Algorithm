'''
두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는
가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
예를 들어 begin이 hit, target가 cog, words가 [hot,dot,dog,lot,log,cog]라면
hit -> hot -> dot -> dog -> cog와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐
 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

제한사항
각 단어는 알파벳 소문자로만 이루어져 있습니다.
각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
begin과 target은 같지 않습니다.
변환할 수 없는 경우에는 0를 return 합니다.

입출력 예
begin	target	words	return
hit	cog	[hot, dot, dog, lot, log, cog]	4
hit	cog	[hot, dot, dog, lot, log]	0

'''
from collections import deque

from collections import deque


def is_change(now, x):
    """ 문자열 now와 x가 한글자만 차이나는지 확인. """

    length = len(now)
    cnt = 0
    for i in range(length):
        if now[i] != x[i]:
            cnt += 1
        if cnt > 1:
            return False

    if cnt == 1:
        return True
    else:
        return False


def bfs(begin, target, words):
    """ 넓이 우선 탐색으로 begin에서 target까지의 최소 거리를 구함. """

    length = len(words)
    visited = [False] * length

    queue = deque()
    queue.append((begin, 0, len(words) - 1))

    while queue:
        now, depth, idx = queue.pop()

        if now == target:
            return depth

        if depth == length:
            continue

        visited[idx] = True

        for i, x in enumerate(words):
            if not visited[i] and is_change(now, x):
                queue.append((x, depth + 1, i))

    return 0


def solution(begin, target, words):
    if target not in words:
        return 0

    if begin not in words:
        words.append(begin)

    return bfs(begin, target, words)


def main():
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))
    words = ["hot", "dot", "dog", "lot", "log"]
    print(solution(begin, target, words))


if __name__ == '__main__':
    main()
