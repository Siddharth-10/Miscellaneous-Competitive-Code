def main():
    total_number = int(input())
    numbers = input().split()
    score = [0] * total_number

    i = 0
    while i < total_number:
        score[i] = [int(x) for x in numbers[i]]
        i += 1

    bitscore = [0] * total_number

    for i in range(int(total_number)):
        sum = 0
        if score[i][0] > score[i][1]:
            if score[i][0] > score[i][2]:
                sum += score[i][0] * 11
                if score[i][1] > score[i][2]:
                    sum += score[i][2] * 7
                else:
                    sum += score[i][1] * 7
            else:
                sum += score[i][2] * 11 + score[i][1] * 7
        else:
            if score[i][1] > score[i][2]:
                sum += score[i][1] * 11
                if score[i][0] > score[i][2]:
                    sum += score[i][2] * 7
                else:
                    sum += score[i][0] * 7
            else:
                sum += score[i][2] * 11 + score[i][0] * 7
        bitscore[i] = str(sum)
        if len(str(bitscore[i])) > 2:
            bitscore[i] = str(int(bitscore[i]) % 100)

    i = 0
    count = 0
    used = []
    while i < total_number:
        j = i + 1
        while j < total_number:
            if bitscore[i][0] == bitscore[j][0] and i % 2 == j % 2 and j not in used and i not in used:
                count += 1
                used.append(j)
            if j != total_number - 1:
                j += 1
            else:
                break
        used.append(i)
        i += 1

    print(count)


main()
