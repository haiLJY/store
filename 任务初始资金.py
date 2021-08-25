import random
num=random.randint(100,500)
number=0
print(num)
while 1:
    a=int(input("请输入一个数字"))
    number=number+1
    if a ==num and a>=0 :
        print("你成功了")
        print("你总共猜了{0}次".format(number))
        break
    elif a<num :
        print("猜小了")
        num=num-10
        print("猜的数为：",num)
    elif a>num :
        print("猜大了")
        a = a - 10
        num = num - 10
        print("猜的数为：",num)
    else :
        print("你失败了")
        a = a - 10
        num = num - 10
        print("猜的数为：",num)





