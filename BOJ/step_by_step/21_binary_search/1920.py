'''
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
'''

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
X = list(map(int, input().split()))

def binary_search(arr, start, end, target):
    if start > end:
        print(0)
    else:
        mid = ((end-start) // 2) + start
        if target == arr[mid]:
            print(1)
        elif arr[mid] > target:
            binary_search(arr, start, mid-1, target)
        else:
            binary_search(arr, mid+1, end, target)

for x in X:
    binary_search(A, 0, len(A)-1, x)