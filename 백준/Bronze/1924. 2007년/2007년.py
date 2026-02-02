#1,3,5,7,8,10,12 -> 31일
#4,6,9,11 -> 30일
#2 -> 28일
import sys
input = sys.stdin.readline

month, day = map(int, input().split())
k = [0,30,58,89,119,150,180,211,242,272,303,333,364]
ans = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
total_day = k[month-1] + day

if month == 1:
    p = (total_day-1) % 7
    print(ans[p])
else:
    p = (total_day) % 7
    print(ans[p])