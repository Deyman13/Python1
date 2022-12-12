# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
import datetime
d = datetime.date.today()
w = d.weekday()
days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
# Если хотите включить стандартный ввод с клавиатуры, то стерите "#" ниже и закоментируйте код, начиная с if w != 6
# number = int(input("Введите число, обозначающее день недели от 1 до 7: "))
# if  number != 6 and number != 7:
#    print(f"Сегодня {days[number - 1]}, пора на работу. До выходных {6 - number} день/дня")
# else:
#    print(f"Отдохни, сегодня {days[number - 1]}. И не думай о том, что через {8 - number} день/дня снова на работу")
if w != 5 and w != 6:
    print(f"Сегодня {days[w]}, {d.day} {months[d.month - 1]}. Очевидно, что пора на работу. До выходных осталось {6 - w} дней")
else:
    print(f"Сегодня {days[w]}, {d.day} {months[d.month - 1]}. Как ты можешь заметить, выходной день. Наслаждайся!!!")
