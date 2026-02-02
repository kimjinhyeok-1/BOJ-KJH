import sys
input = sys.stdin.readline

m, d = map(int, input().split())

# 2007년은 1/1이 MON
days_before = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]  # 각 월 시작 전까지 누적 일수
ans = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

print(ans[(days_before[m-1] + (d-1)) % 7])
