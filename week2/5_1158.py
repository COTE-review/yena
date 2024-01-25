# 접근 방법
# 1. cnt를 1씩 늘리며 K가 될 때까지 큐에 삽입
# 2. cnt가 K라면 답안에 삽입
# 3. 큐가 빌 때까지 반복

import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))

queue = deque([num+1 for num in range(N)])

cnt = 1
answer_lst = []
while(len(queue)):
    if cnt == K:
        answer_lst.append(queue.popleft())
        cnt = 1
    elif cnt < K:
        queue.append(queue.popleft())
        cnt += 1

print('<', end = '')
answer_lst = list(map(str, answer_lst))
print(', '.join(answer_lst), end = '')
print('>')