n, m , k = list(map(int, input().split()))
li = list(map(int, input().split()))
answer = 0

li.sort(reverse= True)

for i in range(1, m + 1):
    if i % (k + 1) == 0:
        answer += li[1]
        continue

    answer += li[0]

print(answer)
