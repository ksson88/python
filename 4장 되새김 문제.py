print("""첫 번째 항의 값이 0이고 두 번째 항의 값이 1 일때,
이후에 이어지는 항들은
      이전의 두 항을 더한 값으로
      이루어지는 수열을 피보나치 수열이라고 한다.""")
print("0, 1, 1, 2, 3, 5, 8, 13, ...")
print("정수 n을 입력받았을때, n 이하까지의 피보나치 수열을 출력하는 함수를 작성해보자")

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1) # 이부분 틀림.

for i in range(10): # 이부분 다르게 작성함. 사용자 입력값을 받아서 출력하는 것으로 생각했음
    
    print(fib(i))




print("파일 읽고 쓰기")
print("""
sample.txt 파일을 읽어, 총합, 평균을 구한후,
평균값을 result.txt 라는 파일에 쓰는 프로그램을 작성해보자.
""")

f = open("sample.txt")
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score

average = total / len(lines)
print("average : ", average)
f = open("result.txt", 'w')
f.write(str(average)) ## 이부분 틀림.
f.close()
    
