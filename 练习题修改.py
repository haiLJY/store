#print("请输入10个数：")
'''a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
g=int(input())
h=int(input())
i=int(input())
j=int(input())
sum=a+b+c+d+e+f+g+h+i+j       10个数的和
print(sum)                       
average=sum/10                 10个数的平均值
print(average)'''
'''def max(*a):
    m=a[0]
    for x in a :
        if x>m :
            m=x
            return m'''
#print("max(0,1,2,6,3,4,5,9,8,7):",max(0,1,2,6,3,4,5,9,8,7))


'''
import random
num=random.randint(50,150)   第三题，随机产生50到150之间的数
print(num)
'''
'''
a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))
if a==b or b==c or a==c :
    print("构成等腰三角形")
elif a==b==c :
    print("构成等边三角形")
elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a :        判断是否可以组成三角形
    print("构成直角三角形")
elif a + b > c and a + c > b and b + c > a :
        print("构成普通三角形")

        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print('三角形面积为 %0.2f' %area)
    
else:
    print("不能形成三角形")
    '''

'''
i = 1
while i <= 9:
    j = 1
    while(j <= i):    # j的大小是由i来控制的
        print(f'{i}*{j}={i*j}', end='\t')      99乘法表
        j += 1
    print('')
    i += 1
    '''
'''
for i in range(-9,0):
 for j in range(1,10):
  if j==i*(-1) :
   print(j,"*",i*(-1),"=",i*j*(-1))
   break
  elif i*j*(-1)>9 :
   print(j,"*",i*(-1),"=",i*j*(-1),end="")      倒叙99乘法表
  else:
   print(j,"*",i*(-1),"=",i*j*(-1),end="")
'''
'''
A=56
B=78
sum=A+B
A=sum-A     +  -实现A，B的调换
B=sum-B
print(A,B)
'''

'''num=int(input("输入一个数字："))
fac=1
 #for i in range(1,num+1):         循环实现阶乘for循环
   fac=fac*i
   print(num, fac)
   '''
#i=1
#while i<=num:
 #fac=fac*i                        循环实现阶乘 while循环
 #i=i+1
 #print(num, fac)

'''row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')                 打印三角形
    for _ in range(2 * i + 1):
        print('*', end='')
    print()'''



'''a=input().split()
b=[]
k=sum1=0
day=1
for i in range(1,4) :
            b.append(int(a[k]))
            k+=1
while True :                               青蛙爬井
            sum1+=b[1]
            if sum1>=b[0] :
             break
            sum1-=b[2]
            day+=1
print(day)
'''

'''count = 0
username = "root"
password = "admin"
name = input("请输入用户名")
if name == username :
    while count < 3 :
      password = input("登录密码：")
      if password == password :
          print("欢迎登录")
          break
      else :
          print("密码错误")
          count +=1
    else :
     print("连续三次输错密码，用户已经被锁定")
else :
    print("用户名错误")'''









