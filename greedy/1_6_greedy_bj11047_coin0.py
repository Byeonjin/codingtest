'''
백준 11047 - 동전 0

문제
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

출력
첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

주소: https://www.acmicpc.net/problem/11047
'''

n, k = list(map(int, input().split()))
answer = 0
value_list = []

for _ in range(n):
    value_list.append(int(input()))

value_list.sort(reverse=True)

for i in value_list:
    if k == 0:
        break

    tmp = 0
    tmp = k // i

    k -= i * tmp
    answer += tmp

print(answer)

'''
greedy 알고리즘의 대표적인 문제!
입력조건 중 (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수) 이 조건이 성립하기 때문에,
큰 화폐 순서로 최대한 빼주며 내려가는 식으로 문제를 풀 수 있다.
2000원을 1000 500 100 50 10 5 1 7가지 종류의 코인을 이용해 거슬러 준다면, 1000원짜리 동전 하나로 2번 거슬러 주는게 제일 동전 수를 줄일 수 있을 것이다.
'''