n, m = list(map(int, input().split()))
info = list(map(int, input().split())) # x, y, direction
answer = 0

chplace = [info[0], info[1]]
direction = info[2]

map1 = []

for _ in range(n):
    tmp = []
    tmp = list(map(int, input().split()))
    map1.append(tmp)

dv = [[-1, 0], [0, 1], [1, 0], [0, -1]]

map1[chplace[0]][chplace[1]] = 2
answer +=1

while True:
    direction -= 1
    tmp_x = chplace[0] + dv[direction][0]
    tmp_y = chplace[1] + dv[direction][1]

    if map1[tmp_x][tmp_y] ==  0:
        map1[tmp_x][tmp_y] = 2
        chplace = [tmp_x, tmp_y]
        answer +=1


    if map1[chplace[0] - 1][chplace[1]] and map1[chplace[0] + 1][chplace[1]] and map1[chplace[0]][chplace[1] -1] and map1[chplace[0]][chplace[1] + 1]:
        if chplace[0] - dv[direction][0] == 1 or chplace[1] - dv[direction][1] == 1:
            break
        else:
            map1[tmp_x][tmp_y] = 2
            chplace = [tmp_x, tmp_y]
            answer += 1

print(answer)