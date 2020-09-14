def main():
    total_bottles = int(input())
    bottle_radius = list(map(int,input().split()))
    bottle_status = [0]*total_bottles
    bottle_enclosed = [0]*total_bottles


    bottle_radius.sort()
    i = 0
    a = list(bottle_status)
    while i < total_bottles:
        j = i+1
        k = i
        while j < total_bottles:
            if j == total_bottles - 1 and bottle_status[j] == 1:
                break
            elif bottle_radius[k] < bottle_radius[j] and bottle_status[j] != 1 and bottle_enclosed[k] != 1:
                bottle_enclosed[k] = 1
                bottle_status[j] = 1
                k = j
            else:
                j += 1
        if bottle_status == a:
            break
        a = list(bottle_status)
        i += 1

    count = 0
    for i in bottle_enclosed:
        if i == 0:
            count += 1
    print(count)




main()