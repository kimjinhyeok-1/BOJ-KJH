def solution(phone_book):
    phone_set = set(phone_book)
    
    for number in phone_book:
        for i in range(1,len(number)):
            temp = number[:i]
            if temp in phone_set:
                return False
    
    return True