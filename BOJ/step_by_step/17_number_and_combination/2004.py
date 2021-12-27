'''
문제
 
(
n
m
)
$n \choose m$의 끝자리 
0
$0$의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 
n
$n$, 
m
$m$ (
0
≤
m
≤
n
≤
2
,
000
,
000
,
000
$0 \le m \le n \le 2,000,000,000$, 
n
≠
0
$n \ne 0$)이 들어온다.

출력
첫째 줄에 
(
n
m
)
$n \choose m$의 끝자리 
0
$0$의 개수를 출력한다.
'''

n, m = map(int, input().split())

def count_num(N, num):
    count = 0
    div_num = num
    while(N >= div_num):
        count += N//div_num
        div_num *= num
    return count

print(min((count_num(n,2)-count_num((n-m),2)-count_num(m,2)), (count_num(n,5)-count_num((n-m),5)-count_num(m,5))))
