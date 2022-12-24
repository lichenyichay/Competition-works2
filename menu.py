# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2022/12/24 14:50
# @FILE:menu.py
# @Software:IDLE 3.9.6

'''
函数名：menu
调用形式：menu()
:param 无
:return 0
作用：输出主菜单
'''
def menu():
    print("------多功能一体机------")
    print("序号          功能")
    print("1             小工具合集")
    print("2             图形计算器")
    print("3             多功能计算器")
    print("4             math库专用计算器")
    print("5             退出")
    return 0

'''
函数名：xiaogongjumenu
调用形式：xiaogongjumenu()
:param 无
:return 0
作用：输出小工具合集菜单
'''
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
    return 0

'''
函数名：calculatormenu
调用形式：calculatormenu()
:param 无
:return 0
作用：输出多功能计算器菜单
'''
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
    return 0

'''
函数名：int_float_cal_menu
调用形式：int_float_cal_menu()
:param 无
:return 0
作用：输出多功能计算器—整数、小数计算菜单
'''
def int_float_cal_menu():
    print("------整数、小数计算（加减乘除）------")
    print("序号             功能")
    print("1                加法")
    print("2                减法")
    print("3                乘法")
    print("4                除法")
    print("5                返回上一级")
    return 0

'''
函数名：fractions_menu
调用形式：fractions_menu()
:param 无
:return 0
作用：输出多功能计算器—分数计算菜单
'''
def fractions_menu():
    print("------分数计算（加减乘除）------")
    print("序号             功能")
    print("1                加法")
    print("2                减法")
    print("3                乘法")
    print("4                除法")
    print("5                返回上一级")
    return 0

'''
函数名：hybrid_computing_menu
调用形式：hybrid_computing_menu()
:param 无
:return 0
作用：输出多功能计算器—混合运算菜单
'''
def hybrid_computing_menu():
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
    return 0

'''
函数名：currency_conversion_menu
调用形式：currency_conversion_menu()
:param 无
:return 0
作用：输出多功能计算器—货币转换菜单
'''
def currency_conversion_menu():
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
    return 0

'''
函数名：mathmenu
调用形式：mathmenu()
:param 无
:return 0
作用：输出math库计算器菜单
'''
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
    return 0
