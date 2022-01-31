'''
문제
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다. 

출력
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.
'''

#DFS던 BFS던 그래프를 다 탐색하는건 좋은데... 이 방향으로 탐색했을때는 칠할 수 있는데 저 방향으로 탐색했을때는 못칠하는 경우는? 생각해보니까 이 방향으로 모순이면 저 방향으로도 모순이네
#그래프가 연결 안되어있을수도있고... 결국 모든 노드에서 시작하는 코드를 추가해야함

from collections import deque
import sys
input = sys.stdin.readline

def BFS(v):
    visit[v] = 1
    queue = deque()
    queue.append(v)
    
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visit[i]==0:
                visit[i] = -visit[x]
                queue.append(i)
            else:
                if visit[i] == visit[x]:
                    return False
    return True


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    visit = [0]*(V+1)
    is_bipartite = True

    for _ in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    for i in range(1, V+1):
        if visit[i] == 0:
            if not BFS(i):
                is_bipartite = False
                break
            
    print('YES' if is_bipartite == True else 'NO')