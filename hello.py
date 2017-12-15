#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print('******************基础*********************')

print('hello, world  你好 中文')


print(ord('A'))

print(ord('中'))

print(chr(66))

x=b'ABC'
print(x)

print(id(x))


print(len('ABC'))


print('******************集合*********************')

#list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

#tuple 元组
classmates2 = ('h1', 'h2', 'h3')
print(classmates2)

#循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)


#dict
d = {'a1': 95, 'a2': 75, 'a3': 85}
print(d['a1'])

#set set和dict类似，也是一组key的集合，但不存储value
#由于key不能重复，所以，在set中，没有重复的key
s=set([1, 1, 2, 2, 3, 3])
print(s)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)


print('****************函数***********************')

#绝对值
a=abs(100)
print(a)
b=abs(-30)
print(b)

#最大值
print(max(1,2))


#类型转换
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

#函数赋值给变量
d=abs
print(d(-40))


#定义函数
def my_abs(x):
    if x>= 0:
        return x
    else:
        return -x

print(my_abs(-99))


#空函数
#如果想定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass

##pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，
##就可以先放一个pass，让代码能运行起来。
##缺少了pass，代码运行就会有语法错误。



##数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


#print(my_abs('A'))会报错

import math

def move(x, y, step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx, ny


x ,y =move(100, 100, 60, math.pi/6)
print(x,y)


print(math.sqrt(2))


def calc(numbers):
    sum=0
    for n in numbers:
        sum =sum+n*n
    return sum


print(calc([1,2,3]))

##可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1, 2))
print(calc())


##  *nums  表示把nums这个list的所有元素作为可变参数传进去。
##这种写法相当有用，而且很常见。
nums=[1,2,3]
print(calc(*nums))


##关键字参数可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，
##这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:',age,'other:', kw)

print(person('Xiaoer',30,city='shanghai'))


extra={'city':'Beijing','job':'Engineer'}
print(person('Jack',24,**extra))



#命名关键字参数
##如果要限制关键字参数的名字，就可以用命名关键字参数，
##例如，只接收city和job作为关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


##和关键字参数**kw不同，
##命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数

##如果没有加* 好，那就是按顺序的位置去传参数的，如果加了* name后面的就是按照
##参数名传的，也就是传参数时，如果需要传入，则必须带名字赋值，如果有默认的值，
##那就可以忽略不传




##如果函数定义中已经有了一个可变参数，
##后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
##def person(name, age, *args, city, job):
##    print(name, age, args, city, job) 

##print(person('Jack', 24, 'Beijing', 'Engineer'))会报错
    

##参数组合
##在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，
##参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

##在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。



    

