###Определить, попадает ли индекс массы тела в интервал нормальных значений.
# Используя переменные weight (вес человека в килограммах) и height (рост в метрах) рассчитать индекс массы тела по формуле: BMI = weight/(height * height)
# Нормальный индекс массы тела имеет значение от 18.5 (lower_bound) до 25 (upper_bound). Поэтому человек имеет нормальный ИМТ,
# если его значение одновременно больше нежной границы и меньше верхней.
# В результате выведите строку: "Your BMI is normal: True" (если ИМТ попадает в интервал) или "Your BMI is normal: False" (если не попадает).
# Использовать только методы, которые рассматривали на занятии (без условных выражений и разветвления).###



weight = 60
height = 1.75
BMI = weight/(height * height)
lower_bound = 18.5
upper_bound = 25
print(BMI <= lower_bound)
print(BMI >= upper_bound)
print("Your BMI is normal: True", round(BMI))




