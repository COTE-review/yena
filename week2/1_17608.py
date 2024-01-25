# 접근 방법
# 1. 제일 오른쪽 부터 기준으로 하고 그 다음 오른쪽부터와 차례로 비교
# 2. 기준보다 크면 카운드 +1하고 기준을 업데이트

import sys

N = int(sys.stdin.readline())
stack = list()

for _ in range(N):
    stack.append(int(sys.stdin.readline()))

test_length = stack.pop()
cnt = 1

for _ in range(len(stack)):
    top  = stack.pop()
    if  top > test_length:
        cnt += 1
        test_length = top

print(cnt)