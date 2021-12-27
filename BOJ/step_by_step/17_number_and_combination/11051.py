'''
문제
자연수 
N
\(N\)과 정수 
K
\(K\)가 주어졌을 때 이항 계수 
(
N
K
)
\(\binom{N}{K}\)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 
N
\(N\)과 
K
\(K\)가 주어진다. (1 ≤ 
N
\(N\) ≤ 1,000, 0 ≤ 
K
\(K\) ≤ 
N
\(N\))

출력
 
(
N
K
)
\(\binom{N}{K}\)를 10,007로 나눈 나머지를 출력한다.
'''

from math import comb

N, K = map(int, input().split())

print(comb(N, K) % 10007)