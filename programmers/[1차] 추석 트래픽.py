입력: [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

def solution(lines):
    for line in lines :
        a,b,c = line.split(' ')
        bb = b.split(':')
        

    return answer






def checktr(time,li):
    c=0
    start=time
    end=time+1000
    for i in li:
        if i[1] >= start and i[0] < end:
            c += 1
    return c

def solution(lines):
    li=[]
    r=1
    for line in lines:
        y,a,b=line.split()
        a=a.split(':')
        b=float(b.replace('s',''))*1000
        end=(int(a[0])*3600 + int(a[1])*60 + float(a[2]))*1000
        start=end-b+1
        li.append([start,end])
    for i in li:
        r=max(r,checktr(i[0],li),checktr(i[1],li))
    return r