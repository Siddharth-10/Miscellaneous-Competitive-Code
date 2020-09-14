x = int(input())

value_one = 0
value_two = x*(x+1)
value_three = x-1
var = str()
value_two = (value_two - value_three)*10
print(value_one,value_two)
i = 0
while i < x:
    
    star,tri2,tri3 = '*',str(),''
    star = star*i*2
    
    k = 0
    y = value_two
    while k<x-i:
        tri3 = tri3 + str(y)
        y += 10
        k+=1
    value_two = value_two - (x-i-1)*10
    
    
    
    j = 0
    while j<x-i:
        tri2 = tri2 + str(value_one+10)
        value_one += 10
        j+=1
    
    var = star+tri2+tri3[:-1]
    print(var)
    i+=1
