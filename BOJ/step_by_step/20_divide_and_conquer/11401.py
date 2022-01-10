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
\(\binom{N}{K}\)를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 
N
\(N\)과 
K
\(K\)가 주어진다. (1 ≤ 
N
\(N\) ≤ 4,000,000, 0 ≤ 
K
\(K\) ≤ 
N
\(N\))

출력
 
(
N
K
)
\(\binom{N}{K}\)를 1,000,000,007로 나눈 나머지를 출력한다.
'''

# import sys
# input=sys.stdin.readline

# n, k=map(int, input().split())
# fac=[1, 1]; mod=1000000007
# for i in range(2, n+1):
#     fac.append((fac[-1]*i)%mod)

# def modPow(a, n, p):
#     if n==0: return 1
#     res=modPow(a*a%p, n//2, p)
#     if n&1: res=res*a%p
#     return res

# print(fac[n]*modPow(fac[k]*fac[n-k], mod-2, mod)%mod)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
p = 1000000007

def factorial(N, modulo):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % modulo
    return n

def pow(base, exponent, modulo):
    if exponent == 1:
        return base % modulo

    temp = pow(base, exponent // 2, modulo)

    if exponent % 2 == 1:
        return (temp**2*base) % modulo
    else:
        return (temp**2) % modulo

top = factorial(N, p)
bot = factorial(N-K, p) * factorial(K, p) % p

print((top * pow(bot, p-2, p)) % p)