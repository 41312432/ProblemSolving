'''
문제
백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 백준이가 외치는 정수의 개수 N이 주어진다. N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다. 그 다음 N줄에 걸쳐서 백준이가 외치는 정수가 차례대로 주어진다. 정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

출력
한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력한다.
'''

# import heapq
# import sys
# input = sys.stdin.readline

# N = int(input())

# heap = []

# for _ in range(N):
#     heapq.heappush(heap, int(input()))

#     heap_len = len(heap)

#     temp=[]
#     for _ in range((heap_len-1) // 2):
#         temp.append(heapq.heappop(heap))
    
#     if heap_len % 2 == 0:
#         a = heapq.heappop(heap)
#         b = heapq.heappop(heap)
#         print(min(a, b))
#         heapq.heappush(heap, a)
#         heapq.heappush(heap, b)
#     else:
#         a = heapq.heappop(heap)
#         print(a)
#         heapq.heappush(heap, a)

#     for num in temp:
#         heapq.heappush(heap, num)

import sys
import heapq
input = sys.stdin.readline

N = int(input())

leftHeap = []
rightHeap = []
answer = []

for _ in range(N):
    input_num = int(input())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, (-input_num, input_num))
    else:
        heapq.heappush(rightHeap, (input_num, input_num))
    
    if rightHeap and leftHeap[0][1] > rightHeap[0][1]:
        right_min = heapq.heappop(rightHeap)[1]
        left_max = heapq.heappop(leftHeap)[1]

        heapq.heappush(leftHeap, (-right_min, right_min))
        heapq.heappush(rightHeap, (left_max, left_max))
    
    answer.append(leftHeap[0][1])

for answer in answer:
    print(answer)