
def foo(a):
    for i in range(a):
        print(' ')

a = 5
b = 10

c = a * b


try:
    b = 10 / 0
    
    raise "other error"
except ZeroDivisionError:
    print('something wrong happened')

foo(c)

d = c // 8

print(d)