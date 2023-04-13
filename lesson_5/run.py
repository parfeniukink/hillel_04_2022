from dis import dis


def foo():
    a = 1.9


print(dis(foo))
