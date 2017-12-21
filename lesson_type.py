import math

width = 10
height = 25

rectangle_square = width * height
print("Площадь прямоугольника равна при высоте:", height, "и ширине:", width, "равна:", rectangle_square)
print("Площадь прямоугольника при высоте %d и ширине %d равна: %d" % (height, width, rectangle_square ))

catheter1 = 4
catheter2 = 4
hypotenuse = math.sqrt(catheter1**2 + catheter2**2)

print("Гипотенуза треугольника при катете1 = %d см и катете2 = %d  см равна: %.3f см" % (catheter1, catheter2, hypotenuse))

print(hypotenuse)