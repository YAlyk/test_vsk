# import matplotlib.pyplot as plt
# import random


# def get_data_from_file() -> tuple:
#     # Получаем 4 массива. По 2 массива с ростом и весом для мужчин и женщин

#     file = open(
#         'C:/Users/koksh/Desktop/pyton/code/web/58-11/3/lesson_4.txt', 'r')

#     file = [line.strip() for line in file]

#     male_height = []
#     male_weight = []

#     female_height = []
#     female_weight = []

#     non_height = []
#     non_weight = []

#     for line in file:
#         q = line.split()
#         sex, height, weight = q[0], int(q[1]), int(q[2])
#         if sex == 'Male':
#             male_height.append(height)
#             male_weight.append(weight)
#         else:
#             female_height.append(height)
#             female_weight.append(weight)

#     return male_height, male_weight, female_height, female_weight


# def find_cnt(data: list) -> dict:
#     # Функция возвращает словарь, где ключ - число, значение - сколько раз
#     # встречается число в наборе данных
#     dic = {}

#     for el in set(data):
#         dic[el] = data.count(el)

#     return dic


# def data_to_bar(data: list) -> tuple:
#     '''
#     На вход получаем список с данными типа int
#     Возвращаем кортеж из двух списков, где первый список - характеристика (например, вес) - для оси иск
#     Второй список - сколько раз эта характеристика встретилась в данных - для оси игрек
#     '''
#     tup = find_cnt(data)
#     x, y = [], []
#     for el in tup:
#         x.append(el)
#         y.append(tup[el])

#     return x, y


# m_h, m_w, f_h, f_w = get_data_from_file()

# fig, axes = plt.subplots(2, 2,)
# x_m_h, y_m_h = data_to_bar(m_h)
# x_m_w, y_m_w = data_to_bar(m_w)
# x_f_h, y_f_h = data_to_bar(f_h)
# x_f_w, y_f_w = data_to_bar(f_w)

# axes[0, 0].bar(x_m_h, y_m_h, color='red')
# axes[0, 1].bar(x_m_w, y_m_w, color='blue')
# axes[1, 0].bar(x_f_h, y_f_h, color='red')
# axes[1, 1].bar(x_f_w, y_f_w, color='blue')
# plt.show()


import matplotlib.pyplot as plt


def get_data_from_file() -> tuple:
    # Получаем 4 массива. По 2 массива с ростом и весом для мужчин и женщин

    file = open(
        'C:/Users/koksh/Desktop/pyton/code/web/58-11/3/lesson_4.txt', 'r')

    file = [line.strip() for line in file]

    male_height = []
    male_weight = []

    female_height = []
    female_weight = []

    non_height = []
    non_weight = []

    for line in file:
        q = line.split()
        sex, height, weight = q[0], int(q[1]), int(q[2])
        if sex == 'Male':
            male_height.append(height)
            male_weight.append(weight)
        else:
            female_height.append(height)
            female_weight.append(weight)

    return male_height, male_weight, female_height, female_weight


# среднее арифметическое
def average(data):
    return round(sum(data) / len(data))


def sigma(data) -> int:
    summa = 0
    av = average(data)

    for el in data:
        summa += (el - av) ** 2

    # По сравнение со 2 уроком исправлено округление и перевод в int
    return int(round((summa / (len(data) - 1)) ** 0.5, 0))


def corr_coef(x, y):
    x_mid = average(x)
    y_mid = average(y)

    chisl = 0
    for i in range(len(x)):
        chisl += (x[i]-x_mid) * (y[i]-y_mid)
    return chisl / (sigma(x) * sigma(y) * (len(x)-1))


def get_coeff_k_b(data_x, data_y):
    sigma_x = sigma(data_x)
    sigma_y = sigma(data_y)
    r_xy = corr_coef(data_y, data_y)
    k = round((sigma_y/sigma_x)*r_xy, 3)
    b = round(average(data_y)-k*average(data_x), 3)

    return k, b


def get_line(data_x, data_y):
    # возвращать 2 массива по 2 точки для построения линии + коэфф к и б
    k, b = get_coeff_k_b(data_x, data_y)
    x = []
    y = []
    x_min = min(data_x)
    x_max = max(data_x)

    x.append(x_min)
    y.append(k+x_min+b)

    x.append(x_max)
    y.append(k+x_max+b)

    return x, y, k, b


m_h, m_w, f_h, f_w = get_data_from_file()
m_l_x, m_l_y, m_k, m_b = get_line(m_w, m_h)
f_l_x, f_l_y, f_k, f_b = get_line(f_w, f_h)


fig, axes = plt.subplots(1, 2)


print('коэффициент кореляции для мужчин:', corr_coef(m_h, m_w))
print('коэффициент кореляции для женщин:', corr_coef(f_h, f_w))
print('коэффициенты k и b для мужчин:', m_k, m_b)
print('коэффициенты k и b для женщин:', f_k, f_b)
axes[0].scatter(m_w, m_h, color='blue')
axes[0].plot(m_l_x, m_l_y, color='red')
axes[1].scatter(f_w, f_h, color='red')
axes[1].plot(f_l_x, f_l_y, color='blue')
plt.show()
