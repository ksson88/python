# 리스트 인덱싱
a = [1, 2, 3]
print("a : ", a)

a = [1, 2, 3, ['a', 'b', 'c']]
print("a : ", a)
print("a[0] : ", a[0])
print("a[-1] : ", a[-1]) # -1은 마지막 요소 값['a', 'b', 'c']
print("a[-1][0] : ", a[-1][0])


print("======================================================================")
print("리스트 슬라이싱")
a = [1, 2, 3, 4, 5]
print("a : ", a)
print("a[0:2] : " , a[0:2]) 
b = a[:2]
print("b = a[:2] : ", b)
c = a[2:]
print("c = a[2:] : ", c)

print("======================================================================")
print("리스트 연산하기")
print("a : ", a)
print("b : ", b)
print("c : ", c)

print("리스트 더하기 : +")
print("b + c : ", b + c)


print("리스트 반복하기 : * ")
print("a * 3", a * 3)

print("리스트 길이 구하기 : len(a)")
print("len(a) : ", len(a))

print("리스트 수정과 삭제 : del a[1]")
print("a", a)
print("a[2] = 4")
a[2] = 4
print("a", a)

del a[2]
print("del a[2]")
print("a : ", a)


print("리스트 관련 함수 : append, sort, reverse, index, insert, remove, pop, count, extend, ")
print("리스트에 요소 추가하기")
print("a", a)
a.append(6)
print("a.append(4)")
print("a : ", a)
a.append([7, 8])
print("a : ", a)
print("a : ", a)

print("리스트 정렬")
a = [ 1, 4, 5, 2, 3]
print("a", a)
a.sort()
print("a.sort")
print("a", a)

a = ['a', 'c', 'b', 'd']
print("a", a)
a.sort()
print("a.sort()")
print("a", a)

print("a.reverse()")
a.reverse()
print("a:", a)

print("a.index('b') : ", a.index('b') )

print("a.insert(0, 'e')")
a.insert(0, 'e')
a.insert(0, 'e')
a.insert(0, 'e')
print("a :", a)

print("a.remove('e')")
a.remove('e')
print("a : ", a)
print("a.remove('e')")
a.remove('e')
print("a : ", a)


print("a.pop() : ", a.pop())

print("a : ", a)

print("a.count('a') : ", a.count('a'))

print("a.extend['f', 'g']")
a.extend(['f', 'g'])
print("a : ", a)
print("a += ['h', 'i']")
a += ['h', 'i']
print("a : ", a)

