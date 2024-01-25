# 접근 방법
# 1. 큐에서 dequeue 후 전체 max보다 작으면 enqueue, 같으면 pop
# 2. pop 할 때 count += 1
# 3. index -= 1 하다가 0일때 max와 같을 때까지

from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    Deq = deque(map(int, sys.stdin.readline().split()))
    index = M
    count = 0

    while(1):
        Max = max(Deq)
        doc = Deq.popleft()
        if doc < Max:
            Deq.append(doc)
            if index == 0: #찾는 문서가 뒤로 갔을 때
                index = len(Deq) - 1
            else: #찾는 문서를 앞 칸으로 옮길 때
                index -= 1
        else:
            count += 1
            if index == 0:
                break
            else:
                index -= 1

    print(count)
