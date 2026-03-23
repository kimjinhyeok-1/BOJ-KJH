def solution(i, j, k):
    ans = "".join([str(num) for num in range(i,j+1)])
    return list(ans).count(str(k))