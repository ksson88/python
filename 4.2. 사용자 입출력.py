print("사용자 입력 활용하기")

a = input()


print("프롬프트를 띄워 사용자 입력받기")

# input("안내_문구")

number = input("숫자를 입력하세요: ")


print("print 자세히 알기")

print("큰따옴표로 둘러싸인 문자열은 + 연산과 동일하다")

print("life" "is" "too short")  # 1번
print("life"+"is"+"too short")  # 2번


print("문자열 띄어쓰기는 쉼표로 한다")
print("life", "is", "too short")


print("한 줄에 결괏값 출력하기")
for i in range(10):
    print(i, end=' ')

# end 매개변수의 초깃값은 줄바꿈(\n) 문자이다.
