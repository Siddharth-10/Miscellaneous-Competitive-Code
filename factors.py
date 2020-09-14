def main():
    number_testcases = int(input())
    testcase = list(map(int,input().split()))


    for i in testcase:
        factor = [i]
        j = 1
        while j * j <= i:
            if i % j == 0 and j:
                factor.append(j)
                if i//j != i and i//j not in factor:
                    factor.append(i//j)
            j += 1

        factor.sort()
        print(" ".join([str(d) for d in factor]))

main()