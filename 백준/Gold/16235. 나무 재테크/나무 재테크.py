import sys
from collections import deque

input = sys.stdin.readline

# N: 땅 크기, M: 초기 나무 개수, K: 목표 년도
n, m, k = map(int, input().split())

# 매년 추가되는 양분의 양 (A 배열)
a = [list(map(int, input().split())) for _ in range(n)]

# 현재 땅의 양분 상태 (초기값은 모두 5)
food = [[5] * n for _ in range(n)]

# 각 칸에 있는 나무들의 나이를 저장할 2차원 리스트 (내부는 deque로 관리)
trees = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

# 가을에 번식할 때 사용하는 인접 8방향 좌표
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(k):
    # --- 봄 & 여름 ---
    for r in range(n):
        for c in range(n):
            if not trees[r][c]:
                continue
            
            new_trees = deque()
            dead_food = 0
            
            # 봄: 어린 나무부터 양분 섭취
            # (새로운 나무는 항상 뒤에 추가되므로 나이순 정렬 필요 없음)
            for age in trees[r][c]:
                if food[r][c] >= age:
                    food[r][c] -= age
                    new_trees.append(age + 1)
                else:
                    # 여름: 죽은 나무가 양분이 됨
                    dead_food += age // 2
            
            trees[r][c] = new_trees
            food[r][c] += dead_food

    # --- 가을 & 겨울 ---
    for r in range(n):
        for c in range(n):
            # 가을: 나무 번식
            for age in trees[r][c]:
                if age % 5 == 0:
                    for i in range(8):
                        nr, nc = r + dx[i], c + dy[i]
                        if 0 <= nr < n and 0 <= nc < n:
                            # 번식된 나무는 나이가 1이므로 가장 앞에 추가 (어린 순서 유지)
                            trees[nr][nc].appendleft(1)
            
            # 겨울: 땅에 양분 추가
            food[r][c] += a[r][c]

# 최종 살아남은 나무 개수 계산
answer = 0
for r in range(n):
    for c in range(n):
        answer += len(trees[r][c])

print(answer)