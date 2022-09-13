def x_list(b):
    x = []
    for i in range(- 1500, 1501):
        x.append((i / b) / 100)
    return x

def trigonometry_func(func, a, b, c, d):
    x = x_list(b)
    trigonometry = [(a * func(b * i + c)) + d for i in x]
    return trigonometry

