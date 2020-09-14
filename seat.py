def seattype(x):
    n = x%6
    if n in [0,1]:
        return 'WS'
    elif n in [2,5]:
        return 'MS'
    else:
        return 'AS'

def oppseat(x):
    n = int(x/6)
    a = int(x%6)
    if(a!=0):
        n = n+1
    if(n%2==0):
        if(a == 1):
            return x-1
        elif(a==2):
            return x-3
        elif(a==3):
            return x-5
        elif(a==4):
            return x-7
        elif(a==5):
            return x-9
        elif(a==0):
            return x-11
    else:
        if(a == 0):
            return x+1
        elif(a==5):
            return x+3
        elif(a==4):
            return x+5
        elif(a==3):
            return x+7
        elif(a==2):
            return x+9
        elif(a==1):
            return x+11

def main():
    t = int(input('enter t '))
    n = []
    for i in range(t):
        k = []
        for i in range(3):
            k.append('0')
        n.append(k)

    for i in range(t):
        n[i][0] = int(input('enter n '))
    
    for j in range(t):
        n[j][1] = seattype(n[j][0])
        n[j][2] = oppseat(n[j][0])
        print(n[j][2])
        print(n[j][1])

main()