#dict = {"k1":"v1","k2":"v2","k3":"v3"}
#循环出遍历所有的key
'''for key in dict.keys():
    print(key)'''

#循环出遍历所有的value
'''for value in dict.values():
    print(value)'''
#在字典中增加一个键值对,"k4":"v4"
'''dict['k4'] = "v4"
print (dict['k4'])'''
#水果存入字典  名称为key，金额value
'''info = {"苹果":32.8,"香蕉":22,"葡萄":15.5}
for key,value in info.items():
    print(key,value)

 '''

#小明和小刚购买水果
fruits = {"苹果":12.3,"草莓":4.5,"香蕉":6.3,"葡萄":5.8,"橘子":6.4,"樱桃":15.8}
info = {"小明":{"fruits":{"苹果":4,"草莓":13,"香蕉":10}},
        "小刚":{"fruits":{"葡萄":19,"橘子":12,"樱桃":30}}}
a=info["小明"]["fruits"]["苹果"]*fruits["苹果"]
b=info["小明"]["fruits"]["草莓"]*fruits["草莓"]
c=info["小明"]["fruits"]["香蕉"]*fruits["香蕉"]
d=info["小刚"]["fruits"]["葡萄"]*fruits["葡萄"]
e=info["小刚"]["fruits"]["橘子"]*fruits["橘子"]
f=info["小刚"]["fruits"]["樱桃"]*fruits["樱桃"]
money1=a+b+c
money2=d+e+f
info["小明"]["money"] = money1
info["小刚"]["money"] = money2
for key,value in info.items():
    print(key,value)



#编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
'''from collections import Counter
list = [21,56,10,56,56,10,21,10,21,56,56,56,56,56,56]
num_count=Counter(list)
print(num_count)
def count(list):
    return count(list)
    print(count(list))'''

#有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
'''names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]'''
'''print("姓名  年龄  性别  编号   任职公司   薪资   部门编号")
dict={}
dict["刘备"]=" 56   男   106     IBM      500     50"
dict["大乔"]=" 19   女   230     微软      501     60"
dict["小乔"]=" 19   女   210   Oracle     600     60"
dict["张飞"]=" 45   男   230   Tencent    700     10"
for key,value in dict.items():
    print(key,value)
'''













