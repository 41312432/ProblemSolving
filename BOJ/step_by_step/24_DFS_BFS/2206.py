'''
문제
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
'''

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

m_map = [list(map(int, input().rstrip())) for _ in range(N)]
queue = deque()
visit = [[[0, 0] for _ in range(M)] for _ in range(N)]

if N == 1 and M == 1:
    print(1)
    exit(0)

queue.append((0,0,1))
visit[0][0][1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, breakable = queue.popleft()

    if x == N-1 and y == M-1:
        break

    for p in range(4):
        xx = x + dx[p]
        yy = y + dy[p]

        if 0 <= xx < N and 0 <= yy < M:
            if m_map[xx][yy] == 1 and breakable == 1:
                visit[xx][yy][0] = visit[x][y][1] + 1
                queue.append((xx, yy, 0))
            elif m_map[xx][yy] == 0 and visit[xx][yy][breakable] == 0:
                visit[xx][yy][breakable] = visit[x][y][breakable] + 1
                queue.append((xx, yy, breakable))

answer = max(visit[N-1][M-1])

if answer == 0:
    print(-1)
else:
    print(answer)
