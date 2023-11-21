print("=============집합 자료형 : set(list), set(string)============")
print("set([1, 2, 3]) : ", set([1, 2, 3]))

print(''' set("hello") : ''', set("hello"))
# 중복을 허용하지 않는다.
# 순서가 없다.

print("============= 교집합, 합집합, 차집합 구하기 ============")

set1 = set([1,2,3,4,5,6])
set2 = set([4,5,6,7,8,9])
print("set1 : ", set1)
print("set2 : ", set2)


print("============= 교집합 : set1 & set2 ============")
print("set1 & set2 : ", set1 & set2)


print("============= 합집합 : set1 | set2 또는 set1.union(set2)============")
print("set1 | set2 : ", set1 | set2)

print("set1.union(set2) : ", set1.union(set2))

print("============= 차집합 : set1 - set2 ============")
print("set1 - set2 : ", set1 - set2)
print("set1.difference(set2)", set1.difference(set2))


print("============= 집합 자료형 관련 함수 : set.add(object), set.update(objects), set.remove(object) ============")
set1 = set([1, 2, 3])
print("set1 : ", set1)

print("set1.add(4)")
set1.add(4)
print("set1 : ", set1)

print("set1.update([5,6,7,8])")
set1.update([5,6,7,8])
print("set1 : ", set1)
print("set1.remove(1)")
set1.remove(1)
print("set1 : ", set1)




