def solution(user_id, banned_id):
    result = set()
    for ban in banned_id :
        for user in user_id :
            if len(ban) == len(user) :
                r = False
                for k in range(len(ban)):
                    if ban[k] == '*' :
                        continue
                    if ban[k] != ban[k]:
                        r = False
                        break
                    r = True
                if r == True :
                    result.add(user)
    print(result)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])


