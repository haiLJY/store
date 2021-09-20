import xlrd
wb = xlrd.open_workbook(filename=r"D:\Python自动化测试\python\python\day07\2020年每个月的销售情况.xlsx")

print("————————————————————————————————全年的销售总额————————————————————————————")
Ssum = 0
sum = 0
for m in range(0, 12):
    sheet = wb.sheet_by_index(m)
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(1, rows):
        data = sheet.row_values(i)
        total = data[2] * data[4]
        sum += total
    print(m+1, "月销售总额为￥", round(sum, 2))
Ssum += sum
print("全年的销售总额为￥", round(Ssum, 2))

print("——————————————————————每件衣服的销售（件数）占比————————————————————————————")
Ssum = 0
sum = sum1=sum2=sum3=sum4=sum5=sum6=sum7=sum8=sum9=sum10=sum11=sum12=0
for m in range(0, 12):
    sheet = wb.sheet_by_index(m)
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(1, rows):
        data = sheet.row_values(i)
        if data[1]=="羽绒服":
            sum += data[4]
        elif data[1]=="牛仔裤":
            sum1 += data[4]
        elif data[1] =="风衣":
            sum2 += data[4]
        elif data[1] =="皮草":
            sum3 += data[4]
        elif data[1] =="T血":
            sum4 += data[4]
        elif data[1] == "马甲":
            sum5 += data[4]
        elif data[1] == "小西装":
            sum6 += data[4]
        elif data[1] == "皮衣":
            sum7 += data[4]
        elif data[1] == "衬衫":
            sum8 += data[4]
        elif data[1] == "休闲裤":
            sum9 += data[4]
        elif data[1] == "卫衣":
            sum10 += data[4]
        elif data[1] == "棉衣":
            sum11 += data[4]
        else :
            sum12 +=data[4]
total=sum+sum1+sum2+sum3+sum4+sum5+sum6+sum7+sum8+sum9+sum10+sum11+sum12
print("羽绒服的销量占比为：", round(sum/total, 2))
print("牛仔裤的销量占为：",round(sum1/total, 2))
print("风衣的销量占比为：",round(sum2/total, 2))
print("皮草的销量占比为：",round(sum3/total, 2))
print("T血的销量占比为：",round(sum4/total, 2))
print("马甲的销量占比为：",round(sum5/total, 2))
print("小西装的销量占比为：",round(sum6/total, 2))
print("皮衣的销量占比为：",round(sum7/total, 2))
print("衬衫的销量占比为：",round(sum8/total, 2))
print("休闲裤的销量占比为：",round(sum9/total, 2))
print("卫衣的销量占比为：",round(sum10/total, 2))
print("棉衣的销量占比为：",round(sum11/total, 2))
print("铅笔裤的销量占比为：",round(sum12/total, 2))


print("————————————————————————————————————————————————每件衣服的月销售占比————————————————————————————————————————————————————————————————————")
Ssum = 0
sum = sum1=sum2=sum3=sum4=sum5=sum6=sum7=sum8=sum9=sum10=sum11=sum12=count = 0
percent = dict()
for m in range(1, 13):
    sheet = wb.sheet_by_name("%s月" % m)
    rows = sheet.nrows
    cols = sheet.ncols

    for i in range(1, rows):
        data = sheet.row_values(i)
        count += data[4]
        if data[1]=="羽绒服":
            sum += data[4]
        elif data[1]=="牛仔裤":
            sum1 += data[4]
        elif data[1] =="风衣":
            sum2 += data[4]
        elif data[1] =="皮草":
            sum3 += data[4]
        elif data[1] =="T血":
            sum4 += data[4]
        elif data[1] == "马甲":
            sum5 += data[4]
        elif data[1] == "小西装":
            sum6 += data[4]
        elif data[1] == "皮衣":
            sum7 += data[4]
        elif data[1] == "衬衫":
            sum8 += data[4]
        elif data[1] == "休闲裤":
            sum9 += data[4]
        elif data[1] == "卫衣":
            sum10 += data[4]
        elif data[1] == "棉衣":
            sum11 += data[4]
        else :
            sum12 += data[4]
        info = "%s月"
        percent[info % m] = {
            "羽绒服的销量占比为：": round(sum / count, 2),
            "牛仔裤的销量占比为：": round(sum1 / count, 2),
            "风衣的销量占比为：": round(sum2 / count, 2),
            "皮草的销量占比为：": round(sum3 / count, 2),
            "T血的销量占比为：": round(sum4 / count, 2),
            "马甲的销量占比为：": round(sum5 / count, 2),
            "小西装的销量占比为：": round(sum6 / count, 2),
            "皮衣的销量占比为：": round(sum7 / count, 2),
            "衬衫的销量占比为：": round(sum8 / count, 2),
            "休闲裤的销量占比为：": round(sum9 / count, 2),
            "卫衣的销量占比为：": round(sum10 / count, 2),
            "棉衣的销量占比为：": round(sum11 / count, 2),
            "铅笔裤的销量占比为：": round(sum12 / count, 2),
            "本月销售总量": count
        }
