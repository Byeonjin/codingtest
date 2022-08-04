n, k = list(map(int, input().split()))

result = 0

# while n != 1:
#     if n % k != 0:
#         n -= 1
#     else:
#         n //= k
#     result += 1

# n이 커지는 경우 연산시간이 늘어나기 때문에, 빼는 연산을 다음 k의 배수까지 한 번에 빼주는 코드

while n != 1:
    if n % k == 0:
        n //= k
        result += 1
    else:
        l = n // k
        result += n - l * k
        n = l * k

print(result)