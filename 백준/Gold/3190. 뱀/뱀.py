import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1  # 사과

l = int(input())
turns = {}
for _ in range(l):
    t, d = input().split()
    turns[int(t)] = d

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direction = 0
time = 0

snake = deque([(1, 1)])
snake_set = {(1, 1)}  # 몸 충돌 체크 빠르게 하려고 같이 사용

while True:
    time += 1

    head_x, head_y = snake[0]
    nx = head_x + dx[direction]
    ny = head_y + dy[direction]

    # 벽 충돌
    if not (1 <= nx <= n and 1 <= ny <= n):
        break

    # 몸 충돌
    if (nx, ny) in snake_set:
        break

    # 머리 이동
    snake.appendleft((nx, ny))
    snake_set.add((nx, ny))

    # 사과가 없으면 꼬리 이동
    if board[nx][ny] == 0:
        tail = snake.pop()
        snake_set.remove(tail)
    else:
        board[nx][ny] = 0  # 사과 먹음

    # 방향 전환
    if time in turns:
        if turns[time] == 'D':
            direction = (direction + 1) % 4
        else:  # 'L'
            direction = (direction - 1) % 4

print(time)