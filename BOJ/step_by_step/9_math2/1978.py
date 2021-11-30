'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
'''

def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

prime_numbers = prime_list(1000)

N = int(input())
numbers = set(map(int, input().split()))

print(len((set(prime_numbers) & numbers)))

'''
    한편, 에라토스테네스의 체를 이용해 1~n까지의 소수를 알고 싶다면, n까지 모든 수의 배수를 다 나눠 볼 필요는 없다. 만약 n보다 작은 어떤 수 m이 
m
=
a
b
m=ab라면 
a
a와 
b
b 중 적어도 하나는 
n
n
​	
 이하이다. 즉 n보다 작은 합성수 m은 
n
n
​	
 보다 작은 수의 배수만 체크해도 전부 지워진다는 의미이므로, 
n
n
​	
  이하의 수의 배수만 지우면 된다.
  '''