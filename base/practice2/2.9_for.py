min, max = input().split()
input_num = list(map(int, input().split()))
for i in input_num:
    if i == -999:
        break
    elif i<int(min) or i>int(max):
        print("Alert!")
        break
    else:
        print("Nothing to report")
