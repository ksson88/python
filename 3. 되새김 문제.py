print("Q1. 다음 코드의 결과값은 무엇일까?")
'''
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
'''

print('shirt')

print("Q1. while 문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 작성해 보자.")

i = 0
while i < 6:
    i += 1
    if i < 6:
        print('*' * i)

        
print("""Q1.A 학급에 총 10명의 학생이 있다. 이 학생들은 중간고사 점수는 다음과 같다.
[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for 문을 이용하여 A학급의 평균 점수를 구해보자.
""")

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
print("range(len(A) : ", range(len(A)))

for students in range(len(A)):
    print("students", students)
    total += A[students]
    
average = total / len(A)

print(average)



