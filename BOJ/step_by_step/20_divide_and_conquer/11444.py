'''
문제
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 n번째 피보나치 수를 1,000,000,007으로 나눈 나머지를 출력한다.
'''

n = int(input())
p = 1000000007

def mul_matrix( matrix1, matrix2, p):
    result = [[0,0], [0,0]]

    for n in range(2):
        for k in range(2):
            for m in range(2):
                result[n][k] += matrix1[n][m] * matrix2[m][k]
            result[n][k] %= p
    
    return result

def square(n, matrix, p):
    if n == 1:
        return matrix
    elif n == 2:
        return mul_matrix(matrix, matrix, p)
    else:
        temp =  square( n//2, matrix, p)
        if n%2 == 0:
            return mul_matrix( temp, temp, p)
        else:
            return mul_matrix(mul_matrix( temp, temp, p), matrix, p) #2//B 제곱하고 그냥 matrix 한번 곱해주기

result = square(n, [[1, 1], [1, 0]], p)

print(result[0][1])