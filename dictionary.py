# 딕셔너리는 key와 value를 한쌍으로 가지는 자료형을 말한다.
# 리스트는 [] 대괄호, 튜플은 () 소괄호 , 딕셔너리는 {} 중괄호

dictionary = {'name' : '기석', 'phone' : '010-1111-2222', 'birth' : '0607' }
print("dictionary = ", dictionary)


a = { 1:'hi'}
print("a : ", a)
a = {'a': [1, 2, 3]}
print("a : ", a)


print("딕셔너리 쌍 추가, 삭제하기")

a = {1: 'a'}
print('a : ', a)
print("a[2] = 'b'")
a[2] = 'b'
print('a : ', a)
del a[2]
print('a : ', a)


print("딕셔너리 사용하는 방법 : name = { key : value, key : value ... }, name['key']")

grade = {'pey' : 10, 'julliet' : 99 }
print("grade = {'pey' : 10, 'julliet' : 99 }")
print("grade['pey']", grade['pey'])
print("grade['julliet']", grade['julliet'])

print("dictionary['name'] = ", dictionary['name'])


test1 = [[1,4,5], 2, 3, 4]
test2 = ([1,2,3], 2, 3, 4)
test3 = {1 : 100, 2 : 200, 3 : 300, 4 : 400}
print("test1", test1)
print("test2", test2)
print("test3", test3)

print("============= 딕셔너리 관련 함수 : .keys(), .values(), .items(), .clear(), .get('key'), 'key' in dictionary =============")
print("============= dictionary key list 출력 =============")
print("dictionary.keys() = ", dictionary.keys())

for key in dictionary.keys():
    print(key)

print("============= dictionary values list 출력 : .values() =============")

print("dictionary.values() = ", dictionary.values())


print("============== key, value 출력 : .items()  =================")
print("dictionary.items()", dictionary.items())

print("============== 모두 지우기: .clear()  =================")
dictionary.clear()
print("dictionary.clear()", dictionary)

print("============== key로 value 얻기: .get(key)  =================")
dictionary = {'name' : '기석', 'phone' : '010-1111-2222', 'birth' : '0607' }
print("dictionary.get('name') : ", dictionary.get('name'))

print("============== key가 dictionary 안에 있는지 확인  =================")
print("'phone' in dictionary : ", 'phone' in dictionary)
