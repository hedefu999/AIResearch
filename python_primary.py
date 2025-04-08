
'''
在vscode中运行python代码的方式：
1. 运行python文件 直接点击运行按钮 通过 code run
2. 运行选中的代码行
    2.1 选择在terminal中运行，可以直接打印变量，不必每次写print函数，但不支持等待用户输入的input函数
    2.2 选择在python终端中运行，支持input函数，但变量需要使用print函数才能打印，且字符串不会带有双引号提示
'''
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!\n"
print(message)

print(message * 3)

""" --第一个小游戏-- """
temp = input("请输入一个数字")
guess = int(temp)
if guess == 5:
    print("恭喜你猜对了")
elif guess > 5:
    print("猜大了")
else:
    print("猜小了")

'''数字相加 got 13'''
print(5+8)
'''got 58'''
print('5'+'8')
print('Let\'s python')

''' print special character '''
print('C:\now')
print('C:\\now')
print(r'C:\now')

''' the only way to print \ appended to the tail of the string'''
print(r'heelo\\')

''' print multi-line verse'''
print('''
shut up!
let me die in peace
''')

# print(1>2 && 2>1)
print(3>2 and 2>1)

''' 研究一下数据类型 '''
# python 3的整型类似java的biginteger
print(149597870700/299792458)
# True相当于1，False相当于0
print(1+1>2)
print(True + True)
print(True * False)
print(3*False)

# 类型转换
print(int(3.14))
print(int('3'))
print(float(3))
print(str(3.14))
print(str(True)+'转换一下')
print(bool(0))
print(bool(1))
# 只要不为空，任意字符串都会被bool函数转换为true
print(bool(''))
print(bool(' '))
if(bool('False')):
    print('新人可能觉得这行不会打印出来')
print(bool('True'))
print(bool('0'))
print(bool('1'))

# 使用 type() 函数判断变量的数据类型
var1 = 42
var2 = 3.14
var3 = "Hello, World!"
var4 = True
var5 = [1, 2, 3]
var6 = (1, 2, 3)
var7 = {'a': 1, 'b': 2}
var8 = {1, 2, 3}
var9 = None
print(type(var1) is int)  # <class 'int'>
print(type(var2) is float)  # <class 'float'>
print(type(var3) is str)  # <class 'str'>
print(type(var4)is bool)  # <class 'bool'>
# 据说更推荐使用内置函数 isinstance() 判断数据类型
print(isinstance(var5, list))  # <class 'list'>
print(isinstance(var6, tuple))  # <class 'tuple'>
print(type(var7))  # <class 'dict'>
print(type(var8))  # <class 'set'>
print(type(var9))  # <class 'NoneType'>

# python中判断一个变量不为空
a=None
if(a is None):
    a = 12
print(a is not None)

# python中打印一个元组
a='100'
b=float('23.1')
a,b
print(a,b)

