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
