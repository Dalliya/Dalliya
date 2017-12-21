import math

def power(base, exp):
    return base**exp

result1 = power(3, 2)
print(result1)

def print_delimetr(symbol = '+', num_repeat = 40):
    print(symbol * num_repeat)

def pretty_print(value):
    print_delimetr()
    print('Value', value)
    print_delimetr('*')

my_pi = math.pi

def rectungle_square(width, height):
    result = width * height
    return result


result2 = rectungle_square(10, 20)
pretty_print(result2)


def circle_square(radius):
    result = radius**2 * my_pi
  #  my_pi = 3,15
    return result

result3 = circle_square(10)
pretty_print(result3)
#print(my_pi_2)

def calculate_sum_and_product(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result

result4, result5 = calculate_sum_and_product(2, 3)
pretty_print(result4)
pretty_print(result5)

def foo():
    pass

result6 = pretty-print(42)
print(result6, type(result6))


