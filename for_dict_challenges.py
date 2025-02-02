from collections import Counter

print("Задание №1\n")
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names = []
for people in students:
    names.append(people['first_name'])

count = Counter(names)
counter_name_1 = count['Вася']
counter_name_2 = count['Маша']
counter_name_3 = count['Петя']

print(f"Вася: {counter_name_1}\nМаша: {counter_name_2}\nПетя: {counter_name_3}")


print("______________________\n\nЗадание №2\n")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = []
for people in students:
    names.append(people['first_name'])

names_str=','.join(names)

words = names_str.split(',')

most_use_name = Counter(words).most_common(1)
for name in most_use_name:
    use_name = name[0]
print(f"Самое частое имя среди учеников: {use_name}")


print("______________________\n\nЗадание №3\n")

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

names = []
a=0
def find_name_in_class():
    names = []
    for students in school_class:
        names.append(students['first_name'])
        names_str=','.join(names)
        words = names_str.split(',')
        most_use_name = Counter(words).most_common(1)
        for name in most_use_name:
            use_name = name[0]
    return (use_name)
    
for school_class in school_students:
    a+=1
    c = find_name_in_class()
    print(f"Самое частое имя в классе {a}: {c}")

print("______________________\n\nЗадание №4\n")


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def count_males_in_school(school_class):
    count_girls = 0
    count_boys = 0
    for name in school_class['students']:
        real_name = name['first_name']
        if is_male[real_name]:
            count_boys+=1
        else:
            count_girls+=1
    return(count_boys,count_girls)
    
        
for school_class in school:
    boys, girls = count_males_in_school(school_class)
    print(f"Класс {school_class['class']}: девочки {girls}, мальчики {boys}")
    
    

print("______________________\n\nЗадание №5\n")

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
def count_males_in_school(school_class):
    count_girls = 0
    count_boys = 0
    for name in school_class['students']:
        real_name = name['first_name']
        if is_male[real_name]:
            count_boys+=1
        else:
            count_girls+=1
    return(count_boys,count_girls)
    
max_boys = []
max_girls = []
for school_class in school:
    max_boys.append(boys)
    max_girls.append(girls)
if max_boys[0] > max_boys[1]:
    print(f"Больше всего мальчиков в классе 2a")
else:
    print(f"Больше всего мальчиков в классе 3c")
if max_girls[0] > max_girls[1]:
    print(f"Больше всего девочек в классе 2a")
else:
    print(f"Больше всего девочек в классе 3c")


'''
^тупое решение.

я могу найти наибольшее значение в списке мальчиков и девочек отдельно через

max_value_boys = max(max_boys)
max_index = max_boys.index(max_value)
max_value_girls = max(max_girls)
max_index = max_girls.index(max_value)


но как мне подцепить и вывести название класса в print через найденный индекс в max_index?
'''