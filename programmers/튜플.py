def solution(s):
    a = s[2:-2].split('},{')
    aa = []
    a.sort(key=lambda x: len(x))
    for i in a :
        k = list(i.split(','))
        aa.append(k)

    result = []
    for i in aa :
        for j in i :
            if int(j) not in result:
                result.append(int(j))
    print(result)

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")