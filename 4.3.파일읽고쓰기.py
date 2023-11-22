print("4.3. 파일 읽고 쓰기")

print("파일 생성하기")
f = open("새파일.txt", 'w') # 파이썬 내장함수 open
f.close()

# 파일객체 = open(파일이름, 파일열기모드)
# r, w, a : 읽기, 쓰기, 마지막에 내용 추가

#f = open("C:/doit/새파일.txt", 'w')
#f.close()


print("파일을 쓰기 모드로 열어 내용 쓰기")
f = open("새파일.txt", 'w')

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data) # 파일에 데이터를 출력하는 방법
f.close()


for i in range(1, 11):
    data = "%d 번째 줄입니다.\n" % i
    print(data) # 화면에 데이터를 출력하는 방법

    

print("파일을 읽는 여러 가지 방법 : .readline(), .readlines() ")

f = open("새파일.txt", 'r')
line = f.readline() # 파일의 첫 번째 줄을 읽는다.
print(line)
f.close()


f = open("새파일.txt", 'r')
while True:
    line = f.readline() 
    if not line: break
    print(line)
f.close()




while True:
    data = input()
    if not data: break
    print(data)



f = open("새파일.txt", 'r')
lines = f.readlines() # 파일의 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트를 리턴한다.
for line in lines:
    print(line)
f.close()

f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip() # 개행 문자를 제거한다.
    print(line)
f.close()


print("read 함수 사용하기")

f = open("새파일.txt", 'r')
data = f.read() # 내용 전체를 문자열로 리턴한다.
print(data) 
f.close()


print("파일 객체를 for 문과 함께 사용하기")
f = open("새파일.txt", 'r')
for line in f:
    print(line)
f.close()


print("파일에 새로운 내용 추가하기")

f = open("새파일.txt", 'a')
for i in range(11, 20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()


print("with 문과 함께 사용하기")

f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")


























