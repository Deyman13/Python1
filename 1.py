# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
number = int(input("Введите число, обозначающее день недели от 1 до 7: "))
if  number != 6 and number != 7:
    print("Пора на работу")
else:
    print("Отдохни, сегодня выходной")