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
            '''
            time = h + m + s
            if list(time).count("3") > 0:
                answer += 1
            '''
            # 위의 코드를 아래와 같이 줄일 수 있다. 그런데 내 코드도 직관성에서는 나쁘지 않은 것 같다.
            if '3' in str(i) + str(j) + str(k):
                answer += 1


print(answer)