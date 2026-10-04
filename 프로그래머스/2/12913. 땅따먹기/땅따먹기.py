def solution(land):
    answer = 0

    arr = land[0]
    
    for l in land[1:]:
        a,b,c,d = l
        arr = [
            a + max(arr[1],arr[2],arr[3]),
            b + max(arr[0],arr[2],arr[3]),
            c + max(arr[0],arr[1],arr[3]),
            d + max(arr[0],arr[1],arr[2])
        ]

    answer = max(arr)

    return answer