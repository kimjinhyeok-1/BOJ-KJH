import sys
input = sys.stdin.readline

n, m = map(int, input().split())

visited = [False] * (n + 1)
seq = []
out = []

def dfs(depth: int):
    if depth == m:
        out.append(" ".join(map(str, seq)))
        return

    for x in range(1, n + 1):
        if not visited[x]:
            visited[x] = True
            seq.append(x)
            dfs(depth + 1)
            seq.pop()
            visited[x] = False

dfs(0)
print("\n".join(out))
