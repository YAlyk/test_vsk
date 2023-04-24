import random
from collections import Counter

def data_generate():
    random.seed(100)
    data = [random.randint(0,30) for el in range(1000)]

    return data

def averge_fu(data):
    return round(sum(data)/len(data), 3)

def mode(data):
    c = Counter(data)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]


def median(data):
    n = len(data)
    index = n // 2
    if n % 2:
        return sorted(data)[index]
    else:
        return sum(sorted(data)[index-1:index+1]) / 2

# тернарная операция

# a if <условие> else b
# if <условие>:
#     d = a
# else:
#     d = b
data = data_generate()
print('среднее значение:', averge_fu(data))
print('мода:', mode(data))
print('медиана:', median(data))
