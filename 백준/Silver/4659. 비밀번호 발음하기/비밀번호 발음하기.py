import sys
input = sys.stdin.readline

passwords = []
m = {'a','e','i','o','u'}
while True:
    x = input().strip()
    if x == 'end':
        break
    passwords.append(x)

for password in passwords:
    ok = True
    has_m = False
    m_count = 0
    j_count = 0
    prev = ''

    for ch in password:
        # 모음인 경우에는 모음 가지기 성공 + 모음 카운트 하나 올리기 + 자음 카운트 0으로 초기화
        # 자음인 경우에는 반대로 
        if ch in m:
            has_m = True
            m_count += 1
            j_count = 0
        else:
            j_count += 1
            m_count = 0

        # 모음이나 자음 카운트가 3이상인 경우 ok는 False
        if j_count >= 3 or m_count >= 3:
            ok = False
        
        # 같은 글자가 왔는데 해당 글자가 o, e가 아닌 경우 ok는 False
        if prev == ch and ch not in ('o','e'):
            ok = False

        # 이전 글자 초기화
        prev = ch
    if has_m and ok:
        print('<' + password + '>' + ' is acceptable.')
    else:
        print('<' + password + '>' + ' is not acceptable.')