for key,value in percent.items():
    print(key,value)

print("——————————————————————————每件衣服的销售额占比——————————————————————————————————————————————————")
Ssum = 0
sum = sum1=sum2=sum3=sum4=sum5=sum6=sum7=sum8=sum9=sum10=sum11=sum12=0
for m in range(0, 12):
    sheet = wb.sheet_by_index(m)
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(1, rows):
        data = sheet.row_values(i)
        if data[1]=="羽绒服":
            sum += data[2]*data[4]
        elif data[1]=="牛仔裤":
            sum1 += data[2]*data[4]
        elif data[1] =="风衣":
            sum2 += data[2]*data[4]
        elif data[1] =="皮草":
            sum3 += data[2]*data[4]
        elif data[1] =="T血":
            sum4 += data[2]*data[4]
        elif data[1] == "马甲":
            sum5 += data[2]*data[4]
        elif data[1] == "小西装":
            sum6 += data[2]*data[4]
        elif data[1] == "皮衣":
            sum7 += data[2]*data[4]
        elif data[1] == "衬衫":
            sum8 += data[2]*data[4]
        elif data[1] == "休闲裤":
            sum9 += data[2]*data[4]
        elif data[1] == "卫衣":
            sum10 += data[2]*data[4]
        elif data[1] == "棉衣":
            sum11 += data[2]*data[4]
        else :
            sum12 += data[2]*data[4]
total=sum+sum1+sum2+sum3+sum4+sum5+sum6+sum7+sum8+sum9+sum10+sum11+sum12
print("羽绒服的销量占比为：", round(sum/total, 2))
print("牛仔裤的销量占为：",round(sum1/total, 2))
print("风衣的销量占比为：",round(sum2/total, 2))
print("皮草的销量占比为：",round(sum3/total, 2))
print("T血的销量占比为：",round(sum4/total, 2))
print("马甲的销量占比为：",round(sum5/total, 2))
print("小西装的销量占比为：",round(sum6/total, 2))
print("皮衣的销量占比为：",round(sum7/total, 2))
print("衬衫的销量占比为：",round(sum8/total, 2))
print("休闲裤的销量占比为：",round(sum9/total, 2))
print("卫衣的销量占比为：",round(sum10/total, 2))
print("棉衣的销量占比为：",round(sum11/total, 2))
print("铅笔裤的销量占比为：",round(sum12/total, 2))

