immutable_var = ([1,6], 5.6, True, 'Строка',8)
print(immutable_var)
immutable_var[0][1] = 7  #НЕ ОШИБКА.Обращаемся к второму элементы списка. Список - изменяемый тип данных
print(immutable_var)
#immutable_var[0] = [2,4,8] #ОШИБКА. Обращаемся к первому элементу Кортежа. Кортеж - не изменяемый тип данных

mutable_list = immutable_var[0]
print(mutable_list)
mutable_list = [1,5,9,0,13]
print(mutable_list)