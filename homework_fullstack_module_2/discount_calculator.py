# программа работает с положительными числами

"""
Нашла следующее: Функция round() в Python округляет число к ближайшему целому числу, но если дробная часть числа
равна .5, то она округляется в сторону ближайшего четного числа. Это называется банковским округлением (или округление
по правилам "Round Half to Even").
По заданию должно было огкругляться в большую сторону (1063), потому использовала math.ceil() для округления
числа до большего целого

"""

import math

def discount_calculator():
    price = input("Введите сумму покупки: ")
    if not price:
        print("Что-то пошло не так. Попробуйте снова!")
    else:
        print(f"Сумма покупки: {price}")

    sale = input("Введите процент скидки: ")
    if not sale:
        print("Что-то пошло не так. Попробуйте снова!")
    else:
        print(f"Процент сикдки: {sale}")

    price = int(price)
    sale = int(sale)

    profit = price * (sale / 100)
    final_price = math.ceil(price - profit)

    print(f'Вы экономите: {profit:.1f} \nСумма к оплате (округлено): {final_price}')


discount_calculator()


