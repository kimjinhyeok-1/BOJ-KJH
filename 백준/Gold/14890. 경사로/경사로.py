"""
check 함수를 만들어서 함수 파라미터 값으로 하나의 줄을 입력
줄이 지나갈 수 있는 줄인지 검사하는게 check 함수
만약 지나갈 수 있으면 True 반환해서 정답 1 올리기

처음 값을 저장을 한 상태에서 다음 값이랑 diff(다음 값 - 현재 값)를 본다.
1. 차이가 0인 경우 
    continue
2. 차이가 1인 경우(오르막길)
    올라가기 위한 경사로를 놓을 수 있나?
    1. 그 전 L개가 범위 안에 들어오는지
    2. 들어온다면 그 전 L개의 값이 전부 같은지
    3. 이미 경사로를 놓은 자리는 아닌지
3. 차이가 -1인 경우(내리막길)
4. 그 외라면 전부 break하고 불가능 표시
"""
import sys
input = sys.stdin.readline
N, L = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

answer = 0

def check(line):
    used = [False] * N
    for i in range(1, len(line)):
        past = line[i-1]
        current = line[i]
        diff = current - past
        if diff == 0:
            continue
        elif diff == 1:
            for j in range(i-L,i):
                if j < 0 or N <= j:
                    return False
                if used[j]:
                    return False
                if line[j] != past:
                    return False
            for j in range(i-L, i):
                used[j] = True
        elif diff == -1:
            for j in range(i, i+L):
                if j < 0 or N <= j:
                    return False
                if used[j]:
                    return False
                if line[j] != current:
                    return False
            for j in range(i, i+L):
                used[j] = True
        else:
            return False
    return True

for r in range(N):
    if check(grid[r]):
        answer += 1

for c in range(N):
    line = [grid[r][c] for r in range(N)]
    if check(line):
        answer += 1

print(answer)