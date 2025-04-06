import random

'''
# 实现一个猜 1-10 随机数字的游戏，3次机会
temp=input("请输入一个数字\n")
guess=int(temp)
answer = random.randint(1,10)
times = 1
while guess != answer and times < 3:
    if guess > answer:
        print(f'数字猜大了～ 还有{3-times}次机会')
    else:
        print(f'数字猜小了-- 还有{3-times}次机会')
    temp=input('嗯 ....\n')
    guess=int(temp)
    times += 1
if(guess != answer):
    print('time\'s up')
else:
    print(f'您猜对了! 是{guess}')
'''

score=int(input('请输入成绩：'))
if score>90:
    level='A'
elif score>80:
    level='B'
elif score > 70:
    level='C'
print(f'成绩等级是{level}')
