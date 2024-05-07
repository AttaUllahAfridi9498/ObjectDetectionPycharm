def bmi(weight, height):
    if weight <= 0 or height <= 0:
        return None
    else:
        return weight / height ** 2

print(bmi(52.5, 1.65))
print(bmi(-10, 1.65))
print(bmi(52.5, -1.65))
print(bmi(0, 1.65))
print(bmi(52.5, 0))

# def ft_and_inch_to_m(ft, inch=0.0):
#     return ft * 0.3048 + inch * 0.0254
#
#
# def lb_to_kg(lb):
#     return lb * 0.45359237
#
#
# def bmi(weight, height):
#     if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
#         return None
#
#     return weight / height ** 2
#
#
# print(bmi(weight=lb_to_kg(176), height=ft_and_inch_to_m(5, 7)))
#


