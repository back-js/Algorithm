import heapq
def solution(jobs):
    n = len(jobs)
    time, end, queue = 0, -1, []
    # 처리한 프로세스 개수
    count = 0

    answer = 0
    while count < n:
        for i in jobs:
            # i[0] = 프로세스 입력 시간, i[1] = 프로세스 끝날 때까지 걸리는 시간
            if end < i[0] <= time:
                # 현재 시간 기준, 프로세스가 queue에 들어가서 얼마나 기다렸는지.
                answer += (time - i[0])
                heapq.heappush(queue, i[1])
        if len(queue) > 0:
            # 가장 빨리 끝나는 프로세스가 끝날 때까지는 queue에 있는 프로세스 전부 대기시간이므로 값을 추가한다.
            answer += len(queue) * queue[0]
            # 끝난 시간
            end = time
            # 가장 빨리 끝나는 프로세스가 걸린 시간을 더해준다
            time += heapq.heappop(queue)
            # 프로세스가 끝났으므로 count + 1 해준다.
            count += 1
        else:
            # queue에 아직 아무것도 없으므로 시간을 +1 해준다.
            time += 1

    return (int(answer / n))

print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))

