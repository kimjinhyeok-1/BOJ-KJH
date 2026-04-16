import sys

def solve():
    n = int(sys.stdin.readline())
    # 인덱스 에러 방지를 위해 뒤에 여유 공간(0)을 추가합니다.
    factories = list(map(int, sys.stdin.readline().split())) + [0, 0]
    
    total_cost = 0
    
    for i in range(n):
        # Case 1: 두 번째 공장이 세 번째 공장보다 라면이 더 많은 경우
        # 세 번째 공장과 3개 묶음을 만들기 위해, 두 번째 공장의 여유분을 미리 2개 묶음으로 처리합니다.
        if factories[i+1] > factories[i+2]:
            # 두 번째와 세 번째의 차이만큼 혹은 현재 공장의 라면만큼 2개 묶음 구매
            count2 = min(factories[i], factories[i+1] - factories[i+2])
            total_cost += 5 * count2
            factories[i] -= count2
            factories[i+1] -= count2
            
            # 그 후 3개 묶음 구매
            count3 = min(factories[i], factories[i+1], factories[i+2])
            total_cost += 7 * count3
            factories[i] -= count3
            factories[i+1] -= count3
            factories[i+2] -= count3
            
        # Case 2: 일반적인 경우 (3개 묶음 -> 2개 묶음 순서)
        else:
            count3 = min(factories[i], factories[i+1], factories[i+2])
            total_cost += 7 * count3
            factories[i] -= count3
            factories[i+1] -= count3
            factories[i+2] -= count3
            
            count2 = min(factories[i], factories[i+1])
            total_cost += 5 * count2
            factories[i] -= count2
            factories[i+1] -= count2
            
        # Case 3: 남은 라면들은 각각 3원씩 주고 구매
        total_cost += 3 * factories[i]
        factories[i] = 0

    print(total_cost)

solve()