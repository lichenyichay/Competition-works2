# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2022/12/24 15:04
# @FILE:main.py
# @Software:IDLE 3.9.6

import math,os,
from menu import *
from xiaogongju import *
from tuxing_cal import *
from calculator import *
from math_cal_py import *
'''
函数名：main
:return 无
作用：主程序
'''
def main():
    while True:
        os.system("cls")
        menu()
        try:
            a = int(input("请输入序号："))
            if a == 1:
                while True:
                    os.system("cls")
                    xiaogongjumenu()
                    try:
                        xuhao = int(input("请输入序号："))
                        if xuhao == 1:
                            c = int(input("请输入最小值："))
                            d = int(input("请输入最大值："))
                            while True:
                                try:
                                    e = input("请输入模式（二进制：bin;八进制：oct,十进制：int，十六进制：hex）：")
                                    print(randomint(d,c,e))
                                    break
                                except Exception as e:
                                    print(repr(e))
                        elif xuhao == 2:
                            e = input("请输入服务：（可选项：大写转小写，小写转大写）")
                            while True:
                                if e == "大写转小写":
                                    try:
                                        daorxiao("datoxiao")
                                        break
                                    except Exception as e:
                                        print(rept(e))
                                elif e == "小写转大写":
                                    try:
                                        daorxiao("xiaotoda")
                                        break
                                    except Exception as e:
                                        print(repr(e))
                                else:
                                    pass
                        elif xuhao == 3:
                            while True:
                                try:
                                    f = int(input("请输入第一个数据："))
                                    g = int(input("请输入第二个数据："))
                                    print(twonumbers_TheBiggestCommonfactor(f,g))
                                    break
                                except Exception as e:
                                    print(repr(e))
                        elif xuhao == 4:
                            while True:
                                try:
                                    h = int(input("请输入第一个数据："))
                                    i = int(input("请输入第二个数据："))
                                    print(twonumbers_TheMinimumCommonmultiple(h,i))
                                    break
                                except Exception as e:
                                    print(repr(e))
                        elif xuhao == 5:
                            while True:
                                try:     
                                    w1 = int(input("被除数："))
                                    w2 = int(input("除数："))
                                    w3 = w1 % w2
                                    print(w3)
                                    break
                                except Exception as e:
                                    print(repr(e))
                        elif xuhao == 6:
                            while True:
                                try:
                                    w1 = float(input("请输入要取整的数"))
                                    print(int(w1))
                                    break
                                except Exception as e:
                                    print(repr(e))
                        elif xuhao == 7:
                            while True:
                                try:
                                    w1 = float(input("请输入要取整的数"))
                                    print(int(w1)+1)
                                    break
                                except Exception as e:
                                    print(repr(e))
                        elif xuhao == 8:
                            try:
                                b = []
                                c = int(input("请输入元素个数："))
                                for i in range(c):
                                    d = float(input("请输入元素："))
                                    b.append(d)
                                b = tuple(b)
                                b = math.fsum(b)
                                print(b)
                            except Exception as e:
                                print(repr(e))
                        elif xuhao == 9:
                            try:
                                b = 0
                                c = int(input("请输入元素个数："))
                                e = []
                                for i in range(c):
                                    d = float(input("请输入元素："))
                                    e.append(d)
                                b = e[0]
                                for i in range(c-1):
                                    b -= e[1+i]
                                print(b)
                            except Exception as e:
                                print(repr(e))
                        elif xuhao == 10:
                            try:
                                b = 0
                                c = int(input("请输入元素个数："))
                                e = []
                                for i in range(c):
                                    d = float(input("请输入元素："))
                                    e.append(d)
                                b = e[0]
                                for i in range(c-1):
                                    b *= e[1+i]
                                print(b)
                            except Exception as e:
                                print(repr(e))
                        elif xuhao == 11:
                            break
                        else:
                            print("序号错误！")
                    except Exception as e:
                        print(repr(e))
            elif a == 2:
                huida = input("请输入计算对象：")
                tuxing(huida)
            elif a == 3:
                while True:
                    os.system("cls")
                    calculatormenu()
                    try:
                        xuhao = int(input("请输入序号："))
                        if xuhao == 1:
                            while True:
                                os.system("cls")
                                int_float_cal_menu()
                                try:
                                    xuhao1 = int(input("请输入序号"))
                                    if xuhao1 == 1:
                                        eee = float(input("第一个加数："))
                                        aaa = float(input("第二个加数："))
                                        qqq = eee + aaa
                                        print("等于",qqq)
                                    elif xuhao1 == 2:
                                        www = float(input("被减数："))
                                        rrr = float(input("减数："))
                                        sss = www - rrr
                                        print("等于",sss)
                                    elif xuhao1 == 3:
                                        eee = float(input("第一个加数："))
                                        aaa = float(input("第二个加数："))
                                        qqq = eee * aaa
                                        print("等于",sss)
                                    elif xuhao1 == 4:
                                        eee = float(input("第一个加数："))
                                        aaa = float(input("第二个加数："))
                                        qqq = eee / aaa
                                        print("等于",sss)
                                    elif xuhao1 == 5:
                                        break
                                    else:
                                        print("序号错误！")
                                except Exception as e:
                                    print(repr(e))
                        elif xuhao == 2:
                            while True:
                                os.system("cls")
                                fractions_menu()
                                try:
                                    xuhao1 = int(input("请输入序号"))
                                    if xuhao1 == 1:
                                        while True:
                                            try:
                                                qw = int(input("分母1："))
                                                sd = int(input("分子1："))
                                                ad = int(input("分母2："))
                                                df = int(input("分子2："))
                                                sva = (sd/qw)+(df/ad)
                                                print("等于",sva)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 2:
                                        while True:
                                            try:
                                                qw = int(input("分母1："))
                                                sd = int(input("分子1："))
                                                ad = int(input("分母2："))
                                                df = int(input("分子2："))
                                                sva = (sd/qw)-(df/ad)
                                                print("等于",sva)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 3:
                                        while True:
                                            try:
                                                qw = int(input("分母1："))
                                                sd = int(input("分子1："))
                                                ad = int(input("分母2："))
                                                df = int(input("分子2："))
                                                sva = (sd/qw)*(df/ad)
                                                print("等于",sva)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 4:
                                        while True:
                                            try:
                                                qw = int(input("分母1："))
                                                sd = int(input("分子1："))
                                                ad = int(input("分母2："))
                                                df = int(input("分子2："))
                                                sva = (sd/qw)/(df/ad)
                                                print("等于",sva)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 5:
                                        break
                                    else:
                                        print("序号错误！")
                                except Exception as e:
                                    print(repr(e))
                        elif xuhao == 3:
                            while True:
                                try:
                                    a1 = float(input("第一个数："))
                                    a2 = float(input("第二个数："))
                                    if a1 > a2:
                                        print(a1,">",a2)
                                    if a1 < a2:
                                        print(a1,"<",a2)
                                    if a1 == a2:
                                        print(a1,"=",a2)
                                    break
                                except Exception as e:
                                    print(repr(e))
                        elif xuhao == 4:
                            while True:
                                try:
                                    q1 = int(input("你出生的年份："))
                                    q2 = int(input("现在的年份："))
                                    q3 = q2 -q1
                                    print("你现在是",q3,"岁")
                                    break
                                except Exception as e:
                                    print(repr(e))
                        elif xuhao == 5:
                            while True:
                                try:
                                    ws1 = int(input("要开平方的数："))
                                    we2 = ws1**0.5
                                    print("平方是：",we2)
                                    break
                                except Exception as e:
                                    print(repr(e))
                            
                        elif xuhao == 6:
                            while True:
                                try:
                                    choose = int(input("请输入序号（1：华氏度转摄氏度，2：摄氏度转华氏度）："))
                                    if choose == 1:
                                        while True:
                                            try:
                                                Ftemp = float(input("请输入华氏度温度："))
                                                print(FtemporCtemp("℉to℃",Ftemp))
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                        break
                                    elif choose == 2:
                                        while True:
                                            try:
                                                Ctemp = float(input("请输入摄氏度温度："))
                                                print(FtemporCtemp("℃to℉",Ctemp))
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                        break
                                    else:
                                        print("序号无效！")
                                    
                                except Exception as e:
                                    print(repr(e)) 
                        elif xuhao == 7:
                            while True:
                                os.system("cls")
                                hybrid_computing_menu()
                                try:
                                    xuhao1 = int(input("请输入序号"))
                                    if xuhao1 == 1:
                                        while True:
                                            try:
                                                az = float(input("第一个加数："))
                                                qa = float(input("第二个加数："))
                                                qz = float(input("减数："))
                                                qwe = az + qa - qz
                                                print("等于：",qwe)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 2:
                                        while True:
                                            try:
                                                qwert = float(input("第一个加数："))
                                                asdfg = float(input("第二个加数："))
                                                zxcvb = float(input("乘数："))
                                                qaws = (qwert + asdfg) * zxcvb
                                                print("等于",qaws)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 3:
                                        while True:
                                            try:
                                                qw1 = float(input("第一个加数："))
                                                qw2 = float(input("第二个加数："))
                                                qw3 = float(input("除数："))
                                                qw4 = (qw1 + qw2) / qw3
                                                print("等于：",qw4)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 4:
                                        while True:
                                            try:
                                                wa_1 = float(input("被减数："))
                                                wa_2 = float(input("减数："))
                                                wa_3 = float(input("加数："))
                                                wa_4 = wa_1 - wa_2 + wa_3
                                                print("等于：",wa_4)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 5:
                                        while True:
                                            try:
                                                az = float(input("被减数："))
                                                ax = float(input("减数："))
                                                ac = float(input("乘数："))
                                                av = (az - ax) *ac
                                                print("等于：",av)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 6:
                                        while True:
                                            try:
                                                sz = float(input("被减数："))
                                                sx = float(input("减数："))
                                                sc = float(input("除数："))
                                                sv = (sz - sx) / sc
                                                print("等于：",sv)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 7:
                                        while True:
                                            try:
                                                milk = float(input("第一个乘数："))
                                                start = float(input("第二个乘数："))
                                                all = float(input("加数："))
                                                one = milk * start + all
                                                print("等于：",one)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 8:
                                        while True:
                                            try:
                                                two = float(input("第一个乘数："))
                                                to = float(input("第二个乘数："))
                                                too = float(input("减数："))
                                                fors = two * to - too
                                                print("等于：",fors)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 9:
                                        while True:
                                            try:
                                                you = float(input("第一个乘数："))
                                                I = float(input("第二个乘数："))
                                                he = float(input("除数："))
                                                she = you * I / he
                                                print("等于：",she)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 10:
                                        while True:
                                            try:
                                                _1 = float(input("被除数："))
                                                _2 = float(input("除数："))
                                                _3 = float(input("加数："))
                                                _4 = _1 / _2 + _3
                                                print("等于：",_4)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 11:
                                        while True:
                                            try:
                                                sk1 = float(input("被除数："))
                                                sk2 = float(input("除数："))
                                                sk3 = float(input("减数："))
                                                sk4 = sk1 / sk2 - sk3
                                                print("等于：",sk4)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 12:
                                        while True:
                                            try:
                                                fish = float(input("被除数："))
                                                water = float(input("除数："))
                                                mm = float(input("乘数："))
                                                mu = fish / water * mm
                                                print("等于：",mu)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 13:
                                        while True:
                                            try:
                                                mum = float(input("被除数："))
                                                dad = float(input("第一个除数："))
                                                sister = float(input("第二个除数："))
                                                brother = mum / dad / sister
                                                print("等于：",brother)
                                                break
                                            except Exception as e:
                                                print(repr(e))
                                    elif xuhao1 == 14:
                                        break
                                    else:
                                        print("序号错误！")
                                except Exception as e:
                                    print(repr(e))
                        elif xuhao == 8:
                            while True:
                                os.system("cls")
                                currency_conversion_menu()
                                try:
                                    choose = int(input("请输入序号："))
                                    if choose <= 16 and choose > 0:
                                        int1 = float(input("请输入金额："))
                                        print(duihuan(choose,int1))
                                    elif choose == 17:
                                        break
                                except Exception as e:
                                    print(repr(e))
                        elif xuhao == 9:
                            while True:
                                try:
                                    sdf = float(input("数："))
                                    z = int(input("次方根："))
                                    z = z/z/z
                                    ghj = sdf ** z
                                    print("等于",ghj)
                                    break
                                except Exception as e:
                                    print(repr(e))
                        elif xuhao == 10:
                            break
                        else:
                            print("序号错误！")
                    except Exception as e:
                        print(repr(e))
            elif a == 4:
                while True:
                    mathmenu()
                    try:
                        choose = int(input("请输入序号："))
                        if choose in [1,10,12,13]:
                            while True:
                                try:
                                    g = float(input("请输入第一个参数："))
                                    h = float(input("请输入第二个参数："))
                                    print(math_cal(choose,g,h))
                                    break
                                except Exception as e:
                                    print(repr(e))
                        elif choose in [2,3,6,7,8,9,11,14,15,16,17,18,19]:
                            while True:
                                try:
                                    g = float(input("请输入参数："))
                                    print(math_cal(choose,g,0))
                                    break
                                except Exception as e:
                                    print(repr(e))
                        elif choose in [4,5]
                            print(math_cal(choose,0,0))
                        elif choose == 20:
                            break
                        else:
                            print("序号错误！")
                        
                    except Exception as e:
                        print(repr(e))
            elif a == 5:
                break
            else:
                print("序号错误！")
                time.sleep(5)
        except Exception as e:
            print(repr(e))
    print("感谢你的使用！希望学生们早日完成作业！再见！")
if __name__ == "__main__":
    main()
