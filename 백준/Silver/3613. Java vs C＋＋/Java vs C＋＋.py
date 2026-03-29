import sys
input = sys.stdin.readline
'''
java: 첫글자는 소문자 대문자도 사용 
C++ : 소문자만 사용, 구분할때 '_' 들어감
둘다 아닌 경우: 
    1. 첫글자가 대문자인 경우
    2. '_'도 있는데 대문자도 있는 경우
    3. '_'가 맨 앞에 존재하는 경우
    4. '_' 가 두번 연속 나타난 경우
'''
s = input().strip()

if s[0].isupper() or ('_' in s and not s.islower()) or s[0] == '_' or '__' in s or s[-1] == '_':
    print("Error!")
    sys.exit()

if '_' in s:
    parts = s.split('_')
    ans = parts[0]
    for part in parts[1:]:
        ans += part[0].upper() + part[1:]
    print(ans)
else:
    ans = ''
    for ch in s:
        if ch.isupper():
            ans += '_' + ch.lower()
        else:
            ans += ch
    print(ans)