# python3中的除法, floor方式还是返回一个浮点数
print(10/3)
print(10.4/3)
print(10//3)
# // 是整除，返回一个整数,即便返回浮点数也会舍弃小数部分
print(10.5//3)

print((-3)*2 + 5/-2 - 4)
# 幂运算
2**3
2**-3
# not逻辑运算符
not True
not 0 # True
not 4 # False
'''
运算符优先级
() > ** > [+ - 正负号] > [* / //] > [+ -] > [< <= > >= == !=] > not and or
'''
(0 and 1) # 0
False or 0 # 0
3 and 4 # 4
3 or 4 # 3
(not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9) # 这个表达式得到 4

# python中的三元操作符
a=1
b=2
c = 10 if a < b else 5
c
# python 断言
a = 3 and 4
assert a == 4
# python有个空跑的占位语句 pass
a = 1
b= 2
pass
c=a+b
c
# python的可迭代对象处理
for each in "hello":
    print(each)
# 使用range这个内置函数生成一个list
list(range(10))
# range函数参数只能是整数
# 指定开始结束范围
list(range(5,10))
# 指定步长
list(range(1,100,2))

# 使用for循环遍历一个list
sum=0
for i in range(101):
    sum+=i
sum

# 打印今年之后的第一个闰年
for year in range(2025,2050):
    if(year%4==0 and year%100!=0 or year%400==0):
        print(f'找到了第一个闰年{year}')
        break
print(f'while循环运行完毕，注意year变量在循环外仍可以访问{year}')

# python中的else还可以与while、for配对起作用
sum=0
for i in range(101):
    sum+=i
else:
    print(sum)
# 上面这个案例，似乎else可有可无.但下面的案例，第二个场景不会打印结果，因为else也是循环体的一部分，break跳出的是整个循环体
for year in range(2025,2050):
    if(year%4==0 and year%100!=0 or year%400==0):
        break
print(f'2025年后出现的第一个闰年是{year}')

for year in range(2025,2050):
    if(year%4==0 and year%100!=0 or year%400==0):
        break
else:
    print(f'2025年后出现的第一个闰年是{year}')

# python的list可以保存不同类型的元素
empty_list = []
mix_list = [12,'小甲鱼',3.14,[1,2,3]]
mix_list.append('hello')
# mix_list.append('world','!') 一次只能传一个
mix_list.extend(['hello','world']) # addAll 会重复的
mix_list

import random
list=[2,3,4,5]
list.insert(0,1) # 第一个参数是位置，支持负数（倒过来数位置）
list
list[len(list)-1]
list[-1] # 与上面效果相同
# python中互换两个变量的语法糖
a=3
b=4
a,b
a,b=b,a
a,b
# random模块有一个随机取元素的功能
print(random.choice(list))
list.pop() # 默认弹出最后一个元素
list.pop(1)
list
del list[2] # 这个del是python语句，而非list对象的方法
list
del list # del还可用来删除整个变量
# 列表切片,不会修改源列表内容，非常方便
srclist=['he','l','lo','wor','ld']
sliceist=srclist[1:3]
sliceist # 注意切片只得到2个元素
sliceist=srclist[:3]
sliceist=srclist[1:]
# 获取列表最后两个元素的简易写法
sliceist=srclist[-2:]
sliceist
# 列表切片时可以指定步长
slicelist=srclist[::2]
# 步长设置为-1的效果：反转列表
slicelist=srclist[::-1]
slicelist
# 注意下述操作会修改源链表
del srclist[::2]
srclist[0:2]=['greet','talk']

# 对list使用 + 运算符 相当于 extend
# list对象有哪些操作函数
dir(list)
numsList=[1,1,2,3,5,8,13,21]

start=numsList.index(1) + 1
stop=len(numsList)
numsList.index(1,start+1, stop) #会引起报错 ValueError: 1 is not in list

numsList=[1,1,2,3,5,8,13,21]
reversedList=numsList.reverse()
# numsList.sort() # sort(func, key, reverse)
# numslist.sort(reverse=True)
print(reversedList) # None 并没有返回值
print(numsList)

# 元组只可以被访问，不可以被修改
tuple1=(1,2,3,4)
tuple1[2] #3
tuple1[2:] # (3,4) 得到一个小元组
# 复制一个元组，可以使用切片实现
tuple2=tuple1[:]
tuple2[1]=1 # 'tuple' object does not support item assignment
# 可以用下述方式声明元组，这表明小括号不是声明元组的必备，逗号才是标识符（list的是中括号[]）
tuple3=12
tuple3=(12,)
tuple3=12,13,14

# 如何更新元组中的内容 -- 只能通过元组拷贝实现
fruits=('apple','orange','blueberry')
# 在apple与orange之间添加一个banana
fruits2=(fruits[0], 'banana')+fruits[1:]
fruits2
# 获取一个对象的唯一id值
id(fruits2)

# 字符串也可以执行切片操作，字符串同样是不可变的，所以字符串的操作函数都会返回一个更改后的“拷贝”
str1="nihaoya,'xiaohei'"
str1
str1[3:7]

# 字符串格式化
'the quick brown {} jumps {} the lazy {}'.format('fox', 'over', 'dog')
'the quick brown {0} jumps {1} the lazy {2}'.format('fox', 'over', 'dog')
'the quick brown {b} jumps {a} the lazy {c}'.format(a='over', b='fox', c='dog')
'{0}: {1:.2f}'.format("圆周率", 3.1415926)
# '{}: {.2f}'.format("圆周率", 3.1415926) 出错 'float' object has no attribute '2f'
# 冒号表示格式化符号的开始 
'{}: {:.2f}'.format("圆周率", 3.1415926)
# 使用%格式化字符串 字面值都是10进制的，方便书写
'%c'%97 # a 格式化ASCII码
'十进制数字%d 转换为八进制数字：%o' % (100,100) # 括号不可缺少
'一个浮点数%f用科学计数法表示为：%e' % (1250000,1250000)
# 使用格式化的方式拼接字符串
str1='一支穿云箭，千军万马来相见'
str2='两支穿云箭，散户追高不听劝'
'%s - %s' % (str1, str2)
#辅助格式化操作符
'%5.1f' % 27.658 #包含小数点，整个数字字符串长度为5
'%.2e' % 27.658 # 2.77e+01
'%10d' % 50000 # '     50000'
'%010d' % 50000 # '0000050000'
'%#X' %100 # '0X64'
'%#x' % 100 #'0x64'
# 一些乱七八糟的转义字符
msg='\'你好\n\t\\\0\0\0小明\a\"'
print(msg)

# zip内置方法 逐个取出混合
list1=[1,3,5,7,9]
str1='fishc'
tuple1=(12,13,14,15,16)
for item in zip(list1, str1, tuple1): #item是tuple类型
    print(f'类型：{type(item)}, 取值：{item}')

# 创建一个函数
def first_func():
    print('my first function')
first_func()
# 函数返回元组
def test():
    return 1,'jack',12
test()
# 函数定义时参数可以指定默认值
# 写成 def test(a='hey',b) 会报错
def test(a,b='buddy'):
    return a + b
test(b='hello', a='world')

# 函数入参声明可变参数(在python中叫收集参数)
def test(*params):
    print('共有%d个参数' % len(params))
    print(f'第二个参数是 {params[1]}')
    print(f'看看python是如何处理可变参数的：{type(params)}')
test('hello', 'world')
# 如果收集参数之后还有其他参数要输入
def test(*params, extra):
    print("收集参数是：", params)
    print(f'额外参数是{extra}')
test(1,2,3,34,extra='hello')

def test(extra, *params):
    print("收集参数是：", params)
    print(f'额外参数是{extra}')
test('hello',1,2,3,34)

# 上面使用星号*进行了收集参数声明，用在参数引用时就是解包效果
num=(1,2,3,4,5)
print(num)
print(*num)

name='FishC'
print(*name)
list=[2,3,4]
print(*list)

# 使用双星号 ** 声明收集参数
# 在函数体中修改全局变量的值，并不会真的改变它

# 如果一定要在函数中修改外部全局变量，可以这样
count=5
def my_func():
    global count
    count=10
    print(count)
my_func()
count

# 内嵌函数，内部函数可以引用外部函数的局部变量
def func1():
    print('func1正在执行')
    def func2():
        print('func2正在执行')
    func2()
func1()
func2()

# LEGB原则
# 先看下代码
x=120
print(id(x))
def funcA():
    x = 12
    print(id(x))
    def funcB():
        x=11
        print(id(x))
    funcB()
# 这3个x是同一个变量吗，使用id值来判断    
funcA()
# 3个id结果并不相同

# LEGB含义：Local-函数内的名字空间；Enclosing function locals-嵌套函数中外部函数的名字空间
# Global - 函数定义所在模块的名字空间；Builtin - Python内置模块的名字空间
#  变量查找的顺序依次是 L -> E -> G -> B

# 闭包是啥：在嵌套函数环境下，内部函数引用了外部函数的局部变量，此时内部函数就可以认为是闭包
def funcX(x):
    def funcY(y):
        return x*y
    return funcY

temp=funcX(8)
temp(5)
# 闭包就是函数返回值是一个函数，函数的调用传参是“二维”的
print(funcX(10)(4))

# 闭包环境下，内部函数无法修改外部函数的局部变量，py3提供了一个关键字nonlocal可以使得这种变量可修改
def funcX():
    x=5
    def funcY():
        nonlocal x
        x=x+1
        return x
    return funcY
funcX()()
# 闭包存在的意义：尽可能避免使用全局变量
# 闭包允许将函数与其所操作的某些环境/数据关联起来，这样外部函数就为内部函数构成了一个封闭的环境
# 如下述写法
def createPlane(pos_x=0, pos_y=0):
    def move(direction, step):
        nonlocal pos_x, pos_y
        new_x = pos_x + direction[0]*step
        new_y = pos_y + direction[1]*step
        return new_x,new_y
    return move
movemove=create()
movemove([1,0],10) #向左移动10步
# 这样movemove函数定义时没有对create传参，使用了默认值，这样就能做到pos_x pos_y 封闭不能被其他外部函数修改

'''
# 运行至131页
# vscode进行的关闭代码提示的配置，新手阶段不建议使用
#
'''


