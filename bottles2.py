def main():
    total_bottle = int(input())
    bottle_radius = list(map(int, input().split()))

    bottle_status = [0]*total_bottle

    bottle_radius.sort()

    a = list(bottle_status)

    i = 0
    while i < total_bottle:
        j = i + 1
        while j < total_bottle:
            if bottle_radius[i] < bottle_radius[j] and bottle_status[j] == 0:
                bottle_status[j] = 1
                bottle_radius.pop(i)
                bottle_status.pop(i)
                j = j - i
                break
            else:
                j += 1
        if bottle_status == a:
            break
        a = list(bottle_status)
        i += 1

    count = 0
    for i in bottle_radius:
        if i == 0:
            count += 1
    print(count)

main()
