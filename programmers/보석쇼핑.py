def solution(gems):
    gems_num = len(gems)
    gems_kinds = len(set(gems))
    start, end = 0,0
    cur_shop = {gems[0]: 1}
    answer = []
    while start < gems_num and end < gems_num :
        if len(cur_shop) < gems_kinds :
            end += 1
            if end == gems_num:
                break
            if gems[end] in cur_shop :
                cur_shop[gems[end]] += 1
            else :
                cur_shop[gems[end]] = 1
        else :
            answer.append((end-start,[start+1,end+1]))
            cur_shop[gems[start]] -= 1
            if cur_shop[gems[start]] == 0:
                del cur_shop[gems[start]]
            start += 1
    answer = sorted(answer, key=lambda x: (x[0], x[1]))
    return answer[0][1]


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])