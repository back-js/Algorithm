def solution(files):
    result = []
    result2 = []
    for i in files :
        start = 0
        end = len(i)
        num = ['1','2','3','4','5','6','7','8','9','0']
        while start != end :
            if i[start] in num :
                break
            start += 1
        point1 = start

        while start != end :
            if i[start] not in num :
                break
            start += 1
        point2 = start
        if point2 == end-1 :
            result.append([i[0:point1],i[point1:],None])
        else :
            result.append([i[0:point1],i[point1:point2],i[point2:]])
    result.sort(key=lambda x : (x[0].upper(), int(x[1]), x[2]))

    for i in result:
        result2.append(''.join(i))
    return result2
solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])


def solution(files):
    dic = dict()
    for file in files:
        head_index, number_index = None, None
        for i in range(len(file)):
            if file[i].isnumeric(): break
            else: head_index = i
        for i in range(head_index+1, len(file)):
            if file[i].isnumeric(): number_index = i
            else: break
        head, number = file[:head_index+1].lower(), int(file[head_index+1:number_index+1])
        dic[file] = (head, number)
    answer = [file_name for file_name, file_info in sorted(dic.items(), key=lambda x: (x[1][0], x[1][1]))]
    return answer