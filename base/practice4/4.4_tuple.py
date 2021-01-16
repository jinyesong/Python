# 두개 이상 인자 처리
def magu_print(x, y, *rest):       
    print(x, y, rest)

magu_print(1,2,3,5,6,7,9,10)

#원소를 하나만 가진 튜플
one = 5, #원소 뒤 콤마
print(one)

#튜플은 리스트와 다르게 원소값을 직접 바꿀 수 없다
#오려붙이기
p = (1,2,3)
q = p[:1] + (5,) + p[2:]
print(q)