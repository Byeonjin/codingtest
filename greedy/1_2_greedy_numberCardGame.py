n, m = list(map(int, input().split()))
tmp = []
for _ in range(n):
    tmp.append(min(list(map(int, input().split()))))

print(max(tmp))
