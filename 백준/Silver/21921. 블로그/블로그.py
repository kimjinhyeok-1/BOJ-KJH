import sys 
input = sys.stdin.readline

n,x = map(int, input().split())
visited = list(map(int, input().split()))
s = 0
end = x-1

u = 0
for t in visited:
   if t == 0: u+=1
   if u == n: 
      print('SAD')
      sys.exit(0)
ans = 1

max_v = sum(visited[s:end+1])
k = max_v
for _ in range(n - x):
    k = k - visited[s] + visited[end+1]
    if max_v == k:
        ans += 1
    elif max_v < k:
        max_v = k
        ans = 1
        
    s+=1
    end+=1
print(max_v)
print(ans)