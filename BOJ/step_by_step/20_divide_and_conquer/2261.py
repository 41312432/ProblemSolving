'''
문제
2차원 평면상에 n개의 점이 주어졌을 때, 이 점들 중 가장 가까운 두 점을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 n(2 ≤ n ≤ 100,000)이 주어진다. 다음 n개의 줄에는 차례로 각 점의 x, y좌표가 주어진다. 각각의 좌표는 절댓값이 10,000을 넘지 않는 정수이다. 여러 점이 같은 좌표를 가질 수도 있다.

출력
첫째 줄에 가장 가까운 두 점의 거리의 제곱을 출력한다.
'''

import sys
input = sys.stdin.readline

n = int(input())

coords = [list(map(int, input().split())) for _ in range(n)]

coords.sort()

def get_square_distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def get_closest(start_point, end_point):
    if start_point == end_point:
        return float('inf')
    
    if end_point-start_point == 1:
        return get_square_distance(coords[start_point], coords[end_point])

    mid_point = (start_point+end_point)//2 
    closest_distance = min(get_closest(start_point, mid_point), get_closest(mid_point + 1, end_point))

    target_coords = []
    for i in range(start_point, end_point + 1):
        if (coords[mid_point][0] - coords[i][0]) ** 2 < closest_distance:
            target_coords.append(coords[i])

    target_coords.sort(key = lambda x: x[1])

    for i in range(len(target_coords)-1):
        for j in range(i+1, len(target_coords)):
            if (target_coords[i][1] - target_coords[j][1]) ** 2 < closest_distance:
                closest_distance = min(closest_distance, get_square_distance(target_coords[i], target_coords[j]))
            else:
                break
    
    return closest_distance

print(get_closest(0, n-1))