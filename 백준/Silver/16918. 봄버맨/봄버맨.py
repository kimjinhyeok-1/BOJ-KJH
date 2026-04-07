import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def print_grid(arr):
    for row in arr:
        print("".join(row))

def explode(arr):
    # 일단 전부 폭탄으로 채운다
    result = [['O'] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                result[i][j] = '.'
                for dr, dc in dirs:
                    ni, nj = i + dr, j + dc
                    if 0 <= ni < R and 0 <= nj < C:
                        result[ni][nj] = '.'
    return result

if N == 1:
    print_grid(grid)
elif N % 2 == 0:
    print_grid([['O'] * C for _ in range(R)])
else:
    first = explode(grid)
    if N % 4 == 3:
        print_grid(first)
    else:  # N % 4 == 1, 단 N>1인 홀수
        second = explode(first)
        print_grid(second)