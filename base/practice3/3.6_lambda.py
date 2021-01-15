print((lambda x,y: x+y)(10,20))

#리스트로부터 원소를 하나씩 꺼내 함수 적용
print(list(map(lambda x: x**2, range(5))))

from functools import reduce
#순서형 자료의 원소들 함수 누적 적용
print(reduce(lambda x,y: x+y, [0,1,2,3,4]))
print(reduce(lambda x,y:y+x, "abcde"))

#리스트의 원소들을 함수에 적용시켜 결과가 참인 것들로 새 리스트 생성
print(list(filter(lambda x:x<5, range(10))))