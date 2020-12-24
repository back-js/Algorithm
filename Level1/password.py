def solution(s, n):
    alphabet_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_u = []
    for i in alphabet_l:
        alphabet_u.append(i.upper())
    result = []
    for i in range(len(s)):
        if s[i] in alphabet_l:
            value = (alphabet_l.index(s[i]) + n) % 26
            new_value = alphabet_l[value]
            result.append(new_value)

        elif s[i] in alphabet_u:
            value = (alphabet_u.index(s[i]) + n) % 26
            new_value = alphabet_u[value]
            result.append(new_value)
        elif s[i] == ' ':
            result.append(s[i])

    return ''.join(result)