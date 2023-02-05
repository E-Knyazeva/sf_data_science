import numpy as np
a = np.int8(25)
print(a)
print(type(a))

print(np.iinfo(np.int8))
print(np.iinfo(a))
print(np.iinfo(np.int16))
print(np.iinfo(np.int32))
print(np.iinfo(np.int64))

b = np.uint8(124)
print(b)
print(type(b))
print(np.iinfo(b))

print(np.iinfo(np.uint64))

a = np.int32(1000)
print(a)
print(type(a))

a = 2056
print(a)
print(type(a))

a = np.int32(2056)
print(a)
print(type(a))

a = np.int32(1000)
b = a + 25
print(b, type(b))

a = np.int32(1000)
b = np.int8(25)
c = a + b
print(c, type(c))


a = np.int8(270)
print(a)

a = np.int32(2147483610)
b = np.int32(2147483605)
print(a, b)
print(a+b)


a = np.int32(2147483610)
b = np.int32(2147483605)
print(a, b)
print(np.int64(a) + np.int64(b))


print(np.finfo(np.float16))


print(np.sctypeDict)
print(len(np.sctypeDict))

print(*sorted(map(str, set(np.sctypeDict.values()))), sep = '\n')

a = True
print(type(a))

a = np.bool(a)
print(type(a))

a = np.bool_(a)
print(type(a))

a = np.uint8(-456)
print(a)