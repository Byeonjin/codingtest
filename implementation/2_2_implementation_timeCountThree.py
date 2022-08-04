n = int(input())

answer = 0

time = ""
h = ""
m = ""
s = ""

for i in range(0, n + 1):
    h = str(i)
    for j in range(0, 60):
        m = str(j)
        for k in range(0, 60):
            s = str(k)
            time = h + m + s
            if list(time).count("3") > 0:
                answer += 1

print(answer)