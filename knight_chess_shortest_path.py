def solution(src,dest):

    queue = []
    queue.append(src)
    
    visited = [0 for i in range(64)]
    visited[src] = 1

    prev = {}

    dr = [-16,-8,+8,+16,+16,+8,-8,-16]
    dc = [1,2,2,1,-1,-2,-2,-1]

    while len(queue) != 0:
        current_pos = queue[0]
        queue.pop(0)

        for i in range(0,8):

            next_pos = current_pos + dr[i] + dc[i]

            if next_pos > 63 :
                continue

            if visited[next_pos] == 1:
                continue

            if current_pos + dr[i] < 0 or current_pos + dr[i] > 63:
                continue

            if (current_pos % 8 ==0 and (dc[i] == -1 or dc[i] == -2)) or (current_pos % 8 == 7 and (dc[i] == 1 or dc[i] == 2)) or ( current_pos % 8 == 6 and dc[i] == 2) or (current_pos % 8 == 1 and dc[i] == -2):
                continue

            queue.append(next_pos)
            visited[next_pos] = 1
            prev[next_pos] = current_pos

    count = 0 
    at = dest
    path = []

    while at in prev:
        path.append(at)
        at =  prev[at]
        count = count + 1

    print(count)
    print(path)


solution(38,0)