# Создать 2 массива NumPy
# Один из случайных чисел, второй - использую arange Или linspace
# После этого выполнить математические операции- сложить, перемножить, делить
# Найти максимальный элемент в каждой строчке и столбце первого массива (из случайных чисел_
# Найти максимальный элемент в из 2 массивов
# Изменить форму массива

import numpy as np

first_array=np.random.randint(0, 10, 12, dtype=int)
print(first_array)

second_array=np.linspace(1, 121, 12, dtype=int)
print(second_array)

sum_of_arrays=first_array+second_array
prod_of_arrays=first_array*second_array
div_of_arrays=first_array/second_array
print(f'sum: {sum_of_arrays}, \n product: {prod_of_arrays}, \n division: {div_of_arrays}')

reshaped_array1=first_array.reshape(3, 4)
cols_maximum=reshaped_array1.max(axis=0)
lines_maximum=reshaped_array1.max(axis=1)
print(f'array: {reshaped_array1} \n maximum values of columns: {cols_maximum} \n maximum values of lines: {lines_maximum}')

def find_max(arr1, arr2):
    return np.concatenate([arr1.ravel(), arr2.ravel()]).max()

max_of_two=find_max(reshaped_array1, second_array)
print(f'array1: {reshaped_array1}, \n array2: {second_array} \n maximum of two arrays: {max_of_two}')