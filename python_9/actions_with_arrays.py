import numpy as np
arr = np.arange(8)
print(arr)

arr.shape = (2,4) # 1ое число - число строк, 2ое число - число столбцов
print(arr)

arr = np.arange(8)
arr_new = arr.reshape((2,4), order = 'F') # массив заполняется числами по столбцам
print(arr_new)

arr = np.arange(8)
arr.shape = (2, 4)
print(arr)
arr_trans = arr.transpose() # транспонирование двумерного массива
print(arr_trans)

arr = np.arange(3)
print(arr.shape)
arr_trans = arr.transpose()
print(arr_trans)

arr = np.linspace(1,2,6)
print(arr)
print(arr[2])
print(arr[2:4])
print(arr[::-1])

nd_arr = np.linspace(0, 6, 12, endpoint = False).reshape(3, 4)
print(nd_arr)
print(nd_arr[1,2])
print(nd_arr[:2, 2])
print(nd_arr[1:, 2:4])
print(nd_arr[:, 2:4])
print(nd_arr[:2])

arr = np.array([23,12,45,12,23,4,15,3])
arr_new = np.sort(arr)
print(arr)
print(arr_new)

arr = np.array([23,12,45,12,23,4,15,3])
print(arr.sort())
print(arr)

data = np.array([4,9,-4,3])
root = np.sqrt(data)
print(root)
print(sum(root))
print(np.isnan(root))
print(root[np.isnan(root)])
root[np.isnan(root)] = 0
print(root)
print(sum(root))