print("——————————————————————最畅销的衣服是哪种，全年销量最低的衣服——————————————————")
Ssum = 0
sum = sum1=sum2=sum3=sum4=sum5=sum6=sum7=sum8=sum9=sum10=sum11=sum12=count = 0
dict={}
for m in range(1, 13):
    sheet = wb.sheet_by_name("%s月" % m)
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(1, rows):
        data = sheet.row_values(i)
        if data[1]=="羽绒服":
            sum += data[4]
            dict[data[1]] = sum
        elif data[1]=="牛仔裤":
            sum1 += data[4]
            dict[data[1]] = sum1
        elif data[1] =="风衣":
            sum2 += data[4]
            dict[data[1]] = sum2
        elif data[1] =="皮草":
            sum3 += data[4]
            dict[data[1]] = sum3
        elif data[1] =="T血":
            sum4 += data[4]
            dict[data[1]] = sum4
        elif data[1] == "马甲":
            sum5 += data[4]
            dict[data[1]] = sum5
        elif data[1] == "小西装":
            sum6 += data[4]
            dict[data[1]] = sum6
        elif data[1] == "皮衣":
            sum7 += data[4]
            dict[data[1]] = sum7
        elif data[1] == "衬衫":
            sum8 += data[4]
            dict[data[1]] = sum8
        elif data[1] == "休闲裤":
            sum9 += data[4]
            dict[data[1]] = sum9
        elif data[1] == "卫衣":
            sum10 += data[4]
            dict[data[1]] = sum10
        elif data[1] == "棉衣":
            sum11 += data[4]
            dict[data[1]] = sum11
        else :
            sum12 += data[4]
            dict[data[1]] = sum12

print("最畅销的衣服为：",max(dict,key=dict.get))
print("销量最低的衣服为：",min(dict,key=dict.get))

print("————————————————————————每个季度最畅销的衣服————————————————————————————————")
sum00 = sum001=sum002=sum003=sum04=sum05=sum06=sum07=sum08=sum09=sum010=sum011=sum012=0
dict1={}
for m in range(1,4):
    sheet = wb.sheet_by_index(m)
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(1, rows):
        data = sheet.row_values(i)
        if data[1]=="羽绒服":
            sum00 += data[4]
            dict1[data[1]] = sum00
        elif data[1]=="牛仔裤":
            sum001 += data[4]
            dict1[data[1]] = sum001
        elif data[1] =="风衣":
            sum002 += data[4]
            dict1[data[1]] = sum002
        elif data[1] =="皮草":
            sum003 += data[4]
            dict1[data[1]] = sum003
        elif data[1] =="T血":
            sum04 += data[4]
            dict1[data[1]] = sum04
        elif data[1] == "马甲":
            sum05 += data[4]
            dict1[data[1]] = sum05
        elif data[1] == "小西装":
            sum06 += data[4]
            dict1[data[1]] = sum06
        elif data[1] == "皮衣":
            sum07 += data[4]
            dict1[data[1]] = sum07
        elif data[1] == "衬衫":
            sum08 += data[4]
            dict1[data[1]] = sum08
        elif data[1] == "休闲裤":
            sum09 += data[4]
            dict1[data[1]] = sum09
        elif data[1] == "卫衣":
            sum010 += data[4]
            dict1[data[1]] = sum010
        elif data[1] == "棉衣":
            sum011 += data[4]
            dict1[data[1]] = sum011
        else :
            sum012 += data[4]
            dict1[data[1]] = sum012
print("第一季度最畅销的衣服为：",max(dict1,key=dict1.get))
dict2={}
sum01 = sum11=sum21=sum31=sum41=sum51=sum61=sum71=sum81=sum91=sum101=sum111=sum121=count = 0
for m in range(4,7) :
    sheet = wb.sheet_by_index(m)
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(1, rows):
        data = sheet.row_values(i)
        if data[1]=="羽绒服":
            sum += data[4]
            dict2[data[1]] = sum01
        elif data[1]=="牛仔裤":
            sum11 += data[4]
            dict2[data[1]] = sum11
        elif data[1] =="风衣":
            sum21 += data[4]
            dict2[data[1]] = sum21
        elif data[1] =="皮草":
            sum31 += data[4]
            dict2[data[1]] = sum31
        elif data[1] =="T血":
            sum41 += data[4]
            dict2[data[1]] = sum41
        elif data[1] == "马甲":
            sum51 += data[4]
            dict2[data[1]] = sum51
        elif data[1] == "小西装":
            sum61 += data[4]
            dict2[data[1]] = sum61
        elif data[1] == "皮衣":
            sum71 += data[4]
            dict2[data[1]] = sum71
        elif data[1] == "衬衫":
            sum81 += data[4]
            dict2[data[1]] = sum81
        elif data[1] == "休闲裤":
            sum91 += data[4]
            dict2[data[1]] = sum91
        elif data[1] == "卫衣":
            sum101 += data[4]
            dict2[data[1]] = sum101
        elif data[1] == "棉衣":
            sum111 += data[4]
            dict2[data[1]] = sum111
        else :
            sum121 += data[4]
            dict2[data[1]] = sum121
