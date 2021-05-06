import numpy as np
from matplotlib import pyplot as plt

def get_order(arr):
    angles = 180*np.arctan2(arr[:, 0], arr[:, 1])/np.pi
    angles = (angles + 360)%360
    order = np.argsort(angles)
    return np.append(order[0], np.flip(order[1:]))

def get_radius(arr):
    return np.sqrt(np.power(arr[:, 0], 2) + np.power(arr[:, 1], 2))
n = input("Введите размер массива с точками на декартовой плоскости: ")

points = np.random.randint(-100, 100, (int(n), 2))
order = get_order(points)
radiuses = get_radius(points)

print("Расположение точек в требуемом порядке: {}".format(points[order].tolist()))
print(f"Среднее значение радиуса: {np.mean(radiuses)}")
print(f"Минимальное значение радиуса: {np.min(radiuses)}; \nМаксимальное значение радиуса: {np.max(radiuses)}")
