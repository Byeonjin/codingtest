point = str(input())
answer = 0
dv = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]

place = [int(ord(point[0]) - 96), int(point[1])]

for i in dv:
    if 1 <= place[0] + i[0] <= 8 and 1 <= place[1] + i[1] <= 8:
        answer +=1

    else:
        continue

print(answer)