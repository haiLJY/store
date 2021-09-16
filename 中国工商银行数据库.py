import random
import pymysql
import cursor

print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank={}#创建一个空的字典
#开户逻辑
bank_name="狼腾测试猿银行"
# 第一个对应第一个 不是名称对应名称
conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="bank",
        charset="utf8"
    )
cursor = conn.cursor()
#开户
def bank_adduser(account):
    cursor = conn.cursor()
    sql = "select count(*) from  add_user"
    cursor.execute(sql)
    date = cursor.fetchall()
    cursor.close()
    if date[0][0] >= 100:
        return 3
    cursor = conn.cursor()
    sql = "select account from  add_user"
    cursor.execute(sql)
    date = cursor.fetchall()
    cursor.close()
    if account in date:
        return 2
    return 1
def adduser():  # 定义了一个方法
    username = input("请输入您的用户名：")
    password = input("请输入您的密码(6位阿拉伯数字)：")
    print("请输入您的地址：")
    country = input("\t\t请输入您的国家：")
    province = input("\t\t请输入您的省份：")
    street = input("\t\t请输入您的街道：")
    door = input("\t\t请输入您的门牌号：")
    bank_name=input("\t\t请输入您的开户行：")
    while True:
        account = random.randint(10000000, 99999999)
        cursor = conn.cursor()
        sql_adduser = "select account from add_user"
        cursor.execute(sql_adduser)
        bank = cursor.fetchall()
        if account not in bank:
            break
        cursor.close()
    if password.isdecimal():
        if len(password) == 6:
            stast = bank_adduser(account)
            if stast == 3:
                print("你去别的银行吧")
            elif stast == 2:
                print("开户失败，你别重复")
            elif stast == 1:
                cursor = conn.cursor()
                sql_insert = "insert into add_user value (%s, %s, %s, %s, %s, %s, %s, %s, NOW(),%s)"
                date = [account, username, password, country, province, street, door, 0,  bank_name]
                cursor.execute(sql_insert, date)
                conn.commit()
                cursor.close()
                print("------------个人信息 - -----------")
                print("账号： %s" % account)
                print("用户名: %s" % username)
                print("密码： *****")
                print("地址： %s %s %s %s" % (country, province, street, door))
                print("余额： %s" % date[7])
                print("开户行名称： %s" % bank_name)
                print("--------------------------------")
        else:
            print("密码长度必须是6位！！！")
    else:
        print("密码必须是阿拉伯数字！！！")
#查询
def select():
    user = input("请输入您的用户名: ")
    cursor.execute("SELECT * FROM add_user where username=  '%s' " % user)
    card = cursor.fetchone()
    if card is None:
        return Return(1)
    else:
        cursor.execute("SELECT * FROM add_user where username='%s' " % user)
        data = cursor.fetchone()
        print(data[1], "您好!")
        for i in range(3):
            pswd = input("请输入您的密码: ")
            if pswd == data[2]:
                info = '''
                                             ------------个人信息------------
                                             账号：%s
                                             用户名:%s
                                             密码：*****
                                             地址：%s%s%s%s
                                             余额：%s
                                             开户行名称：%s
                                             --------------------------------
                                                                           '''
                print(info % (data[0], data[1], data[3], data[4], data[5], data[6], data[7], data[9]))
                break
            else:
                print("对不起,您输入的密码错误")


#存钱
def saveMoney():
    user = input("请输入您的用户名：")
    cursor.execute("SELECT * FROM add_user where username=  '%s' " % user)
    card = cursor.fetchone()
    if card is None:
        return Return(1)
    cursor.execute("SELECT * FROM add_user where username='%s' " % user)
    data = cursor.fetchone()
    print(data[1], "您好!")
    for i in range(3):
        pswd = input("请输入您的密码: ")
        if pswd == data[2]:
            print("您有金额: ", data[7])
            break
        else:
            return Return(2)
    savemoney = float(input("请输入您要存入的金额："))
    money = float(data[7]) + savemoney
    cursor.execute("UPDATE add_user SET money = '%s' WHERE username = '%s' " % (money, user))
    conn.commit()
    # 提示消息
    print("存款成功，您当前用户可用余额为：%s元" % (money))
#取钱
def getMoney():
    user = input("请输入您的用户名：")
    cursor.execute("SELECT * FROM add_user where username=  '%s' " % user)
    card = cursor.fetchone()
    if card is None:
        return Return(1)
    cursor.execute("SELECT * FROM add_user where username='%s' " % user)
    data = cursor.fetchone()
    print(data[1], "您好!")
    for i in range(3):
        pswd = input("请输入您的密码: ")
        if pswd == data[2]:
            print("您有金额: ", data[7])
            break
        else:
            return Return(2)
    getmoney = float(input("请输入您要取出的金额："))
    if getmoney > float(data[7]):
        print("对不起，您的余额当前余额为%s元，余额不足！！！" % float(data[7]))
        return Return(3)
    else:
        card_money = float(data[7]) - getmoney
        cursor.execute("UPDATE add_user SET money = '%s' WHERE username = '%s' " % (card_money, user))
        conn.commit()
        print("取款成功，您当前用户可用余额为：%s元" % (card_money))
#转账
def transferMoney():
    user = input("请输入您的用户名：")
    cursor.execute("SELECT * FROM add_user where username=  '%s' " % user)
    card = cursor.fetchone()
    if card is None:
        return Return(1)
    else:
        cursor.execute("SELECT * FROM add_user where username='%s' " % user)
        data = cursor.fetchone()
        print(data[1], "您好!")
        for i in range(3):
            pswd = input("请输入您的密码: ")
            if pswd == data[2]:
                have_money = float(data[7])
                print("您有金额: ", have_money)
                user2 = input("请输入您要转账的用户名: ")
                cursor.execute("SELECT * FROM add_user where username=  '%s' " % user2)
                card2 = cursor.fetchone()
                if card2 is None:
                    return Return(1)
                else:
                    cursor.execute("SELECT * FROM add_user where username='%s' " % user2)
                    data1 = cursor.fetchone()
                    while True:
                        turn_money = float(input("请输入您要转的金额: "))
                        if turn_money > have_money:
                            print("对不起,您没有那么多钱,请重新输入")
                        else:
                            your_card_money = float(data[7]) - turn_money
                            his_card_money = float(data1[7]) + turn_money
                            cursor.execute(
                                "UPDATE add_user SET money = '%s' WHERE username = '%s' " % (your_card_money, user))
                            conn.commit()
                            cursor.execute(
                                "UPDATE add_user SET money = '%s' WHERE username = '%s' " % (his_card_money, user2))
                            conn.commit()
                            print("恭喜你转账成功,你还有", your_card_money, "元")
                            break
                break
            else:
                print("对不起,您输入的密码错误")

#返回值
def Return(num):
    if num == 1:
        print("您输入的用户名不对：")
    elif num == 2:
        print("您输入的密码不对：")
    elif num == 3:
        print("您的钱不够：")
    else :
        print("")




while True:
    begin = input("请选择业务")
    if begin =="1":#您输入的业务等于1执行开户操作
        adduser()
    elif begin == "2":
        getMoney()
    elif begin == "3":
        saveMoney()
    elif begin == "4":
        transferMoney()
    elif begin == "5":
        select()
    else:
        print("Byebye")
        break