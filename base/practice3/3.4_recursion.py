def sumOfDigits(num):
    if len(num) == 1:
        return int(num)
    else:
        return int(num[len(num)-1]) + sumOfDigits(num[:len(num)-1])

print(sumOfDigits(input()))