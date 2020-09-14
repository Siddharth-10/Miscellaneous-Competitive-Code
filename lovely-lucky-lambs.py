def solution(total_lambs):
    generous_lambs = generous(total_lambs)
    stingy_lambs = stingy(total_lambs)

    diff_lambs = stingy_lambs - generous_lambs
    return diff_lambs

def generous(total_lambs):
    i = 1
    total = 0
    count  = 0
    while total + i <= total_lambs:
        total = total + i
        count = count + 1
        i = i*2

    return count 

def stingy(total_lambs):
    a = 1
    b = 1
    total = 1
    count = 1
    while total + b<= total_lambs:
        temp = a + b
        a = b
        b = temp
        total = total + a
        count = count + 1

    return count




solution(143)