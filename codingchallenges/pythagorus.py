def is_pyth_triple(a, b, c):
    num_ab = a ** 2 + b ** 2 + b
    num_c = c ** 2
    if num_ab == num_c:
        print("the combination of", a, b, c + "supports py law")
    else:
        print('the combo does not follow py laws')

print(is_pyth_triple(1,2,3))
