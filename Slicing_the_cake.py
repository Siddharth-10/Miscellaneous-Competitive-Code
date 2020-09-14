def solution(s):
    length = len(s)
    p = 1
    start = 0
    s2 = 0
    e = 0 
    while p < length:
        if s[p] != s[p-s2] and s2 != start and (s2 % p) != 0:
            s2 = start
        if s[start] == s[p]  and s2 == start:
            s2 = p
        if s2 % p == 0 and s2 != 0 and p != s2:
            e = s2
            div = splitvalue(s,s2) 
            if div == 0:
                s2 = start
            else:
                break
        p = p+1
    if p == length and s2!=0:
        div = splitvalue(s,s2)
    else:
        div = 1
    

    print(int(div))

def splitvalue(st,e):
    i = e
    count = len(st)/e
    if count != int(count):
        return 0
    while i < len(st):
        j = 0
        k = i
        while j < e:
            try:
                if st[j] != st[k]:
                    return 0
            except:
                break
            j = j +1
            k = k +1 
        i = i + e

    return count

solution('baaaaaaaaaaab')