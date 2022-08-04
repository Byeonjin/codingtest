n = int(input())
plan = list(map(str, input().split()))

d_vec = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}

point = [1, 1]

for i in plan:
    if (point[0] == 1 and i == "U") or (point[0] == n and i == "D") or (point[1] == 1 and i == "L") or (point[1] == n and i == "R"):
        continue
    point[0] += d_vec[i][0]
    point[1] += d_vec[i][1]

print(point)
