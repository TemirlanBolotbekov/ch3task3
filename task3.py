#"Аналог шифра цезаря ". Программа должна запрашивать элементы списка через
#пробел. После чего пользователь должен ввести значение для сдвига элементов списка.
#Значение может быть как положительным, так и отрицательным. Если значение
#положительное, элементы списка должны сдвигаться вправо, если отрицательное -
#влево. Результат необходимо вывести на экран:


spis = (input('Input numbers:').split())
com =int(input('Moving :'))
print("Before-",spis)
if com > 0:
    spis = spis[com:]+spis[:com]#Старт,стоп,шаг:СРЕЗЫ используется:list,str,tuple
    print("After-",spis)
elif com < 0:
    spis = spis[com:]+spis[:com:]
    print("After-",spis)
