import random,math,os,time
def menu():
    print("------多功能一体机------")
    print("序号          功能")
    print("1             小工具合集")
    print("2             图形计算器")
    print("3             多功能计算器")
    print("4             math库专用计算器")
    print("5             退出")

def xiaogongjumenu():
    print("------小工具合集------")
    print("序号          功能")
    print("1             抽取随机数")
    print("2             大小写转换")
    print("3             求最大公因数")
    print("4             求最小公倍数")
    print("5             取余")
    print("6             向下取整")
    print("7             向上取整")
    print("8             多个数求和")
    print("9             多个数求差")
    print("10            多个数求积")
    print("11            返回上一级")

def calculatormenu():
    print("------多功能计算器------")
    print("序号          功能")
    print("1             整数、小数计算（加减乘除）")
    print("2             分数计算（加减乘除）")
    print("3             比大小")
    print("4             年龄计算")
    print("5             开平方")
    print("6             华氏度摄氏度转换")
    print("7             混合运算")
    print("8             货币换算")
    print("9             次方根")
    print("10            返回上一级")
def xuhao1_menu():
    print("------整数、小数计算（加减乘除）------")
    print("序号             功能")
    print("1                加法")
    print("2                减法")
    print("3                乘法")
    print("4                除法")
    print("5                返回上一级")
def xuhao2_menu():
    print("------分数计算（加减乘除）------")
    print("序号             功能")
    print("1                加法")
    print("2                减法")
    print("3                乘法")
    print("4                除法")
    print("5                返回上一级")
def xuhao7_menu():
    print("------混合运算------")
    print("序号             功能")
    print("1                +-混合运算")
    print("2                +*混合运算")
    print("3                +/混合运算")
    print("4                -+混合运算")
    print("5                -*混合运算")
    print("6                -/混合运算")
    print("7                *+混合运算")
    print("8                *-混合运算")
    print("9                */混合运算")
    print("10               /+混合运算")
    print("11               /-混合运算")
    print("12               /*混合运算")
    print("13               //混合运算")
    print("14               返回上一级")
def xuhao8_menu():
    print("------货币转换------")
    print("序号             功能")
    print("1                CNY（人民币）->USD（美元）")
    print("2                CNY（人民币）->JPY（日元）")
    print("3                USD（美元）->CNY（人民币）")
    print("4                USD（美元）->JPY（日元）")
    print("5                JPY（日元）->CNY（人民币）")
    print("6                JPY（日元）->USD（美元）")
    print("7                CNY（人民币）->MOP（澳门元）")
    print("8                MOP（澳门元）->CNY（人民币）")
    print("9                CNY（人民币）->HKD（港元）")
    print("10               HKD（港元）->CNY（人民币）")
    print("11               CNY（人民币）->TWD（台币）")
    print("12               TWD（台币）->CNY（人民币）")
    print("13               CNY（人民币）->GBP（英镑）")
    print("14               GBP（英镑）->CNY（人民币）")
    print("15               CNY（人民币）->EUR（欧元）")
    print("16               EUR（欧元）->CNY（人民币）")
    print("17               返回上一级")

