#요약하면, 함수(function)는 독립적인 코드 블록이고, 메소드는 객체에 속한 함수입니다.

def add(a, b):
    return a + b
a = 3
b = 4
c = add(a, b)
print(c)


print("매개변수와 인수")
def add(a, b):      # a, b는 매개변수
    return a + b
print(add(3, 4))     # 3, 4는 인수= 입력값 = 파라미터

print("일반적인 함수")
def add(a, b):
    result = a + b
    return result
a = add(10, 22)
print(a)

print("입력값이 없는 함수")
def say():
    return 'Hi'

a = say()
print(a)

print("리턴값이 없는 함수")
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add(3, 10)

print("입력값도, 리턴값도 없는 함수")
def say():
    print('hi')

say()

print("매개변수를 지정하여 호출하기")
def sub(a, b):
    return a - b

result = sub(a=7, b=3)
print(result)

result = sub(b=7, a=3)
print(result)

print("입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?")

""" def 함수_이름(*매개변수):
        수행할_문장
        ...
"""

print("여러 개의 입력값을 받는 함수 만들기")

def add_many(*args):
    result = 0
    for i in args:
        result += i # *args에 입력 받은 모든 값을 더한다.
    return result

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)




def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result


result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)


print("키워드 매개변수, kwargs")

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', are=3)


print("함수의 리턴값은 언제나 하나이다")

def add_and_mul(a, b):
    return a+b, a*b

result = add_and_mul(3, 4)
print(result) # 7, 12

result1, result2 = add_and_mul(3, 4)

print("매개변수에 초깃값 미리 설정하기")

def say_myself(name, age, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")


say_myself("박응용", 27)


say_myself("박응용", 27, True)


say_myself("박응선", 27, False)




print("함수 안에서 선언한 변수의 효력 범위")



a = 1
def vartest(a):
    a = a +1

vartest(a)
print(a) # 1


print("함수 안에서 함수 밖의 변수를 변경하는 방법: return, global, lambda")
print("return")
a = 1
def vartest(x):
    x += 1
    return x

a = vartest(a)
print(a)


print("global")
a = 1
def vartest():
    global a
    a += 1

vartest()
print(a)


print("lambda")
# lambda는 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을 한다. 보통 함수를 한 줄로 간결하게 만들때 사용한다. def를 사용할 정도로 복잡하지 않거나, def를 사용할 수 없는 곳에서 사용된다.

def def_add(a, b):
    return a + b

lambda_add =lambda a, b: a + b

print(def_add(10, 11))

print(lambda_add(22, 33))















































