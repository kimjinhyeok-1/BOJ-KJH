import sys
from collections import deque
input = sys.stdin.readline

# (층, 행, 열)
d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

while True:
    # 빈 줄 건너뛰고 L R C 읽기
    line = input().strip()
    while line == "":
        line = input().strip()

    L, R, C = map(int, line.split())

    if L == 0 and R == 0 and C == 0:
        break

    grid = []
    dist = [[[-1] * C for _ in range(R)] for _ in range(L)]

    start = None
    end = None

    for l in range(L):
        floor = [list(input().strip()) for _ in range(R)]
        grid.append(floor)

        for x in range(R):
            for y in range(C):
                if grid[l][x][y] == 'S':
                    start = (l, x, y)
                elif grid[l][x][y] == 'E':
                    end = (l, x, y)

        if l != L - 1:
            input()  # 층 사이 빈 줄 제거

    q = deque([start])
    sl, sx, sy = start
    dist[sl][sx][sy] = 0

    escaped = False

    while q:
        l, x, y = q.popleft()

        if (l, x, y) == end:
            print(f"Escaped in {dist[l][x][y]} minute(s).")
            escaped = True
            break

        for dl, dx, dy in d:
            nl, nx, ny = l + dl, x + dx, y + dy

            if 0 <= nl < L and 0 <= nx < R and 0 <= ny < C:
                if dist[nl][nx][ny] == -1 and grid[nl][nx][ny] != '#':
                    dist[nl][nx][ny] = dist[l][x][y] + 1
                    q.append((nl, nx, ny))

    if not escaped:
        print("Trapped!")