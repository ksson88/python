print("변수 선언 방식")
a = 1
b = "python"
c = [1,2,3]
print("a = 1")
print('''b = "python"''')
print("c = [1,2,3]")

# 파이썬은 변수를 만들 때 자료형의 타입을 지정하지 않는다.
# 변수에 저장된 값을 스스로 판단한여 자료형의 타입을 지정한다.
print("=========================================================")

a = [1, 2, 3]
print("a : ", a)
print("a 변수가 가리키는 메모리 주소값")
print("id(a) : ", id(a))
x = a
print("x = a")
print("id(x) = ", id(x))

print("a is x : ", a is x)
print("a", a)
print("a[1] = 4")
a[1] = 4
print("a", a)
print("x", x)

print(" [:] 이용하기 : a변수가 가리키는 리스트를 복사")
a = [1, 2, 3]
print("a", a)
b = a[:]
a[1] = 4
print("a : ", a)
print("b = a[:]", b)

print("copy 모듈 이용하기 : from copy import copy : a 변수가 가리키는 값을 복사")
from copy import copy
a = [1,2,3]
b = copy(a)
print(b)
print(b is a)

a, b = 'python', 'life'
print(a) # python
print(b) # life

[a, b] = ['python', 'life']
print(a) # python
print(b) # life

a = b = 'python'
print(a)
print(b)

a = 3
b = 5
a, b = b, a
print(a)
print(b)
