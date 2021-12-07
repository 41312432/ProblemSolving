'''
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
'''

N = int(input())

sol = 0
board = [[0 for _ in range(N)]for _ in range(N)]

def arrange(index):
    row = index[0]
    col = index[1]

    diagonal = 1
    for i in range(row + 1, N):
        board[i][col] += 1
        if col - diagonal >= 0 and col - diagonal < N:
            board[i][col - diagonal] += 1
        if col + diagonal >= 0 and col + diagonal < N:
            board[i][col + diagonal] += 1
        diagonal += 1

def clear(index):
    row = index[0]
    col = index[1]

    diagonal = 1
    for i in range(row + 1, N):
        board[i][col] -= 1
        if col - diagonal >= 0 and col - diagonal < N:
            board[i][col - diagonal] -= 1
        if col + diagonal >= 0 and col + diagonal < N:
            board[i][col + diagonal] -= 1
        diagonal += 1

def dfs(depth):
    if depth == N:
        global sol
        sol += 1
        return

    for i in range(0, N):
        if board[depth][i]:
            continue
        arrange((depth, i))
        dfs(depth + 1)
        clear((depth, i))

dfs(0)

print(sol)