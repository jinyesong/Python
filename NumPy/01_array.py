import numpy as np

ar = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#print(type(ar))

answer = []
for di in ar:
    answer.append(2 * di)

#print(answer)

c = np.array([[0, 1, 2], [3, 4, 5]])  # 2 x 3 array

#print(len(c)) #행의 갯수
#print(len(c[0])) #열의 갯수

a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])

print(a[0, :])  # 첫번째 행 전체
print(a[:, 1])  # 두번째 열 전체
print(a[1, 1:])  # 두번째 행의 두번째 열부터 끝열까지