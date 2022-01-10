'''
문제
크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

입력
첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)

둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.
'''

N, B = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

def mul_matrix(N, matrix1, matrix2):
    result = [[0 for _ in range(N)] for _ in range(N)]

    for n in range(N):
        for k in range(N):
            for m in range(N):
                result[n][k] += matrix1[n][m] * matrix2[m][k]
            result[n][k] %= 1000
    
    return result

def divide(N, B, matrix):
    if B == 1:
        return matrix
    elif B == 2:
        return mul_matrix(N, matrix, matrix)
    else:
        temp =  divide(N, B//2, matrix)
        if B%2 == 0:
            return mul_matrix(N, temp, temp)
        else:
            return mul_matrix(N, mul_matrix(N, temp, temp), matrix) #2//B 제곱하고 그냥 matrix 한번 곱해주기

result = divide(N, B, A)

for row in result:
    for num in row:
        print(num%1000, end = ' ')
    print()


    
