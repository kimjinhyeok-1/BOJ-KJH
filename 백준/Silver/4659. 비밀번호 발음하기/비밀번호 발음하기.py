def check(password):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    has_vowel = False
    v_cnt = 0
    c_cnt = 0
    prev = ''

    for ch in password:
        if ch in vowels:
            has_vowel = True
            v_cnt += 1
            c_cnt = 0
        else:
            c_cnt += 1
            v_cnt = 0

        if v_cnt >= 3 or c_cnt >= 3:
            return False

        if prev == ch and ch not in ('e', 'o'):
            return False

        prev = ch

    return has_vowel

while True:
    password = input().strip()
    if password == 'end':
        break

    if check(password):
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')