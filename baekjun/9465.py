N = int(input())
for _ in range(N) :
    n = int(input())
    card = []
    for k in range(2):
        score = list(map(int,input().split()))
        card.append(score)
    for j in range(1,n):
        if j == 1 :
            card[0][j] = card[0][j]+card[1][j-1]
            card[1][j] = card[1][j] + card[0][j - 1]
        else :
            card[0][j] = card[0][j] + max(card[1][j-1],card[1][j-2])
            card[1][j] = card[1][j] + max(card[0][j - 1], card[0][j - 2])

    print(max(card[0][n-1],card[1][n-1]))

