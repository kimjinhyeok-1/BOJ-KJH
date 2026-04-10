import sys

# 입력 받기
word = sys.stdin.readline().strip()
results = []

# 단어를 세 부분으로 나누기 위한 이중 반복문
# i는 첫 번째 분할점, j는 두 번째 분할점
for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        # 1. 단어 나누기
        part1 = word[:i]
        part2 = word[i:j]
        part3 = word[j:]
        
        # 2. 각 부분 뒤집기 및 3. 합치기
        new_word = part1[::-1] + part2[::-1] + part3[::-1]
        
        # 결과 리스트에 추가
        results.append(new_word)

# 4. 사전순으로 정렬 후 가장 앞선 것 출력
results.sort()
print(results[0])