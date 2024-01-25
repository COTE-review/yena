# 접근 방법
# 1. 찾는 대상이 되는 리스트를 작은 순으로 정렬
# 2. 정렬된 리스트를 반을 나누고, 찾으려는 숫자가 가운데 보다 작으면 앞쪽에서 찾고 크면 뒤쪽에서 찾음

import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for m in M_list:
    left = 0
    right = N-1

    while left <= right:
        mid = (left + right) // 2
        if m > N_list[mid]:
            left = mid + 1
        elif m < N_list[mid]:
            right = mid - 1
        else: 
            left = mid
            right = mid
            break
    
    if left == mid and right == mid:
        print(1)
    else:
        print(0)