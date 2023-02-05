import numpy as np

vec1 = np.array([2,4,7,2.5])
vec2 = np.array([12,6,3.6,13])
print(vec1 + vec2)
print(vec1 * vec2)

vec1 = np.array([2,4,7,2.5])
vec2 = np.array([12,6,3.6,13])
print(vec1 > vec2)

vec = np.array([3,4])
length = np.sqrt(np.sum(vec ** 2)) # длина вектора через формулу
print(length)

length = np.linalg.norm(vec) # длина вектора через функцию numpy
print(length)

vec1 = np.array([0,3,5])
vec2 = np.array([12,4,7])
distance = np.sqrt(np.sum((vec1-vec2)**2)) # расстояние между двумя векторами через формулу
print(distance)
distance = np.linalg.norm(vec1-vec2) # расстояние между двумя векторами через функцию numpy
print(distance)

vec1 = np.arange(1,6)
vec2 = np.linspace(10,20,5)
scalar_product = np.sum(vec1 * vec2) # скалярное произведение двух векторов через формулу
print(scalar_product)
scalar_product = np.dot(vec1, vec2) # скалярное произведение двух векторов через функцию numpy
print(scalar_product)