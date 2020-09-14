
def main():
    holes_count = []

    number_holes = int(input())

    i = 0
    while i < number_holes:
        holes_count.append(i + 1)
        i += 1

    holes_value = list(map(int,input().split()))

    number_balls = int(input())

    ball_pos = [0] * number_balls

    ball_value = list(map(int,input().split()))

    i = 0
    while i < number_balls:
        j = number_holes - 1
        while j >= 0:
            if ball_value[i] <= holes_value[j] and holes_count[j] > 0:
                ball_pos[i] = j + 1
                holes_count[j] -= 1
                break
            j = j - 1
        i = i + 1

    i = 0
    while i < number_balls:
        print(ball_pos[i], end='')
        i = i + 1


main()

