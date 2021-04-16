
from collections import defaultdict


def solution(gems):
    result = [0, len(gems)]
    gem_kinds = len(set(gems))
    count_dict = defaultdict(int)
    count_dict[gems[0]] = 1

    left_idx, right_idx = 0, 0
    while right_idx < len(gems) and left_idx < len(gems):
        if len(count_dict) == gem_kinds:
            if result[1] - result[0] > right_idx - left_idx:
                result = [left_idx + 1, right_idx + 1]

            count_dict[gems[left_idx]] -= 1
            if count_dict[gems[left_idx]] == 0:
                del count_dict[gems[left_idx]]
            left_idx += 1

        else:
            right_idx += 1
            if right_idx == len(gems):
                break
            count_dict[gems[right_idx]] += 1

    return result


def solution(gems):
    TYPE_NUM = len(set(gems)) # 종류개수
    GEM_NUM = len(gems) # 진열대 길이
    answer = []
    start, end = 0, 0
    DIST, INDEX = 0, 1 # 구간, index
    # 초기값
    cur_shop = {gems[0]: 1}
    while start < GEM_NUM and end < GEM_NUM:
        if len(cur_shop) < TYPE_NUM: # 아직 전체 모음 아님
            end += 1
            if end == GEM_NUM:
                break
            cur_shop[gems[end]] = cur_shop.get(gems[end], 0) + 1
        else:
            answer.append((end-start, [start+1, end+1]))
            cur_shop[gems[start]] -= 1
            if cur_shop[gems[start]] == 0:
                del cur_shop[gems[start]]
            start += 1
    answer = sorted(answer, key=lambda x: (x[DIST], x[INDEX]))
    return answer[0][INDEX]
   