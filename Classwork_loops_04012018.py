for i in range(10):
    if i % 2 == 0:
        print('hello world!', i)
    else:
        print('happy new year!', i)

s = 'abcabc'
print(s[1:-1:2])
for i in range(100, 20, -2):
    print('Iteration#:', i)


for i in range(10):
    print('print smth!')


#####################################################################
print('------------------------------')
for week_day in ['Mo', 'Tu', 'We', 'Th']:
    print(week_day)


#####################################################################
print('------------------------------')
for i in range(1, 101):
    print(i)

####################################################################
print('------------------------------')
for i in range(1, 101, 2):
    print(i)


#####################################################################
print('------------------------------')
for i in range(1, 101):
    if i % 2 == 0:
        print(i)


#####################################################################
sum_total = 0
for i in range(1, 101):
    sum_total = sum_total + i
print(sum_total)

#####################################################################
def sum_of_n(n):
    sum_total = 0
    for i in range(1, n+1):
        sum_total += i
    return sum_total

print(sum_of_n(100))
print(sum_of_n(10))
print(sum_of_n(3))
print(sum_of_n(42))

######################################################################
text = 'Вы перешли в режим инкогнито.'
print(len(text.split(' '))-1)
print(text.count(' '))


def find_num_of_uppers(text):
    upper_total = 0
    for char in text:
       if char.isupper():
          upper_total += 1
    return upper_total

print(find_num_of_uppers(text))


########################################################################
def camelize_me(var_name):
    var_name_lst = var_name.split('_')
    result = ''
    for part_name in var_name_lst:
        print(part_name)
        print(part_name, part_name.capitalize())
        result += part_name.capitalize()
    return result


print(camelize_me('this_is_a_long_snake_style_var_name'))
print(camelize_me('style_var_name'))
print(camelize_me('a_b_c_d_e'))

