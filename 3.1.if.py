print("\n"+ "if" + "="*50 )
money = True
if money:
    print("택시 타고 가")
else:
    print("걸어가")

# 비교연산자 <, >, ==, !=, <=, =>
# and, or, not
# in, not in

# elif

print("\n"+ "elif" + "="*50 )

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시")
elif card:
    print("택시")
else:
    print("도보")

print("\n"+ "조건부 표현식"+ "="*50)
score = 100
message = "success" if score >= 60 else "failure"
print(message)
