num = 12345

list_num = list(str(num))
print(list_num)

sum = 0
for i in list_num:
    sum += int(i)

print(sum)