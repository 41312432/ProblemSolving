'''
문제
N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.

만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
(1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 37, N은 3k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.

출력
첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.
'''


N = int(input())

paper = [list(map(int ,input().split())) for _ in range(N)]

x, y, z = 0, 0, 0

def cut(paper):
    global x, y, z

    half_len = len(paper) // 2
    p1 = [paper[i][0: half_len] for i in range(half_len)]
    p2 = [paper[i][half_len:] for i in range(half_len)]
    p3 = [paper[half_len + i][0:half_len] for i in range(half_len)]
    p4 = [paper[half_len + i][half_len:] for i in range(half_len)]

    point_one = len(paper) // 3
    point_two = len(paper) * 2 // 3

    p1 = [paper[i][0: point_one] for i in range(point_one)]
    p2 = [paper[i][point_one: point_two] for i in range(point_one)]
    p3 = [paper[i][point_two:] for i in range(point_one)]
    p4 = [paper[point_one + i][0: point_one] for i in range(point_one)]
    p5 = [paper[point_one + i][point_one: point_two] for i in range(point_one)]
    p6 = [paper[point_one + i][point_two:] for i in range(point_one)]
    p7 = [paper[point_two + i][0: point_one] for i in range(point_one)]
    p8 = [paper[point_two + i][point_one: point_two] for i in range(point_one)]
    p9 = [paper[point_two + i][point_two:] for i in range(point_one)]

    if check(p1):
        cut(p1)
    if check(p2):
        cut(p2)
    if check(p3):
        cut(p3)
    if check(p4):
        cut(p4)
    if check(p5):
        cut(p5)
    if check(p6):
        cut(p6)
    if check(p7):
        cut(p7)
    if check(p8):
        cut(p8)
    if check(p9):
        cut(p9)

def check(paper):
    global x, y, z

    if len(paper) == 1:
        if paper[0] == [-1]:
            x += 1
        elif paper[0] == [0]:
            y += 1
        else:
            z += 1
    elif isHomo(paper) == '-1':
        x += 1
    elif isHomo(paper) == '0':
        y += 1
    elif isHomo(paper) == '1':
        z += 1
    else:
        return True
    return False

def isHomo(paper):
    temp = paper[0][0]
    for x in paper:
        for y in x:
            if y != temp:
                return False
    return str(temp)

if isHomo(paper) == '-1':
    x += 1
elif isHomo(paper) == '0':
    y += 1
elif isHomo(paper) == '1':
    z += 1
else:
    cut(paper)

print(x)
print(y)
print(z)
