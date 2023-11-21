print(" Q1. (1,2,3) 이라는 튜플에 4라는 값을 추가하여 (1,2,3,4)처럼 만들어 출력해 보자")

tuple1 = (1,2,3)
tuple1 += (4, )
print(tuple1)


print(" Q2. 딕셔너리 a에서 'B'에 해당되는 값을 추출하고 삭제해 보자. ")
a = {'A':90, 'B':80, 'C':70}
# print(a)
# print(a.keys())
# print(a.values())
# print(a.items())
# print(a.get('B'))
#print("a.values('B')", a.values('B'))
result = a.pop('B')
print(a)
print(result)


print(" Q3. a 리스트에서 중복된 숫자들을 제거해 보자 ")

a = [  3, 3, 3, 2, 2, 4, 4, 5, 1, 1, 1]
aSet = set(a)
print(aSet)
b = list(aSet)

print(b)


print(" Q4. 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. \n아래와 같이 a, b 변수를 선언한 후 a의 첫 번째 요소 값을 변경하면 b의 값은 어떻게 될까? \n그리고 이런 결과가 나오는 이유에 대해 설명해 보자.")
a = b = [1,2,3]
a[1] = 4
print(b)

# [1,4,3]이 출력된다. a와 b는 동일한 [1,2,3] 리스트 객체를 가리키고 있다.
