def solution(num):
    answer = 0
    count = 0
    while True:
        if num == 1:
            return count
        elif count == 500:
            return -1
        elif num%2 == 0:
            num = num/2
        elif num%2 == 1:
            num = num*3+1
        count += 1
