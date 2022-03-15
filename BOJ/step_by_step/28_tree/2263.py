'''
문제
n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다. 이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n(1 ≤ n ≤ 100,000)이 주어진다. 다음 줄에는 인오더를 나타내는 n개의 자연수가 주어지고, 그 다음 줄에는 같은 식으로 포스트오더가 주어진다.

출력
첫째 줄에 프리오더를 출력한다.
'''

n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0] * (n+1)

for i in range(n):
    position[inorder[i]] = i

def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    
    root = postorder[post_end]
    print(root, end=' ')

    left_count = position[root] - in_start
    right_count = in_end - position[root]

    preorder(in_start, position[root]-1, post_start, post_start+left_count-1)
    preorder(position[root]+1, in_end, post_end-right_count, post_end-1)

preorder(0, n-1, 0, n-1)