print("第二季度最畅销的衣服为：",max(dict2,key=dict2.get))
dict3={}
sum02 = sum1a2=sum22=sum32=sum42=sum52=sum62=sum72=sum82=sum92=sum102=sum112=sum122=count = 0
for m in range(7,10):
    sheet = wb.sheet_by_index(m)
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(1, rows):
        data = sheet.row_values(i)
        if data[1]=="羽绒服":
            sum02 += data[4]
            dict3[data[1]] = sum02
        elif data[1]=="牛仔裤":
            sum1a2 += data[4]
            dict3[data[1]] = sum1a2
        elif data[1] =="风衣":
            sum22 += data[4]
            dict3[data[1]] = sum22
        elif data[1] =="皮草":
            sum32 += data[4]
            dict3[data[1]] = sum32
        elif data[1] =="T血":
            sum42 += data[4]
            dict3[data[1]] = sum42
        elif data[1] == "马甲":
            sum52 += data[4]
            dict3[data[1]] = sum52
        elif data[1] == "小西装":
            sum62 += data[4]
            dict3[data[1]] = sum62
        elif data[1] == "皮衣":
            sum72 += data[4]
            dict3[data[1]] = sum72
        elif data[1] == "衬衫":
            sum82 += data[4]
            dict3[data[1]] = sum82
        elif data[1] == "休闲裤":
            sum92 += data[4]
            dict3[data[1]] = sum92
        elif data[1] == "卫衣":
            sum102 += data[4]
            dict3[data[1]] = sum102
        elif data[1] == "棉衣":
            sum112 += data[4]
            dict3[data[1]] = sum112
        else :
            sum122 += data[4]
            dict3[data[1]] = sum122
print("第三季度最畅销的衣服为：",max(dict3,key=dict3.get))
dict4={}
sum03 = sum1a3=sum23=sum33=sum43=sum53=sum63=sum73=sum83=sum93=sum103=sum113=sum123=0
for m in range(10,12) and range(0,1):
    sheet = wb.sheet_by_index(m)
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(1, rows):
        data = sheet.row_values(i)
        if data[1]=="羽绒服":
            sum03 += data[4]
            dict4[data[1]] = sum03
        elif data[1]=="牛仔裤":
            sum1a3 += data[4]
            dict4[data[1]] = sum1a3
        elif data[1] =="风衣":
            sum23 += data[4]
            dict4[data[1]] = sum23
        elif data[1] =="皮草":
            sum33 += data[4]
            dict4[data[1]] = sum33
        elif data[1] =="T血":
            sum43 += data[4]
            dict4[data[1]] = sum43
        elif data[1] == "马甲":
            sum53 += data[4]
            dict4[data[1]] = sum53
        elif data[1] == "小西装":
            sum63 += data[4]
            dict4[data[1]] = sum63
        elif data[1] == "皮衣":
            sum73 += data[4]
            dict4[data[1]] = sum73
        elif data[1] == "衬衫":
            sum83 += data[4]
            dict4[data[1]] = sum83
        elif data[1] == "休闲裤":
            sum93 += data[4]
            dict4[data[1]] = sum93
        elif data[1] == "卫衣":
            sum103 += data[4]
            dict4[data[1]] = sum103
        elif data[1] == "棉衣":
            sum113 += data[4]
            dict4[data[1]] = sum113
        else :
            sum123 += data[4]
            dict4[data[1]] = sum123
print("第四季度最畅销的衣服为：",max(dict4,key=dict4.get))






