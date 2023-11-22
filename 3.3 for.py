print("\n" + "for문 기본" + "="*50)

testList = ['one', 'two', 'three']
for i in testList:
    print(i)

tuplesList = [(1,2), (3,4), (5,6)]
for (first, last) in tuplesList:
    print(first + last)


print("\n" + "for문 응용" + "="*50)
# 5명의 학생이 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다. 결과를 출력하라.
marks = [90, 25, 67, 45, 80]

number = 0

for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생 합격" % number)
    else:
        print("%d번 학생 불합격" % number)


print("\n" + "for문과 continue문" + "="*50)
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)



print("\n" + "for문과 range 함수" + "="*50)
a = range(10)
print(a)

a = range(1, 11)
print(a)

add = 0
for i in range(1, 11):
    add += i
print(add)


marks = [90, 25, 67, 45, 80]
print("range(len(marks) : ", range(len(marks)) )
      
# number = 0
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % (number + 1))


print("\n" + "for문과 range 구구단 " + "="*50)

for i in range(2, 10):
    for j in range(1, 10):
        print( i * j, end  = " ")
    print('')


print("\n" + "리스트 컴프리헨션(list comprehenshion) 사용하기 " + "="*50)
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)


a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)


a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# [표현식 for 항목 in 반복_가능_객체 if 조건문]

# [표현식 for 항목1 in 반복_가능_객체1 if 조건문1
#       for 항목2 in 반복_가능_객체2 if 조건문2
#       ...
#       for 항목n in 반복_가능_객체n if 조건문n]

result = [ x * y for x in range(2, 10) for y in range(1, 10)]
print(result)



































