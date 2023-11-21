tuple1 = ()
tuple2 = (1,)
tuple3 = (1,2,3)
tuple4 = 1,2,3
tuple5 = ('a', 'b', ('ab', 'cd'))
print("tuple1 : ", tuple1)
print("tuple2 요소가 1개면 반드시 뒤에 쉼표를 붙여야 한다. : ", tuple2)
print("tuple3 : ", tuple3)
print("tuple4 : ", tuple4)
print("tuple5 : ", tuple5)
print("튜플은 요솟값을 지우거나 변경할 수 없다")

print("tuple2(0) : ", tuple2[0])

print("tuple5[1:] : ", tuple5[1:])


tuple1 = (1, 2, 'a', 'b')
tuple2 = (3, 4)
print("tuple1 : ", tuple1)
print("tuple2 : ", tuple2)
print("tuple1 + tuple2", tuple1 + tuple2)

print("tuple2 * 3 : ", tuple2 * 3)

print("len(tuple2)", len(tuple2))