def mathmenu():
    print("------math库计算器------")
    print("序号             功能")
    print("1                把y的正负号加到x的前面")
    print("2                求x的余弦")
    print("3                弧度x转换成角度")
    print("4                求数学常量e"")
    print("5                求数学常量pi")
    print("6                求x的正切值")
    print("7                求x的平方根")
    print("8                求x的正弦值")
    print("9                角度x转换成弧度")
    print("10               求x的y次方")
    print("11               输出由x的小数部分和整数部分组成的元组")
    print("12               求x以a为底的对数")
    print("13               求x*（2**i）的值")
    print("14               求x是不是数字")
    print("15               求x是不是正无穷大或负无穷大")
    print("16               求x的阶乘")
    print("17               求x的绝对值")
    print("18               求math.e的x次方-1")
    print("19               求math.e的x次方")
    print("20               返回上一级")

def randomint(maxint,minint,mode):
    b = random.randint(minint,maxint)
    if mode == "bin":
        return bin(b)
    elif mode == "oct":
        return oct(b)
    elif mode == "int":
        return b
    elif mode == "hex":
        return hex(b)
    else:
        raise TypeError("TypeError:模式错误！")
def daorxiao(mode):
    zifugeshu = int(input("请输入字符个数"))
    if mode == "datoxiao":
        if zifugeshu > 1:
            for i in range(zifugeshu):
                zifu = input("请输入第" + str(i + 1) + "个字符")
                # zifu1 = ord(zifu)
                zifu1 = ord(zifu) + 32
                zifu1 = chr(zifu1)
                zongzifu = []
                zongzifu.append(zifu1)
            print("转换结果：",end = '')
            for j in zongzifu:
                print(j)
        else:
            zifu = input("请输入字符：")
            zifu1 = ord(zifu)
            zifu1 = zifu1 + 32
            zifu1 = chr(zifu1)
            print("转换结果：" + zifu1)
    elif mode == "xiaotoda":
        if zifugeshu > 1:
            for i in range(zifugeshu):
                zifu = input("请输入第" + str(i + 1) + "个字符")
                # zifu1 = ord(zifu)
                zifu1 = ord(zifu) - 32
                zifu1 = chr(zifu1)
                zongzifu = []
                zongzifu.append(zifu1)
            print("转换结果：",end = '')
            for j in zongzifu:
                print(j)
        else:
            zifu = input("请输入字符：")
            zifu1 = ord(zifu)
            zifu1 = zifu1 - 32
            zifu1 = chr(zifu1)
            print("转换结果：" + zifu1)
    else:
        raise Exception("Error:模式错误!")
def tuxing(huida):
    while True:
        if huida == "长方体":
            huida1 = input("请输入计算的是体积、表面积、棱长总和、容积还是染色问题（包含底面，且长宽高均为整数）：")
            huida2 = float(input("请输入长："))
            huida3 = float(input("请输入宽："))
            huida4 = float(input("请输入高："))
            if huida1 == "体积":
                shuchu = huida2 * huida3 * huida4
                print("体积是：" + str(shuchu))
            elif huida1 == "表面积":
                shuchu = (huida2 * huida3 + huida2 * huida4 + huida3 * huida4) * 2
                print("表面积是：" + str(shuchu))
            elif huida1 == "染色问题":
                huida2 = int(huida2)
                huida3 = int(huida3)
                huida4 = int(huida4)
                if huida4 == 1:
                    print("4个面染色的小正方体有4个。")
                    print("3个面染色的小正方体有" + str((huida2 - 2) * 2 + (huida3 - 2) * 2) + "个。")
                    print("2个面染色的小正方体有" + str((huida2 - 2) * (huida3 - 2)) + "个。")
                else:
                    print("3个面染色的小正方体有8个。")
                    print("2个面染色的小正方体有" + str(((huida2-2)+(huida3-2)+(huida4-2))*4) +"个。")
                    print("1个面染色的小正方体有" + str(((huida2-2)*(huida3-2)+(huida2-2)*(huida4-2)+(huida3-2)*(huida4-2))*2) + "个。")
                    print("0个面染色的小正方体有" + str((huida2-2)*(huida3-2)*(huida4-2)) + "个")
            elif huida1 == "棱长总和":
                shuchu = (huida2+huida3+huida4)*4
                print("棱长总和是：" + str(shuchu))
            elif huida1 == "容积":
                shuchu = huida2*huida3*huida4
                print("容积是：" + str(shuchu))
            else:
                print("不支持此功能")
        elif huida == "正方体":
            huida1 = input("请输入计算的是体积、表面积、棱长总和、容积还是染色问题（包含底面，且长宽高均为整数）：")
            huida2 = float(input("请输入棱长："))
            if huida1 == "体积":
                shuchu = huida2 ** 3
                print("体积是：" + str(shuchu))
            elif huida1 == "表面积":
                shuchu = huida2 ** 2 * 6
                print("表面积是" + str(shuchu))
            elif huida1 == "棱长总和":
                shuchu = huida2 * 12
                print("棱长总和" + str(shuchu))
            elif huida1 == "容积":
                shuchu = huida2 ** 3
                print("容积是：" + str(shuchu))
            elif huida1 == "染色问题":
                huida2 = int(huida2)
                if huida2 == 1:
                    print("6个面染色的小正方体有1个")
                else:
                    print("3个面染色的小正方体有8个。")
                    print("2个面染色的小正方体有" + str((huida2-2)*12) + "个。")
                    print("1个面染色的小正方体有" + str((huida2-2)**2*6) + "个。")
                    print("0个面染色的小正方体有" + str((huida2-2)**3) + "个。")
            else:
                print("不支持此功能")
        elif huida == "正方形":
            huida1 = input("请输入计算的是面积、边长之和还是折纸盒问题（剪掉的只能是小正方形）：")
            huida2 = float(input("请输入边长："))
            if huida1 == "面积":
                shuchu = huida2**2
                print("面积是：" + str(shuchu))
            elif huida1 == "边长之和":
                shuchu = huida2*4
                print("边长之和是：" + str(shuchu))
            elif huida1 == "折纸盒问题":
                huida3 = float(input("请输入被剪掉的小正方形的边长："))
                V = (huida2-2*huida3)**2
                S = huida2**2-((huida3**2)*4)
                print("体积是：" + str(V) + "表面积是：" + str(S))
            else:
                print("不支持此功能！")
        elif huida == "长方形":
            huida1 = input("请输入计算的是面积、周长还是折纸盒问题（剪掉的只能是小正方形）：")
            huida2 = float(input("请输入长："))
            huida3 = float(input("请输入宽："))
            if huida1 == "面积":
                shuchu = huida2*huida3
                print("面积是：" + str(shuchu))
            elif huida1 == "周长":
                shuchu = (huida2+huida3)*2
                print("周长是：" + str(shuchu))
            elif huida1 == "折纸盒问题":
                huida4 = float(input("请输入被剪掉的小正方形的边长："))
                V = (huida2-(2*huida4))*(huida3-(2*huida4))
                S = huida2*huida3-(huida4**2*4)
                print("体积是：" + str(V) + "表面积是：" + str(S))
            else:
                print("不支持此功能！")
        elif huida == "平行四边形":
            huida1 = int(input("请输入要计算的是面积、周长还是折纸盒问题（剪掉的必须是平行四边形，且平行四边形的四条边长度均相等）"))
            huida2 = float(input("请输入底："))
            huida3 = float(input("请输入高："))
            huida4 = float(input("请输入斜边的长度："))
            if huida1 == "面积":
                shuchu = huida2*huida3
                print("面积是：" + str(shuchu))
            elif huida1 == "周长":
                shuchu = (huida2+huida4)*2
                print("周长是：" + str(shuchu))
            elif huida1 == "折纸盒问题":
                huida5 = float(input("请输入被剪掉的平行四边形的边长："))
                S = huida2*huida3-(huida4**2)*4
                V = huida5*((huida4-2*huida5)*(huida2-2*huida5))
                print(f"体积是：{str(V)},表面积是：{str(S)}")
            else:
                print("不支持此功能！")
        elif huida == "菱形":
            huida1 = input("请输入要计算的是面积还是周长：")
            huida2 = float(input("请输入底："))
            huida3 = float(input("请输入高："))
            if huida1 == "面积":
                shuchu = huida2*huida3
                print(f"面积是：{str(shuchu)}")
            elif huida1 == "周长":
                shuchu = huida2*4
                print(f"周长是：{str(shuchu)}")
            else:
                print("不支持此功能！")
        elif huida == "三角形":
            huida1 = input("请输入要计算的是面积还是周长：")
            huida2 = float(input("请输入底："))
            huida3 = float(input("请输入高："))
            if huida1 == "面积":
                shuchu = huida2*huida3/2
                print(f"面积是：{str(shuchu)}")
            elif huida1 == "周长":
                huida4 = float(input("请输入其中1条腰长："))
                huida5 = float(input("请输入另1条腰长："))
                shuchu = huida2+huida4+huida5
                print(f"周长是：{str(shuchu)}")
            else:
                print("不支持此功能！")
        elif huida == "梯形":
            huida1 = input("请输入要计算的是面积还是周长：")
            huida2 = float(input("请输入上底："))
            huida3 = float(input("请输入下底："))
            huida4 = float(input("请输入高："))
            if huida1 == "面积":
                shuchu = (huida2+huida3)*huida4/2
                print(f"面积是：{str(shuchu)}")
            elif huida1 == "周长":
                huida5 = float(input("请输入其中1条腰长："))
                huida6 = float(input("请输入另1条腰长："))
                shuchu = huida2+huida3+huida5+huida6
                print(f"周长是：{str(shuchu)}")
            else:
                print("不支持此功能！")
        elif huida == "圆形":
            huida1 = input("请输入要计算的是面积还是周长：")
            huida2 = float(input("请输入半径："))
            if huida1 == "面积":
                shuchu = 3.14*(huida2**2)
                print(f"面积是：{shuchu}")
            elif huida1 == "周长":
                shuchu = 2*3.14*huida2
                print(f"周长是：{shuchu}")
            else:
                print("不支持此功能！")
        else:
            print("暂不支持此图形的计算！！！")
            print("退出中......")
            time.sleep(2)
            break
    return 0
def twonumbers_TheBiggestCommonfactor(num1,num2):
    lst = []
    for i in range(1,max(num1,num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            lst.append(i)
    return max(lst)
def tonumbers_TheMinimumCommonmultiple(num1,num2):
    lst = []
    for i in range(1,max(num1,num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            lst.append(i)
    return num1 * num2 // max(lst)
def FtemporCtemp(mode,FtemporCtemp):
    if mode == "℃to℉":
        return FtemporCtemp*9/5+32
    elif mode == "℉to℃":
        return (FtemporCtemp-32)*5/9
    else:
        raise TypeError("TypeError:模式错误！")
def duihuan(mode,money):
    if mode == 1:
        return 0.1565 * money
    elif mode == 2:
        return 17.1278 * money
    elif mode == 3:
        return 6.9670 * money
    elif mode == 4:
        return 109.4451 * money
    elif mode == 5:
        return 0.0584 * money
    elif mode == 6:
        return 0.0091 * money
    elif mode == 7:
        return 1.1497 * money
    elif mode == 8:
        return 0.8640 * money
    elif mode == 9:
        return 1.2276 * money
    elif mode == 10:
        return 0.8146 * money
    elif mode == 11:
        return 4.6834 * money
    elif mode == 12:
        return 0.2135 * money
    elif mode == 13:
        return 0.1177 * money
    elif mode == 14:
        return 9.1443 * money
    elif mode == 15:
        return 0.1342 * money
    elif mode == 16:
        return 8.2470 * money
    else:
        raise TypeError("TypeError:模式错误！")
def Math_cal(mode,float1,float2):
    if mode == 1:
        return math.copysign(float1,float2)
    elif mode == 2:
        return math.cos(float1)
    elif mode == 3:
        return math.degrees(float1)
    elif mode == 4:
        return math.e
    elif mode == 5:
        return math.pi
    elif mode == 6:
        return math.tan(float1)
    elif mode == 7:
        return math.sqrt(float1)
    elif mode == 8:
        return math.sin(float1)
    elif mode == 9:
        return math.radians(float1)
    elif mode == 10:
        return math.pow(float1,float2)
    elif mode == 11:
        return math.modf(float1)
    elif mode == 12:
        return math.log(float1,float2)
    elif mode == 13:
        return math.ldexp(float1,float2)
    elif mode == 14:
        return not math.isnan(float1)
    elif mode == 15:
        return not math.isinf(float1)
    elif mode == 16:
        return math.factorial(int(float1))
    elif mode == 17:
        return math.fabs(float1)
    elif mode == 18:
        return math.exp1(float1)
    elif mode == 19:
        return math.exp(float1)
    else:
        raise TypeError("TypeError:类型错误！")
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
                                    print(tonumbers_TheMinimumCommonmultiple(h,i))
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
                os.system("cls")
                while True:
                    calculatormenu()
                    try:
                        xuhao = int(input("请输入序号："))
                        if xuhao == 1:
                            while True:
                                os.system("cls")
                                xuhao1_menu()
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
                                xuhao2_menu()
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
                                xuhao7_menu()
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
                                xuhao8_menu()
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
                                    print(Math_cal(choose,g,h))
                                    break
                                except Exception as e:
                                    print(repr(e))
                        elif choose in [2,3,6,7,8,9,11,14,15,16,17,18,19]:
                            while True:
                                try:
                                    g = float(input("请输入参数："))
                                    print(Math_cal(choose,g,0))
                                    break
                                except Exception as e:
                                    print(repr(e))
                        elif choose in [4,5]
                            print(Math_cal(choose,0,0))
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
