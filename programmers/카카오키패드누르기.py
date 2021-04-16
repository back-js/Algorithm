
def solution(numbers, hand):
    result = []
    Left = 10
    Right = 12
    while numbers :
        a = numbers.pop(0)
        if a in [1, 4, 7] :
            result.append('L')
            Left = a
        elif a in [3, 6, 9] :
            result.append('R')
            Right = a
        else :
            d_left = distance(Left,a)
            d_right = distance(Right,a)

            if d_left < d_right :
                result.append('L')
                Left = a
            elif d_left > d_right :
                result.append('R')
                Right = a
            else :
                if hand == 'left' :
                    result.append('L')
                    Left = a
                else :
                    result.append('R')
                    Right = a
    return "".join(result)

def distance(hand,target) :
    location = {'1':(0,0),'2':(0,1),'3':(0,2),
    '4':(1,0),'5':(1,1),'6':(1,2),
    '7':(2,0),'8':(2,1),'9' : (2,2), '10':(3,0),'0':(3,1),'12':(3,2)}

    hand,target = str(hand), str(target)
    hand_x,hand_y = location[hand]
    target_x, target_y = location[target]

    return abs(hand_x-target_x) + abs(hand_y-target_y)

solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left")