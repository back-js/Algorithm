'''

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
'''
# n 노드수
# m 간선 수
# 출발 노드
n, m, v = map(int, input().split())

adj = [[0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

def dfs(v, hist, adj):
    hist.append(v)
    for i in range(1, n + 1):
        if adj[v][i] and i not in hist:
            hist = dfs(i, hist, adj)
    return hist

def bfs(v, adj):
    q = [v]
    hist = [v]
    while q:
        now = q.pop(0)
        for i in range(1, n + 1):
            if adj[now][i] and i not in hist:
                q.append(i)
                hist.append(i)
    return hist

print(' '.join(map(str, dfs(v, [], adj))))
print(' '.join(map(str, bfs(v, adj))))