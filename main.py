# Задача 1
# Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.

for i in range(5):
    print("{}: 0".format(i + 1))

# Задача 2
# Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.

count = 0
for i in range(10):
    data = int(input("Type the number: "))
    if data == 5:
        count += 1

print(count)

# Задача 3
# Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.

sum_value = 100
for i in range(1, 50):
    sum_value += (i + (100 - i))
sum_value += 50
print(sum_value)

# Задача 4
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.

multiple = 1
for i in range(1, 11):
    multiple *= i

print(multiple)

# Задача 5
# Вывести цифры числа на каждой строчке.

integer_number = 67543

while (integer_number // 10) > 0:
    print(integer_number % 10)
    integer_number = integer_number // 10
print(integer_number % 10)

# Задача 6
# Найти сумму цифр числа.

integer_number = 1111111111
sum_of_numbers = 0

while (integer_number // 10) > 0:
    sum_of_numbers += (integer_number % 10)
    integer_number = integer_number // 10

sum_of_numbers += (integer_number % 10)
print(sum_of_numbers)

# Задача 7
# Найти произведение цифр числа.

integer_number = 12345
multiple_of_numbers = 1

while (integer_number // 10) > 0:
    multiple_of_numbers *= (integer_number % 10)
    integer_number = integer_number // 10

print(multiple_of_numbers)

# Задача 8
# Дать ответ на вопрос: есть ли среди цифр числа 5?

integer_number = 67435
count = 0

while (integer_number // 10) > 0:
    if integer_number % 10 == 5:
        count += 1
    integer_number = integer_number // 10

print("{}".format(count > 0))

# Задача 9
# Найти максимальную цифру в числе

test_number = 222578
max_number = 0

while (test_number // 10) > 0:
    temp = test_number % 10
    if temp % 10 > max_number:
        max_number = temp
    test_number = test_number // 10

print(max_number)

# Задача 10
# Найти количество цифр 5 в числе

test_number = 252257855
count = 0

while (test_number // 10) > 0:
    if test_number % 10 == 5:
        count += 1
    test_number = test_number // 10

print(count)
