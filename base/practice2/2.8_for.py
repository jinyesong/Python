dataList = list(range(2,26))

for i in dataList:
    for j in dataList:
        if j!=i and j%i == 0:
            dataList.remove(j)
print(dataList)
