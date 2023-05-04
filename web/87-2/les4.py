import matplotlib.pyplot as plt


def get_data_from_file() -> tuple:
    file = open(r'web\87-2\lesson_4.txt', 'r')
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


def average_fu(data: list) -> float:
    return round(sum(data)/len(data), 3)


def sigma(data) -> int:
    summa = 0
    av = average_fu(data)
    for el in data:
        summa += (el-av)**2
    return round((summa/(len(data)-1))**0.5, 3)


def corr_coef():
    # дописать функцию
    pass


m_h, m_w, f_h, f_w = get_data_from_file()

fig, axes = plt.subplots(1, 2)

# построить графики

plt.show()
