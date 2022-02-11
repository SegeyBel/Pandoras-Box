###Определить, является ли строка валидным украинским номером телефона. Входное значение - строка
# phone_number - мы считаем валидной, если она одновременно отвечает следующим условиям:
#- имеет длину 12 символов;
#- содержит только цифры;
#- начинается с подстроки "380".
#Следовательно, строка "380501234567" должна быть признана валидной,
#"38050123456" - не валидная (не достаточная длина), "380-50-123-4" - невалидная (присутствуют не цифровые символы), "4421234567" ) ###

phone_number1 = "380501234567"
print(len(phone_number1)==12)
print(phone_number1.isdigit())
print(phone_number1.startswith('380'))
print(phone_number1, " is valid" )

phone_number2 = "38050123456"
print(len(phone_number2)==12)
print(phone_number2.isdigit())
print(phone_number2.startswith('380'))
print(phone_number2 , "is invalid no len" )

phone_number3 = "380-50-123-4"
print(len(phone_number3)==12)
print(phone_number3.isdigit())
print(phone_number3.startswith('380'))
print(phone_number3 , "is invalid have no numeric symbols")

phone_number4 = "4421234567"
print(len(phone_number4)==12)
print(phone_number4.isdigit())
print(phone_number4.startswith('380'))
print(phone_number4 , "is invalid begin no '380'")






