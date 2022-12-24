# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2022/12/24 15:17
# @FILE:tuxing_cal.py
# @Software:IDLE 3.9.6
import time

'''
函数名：tuxing
调用形式：tuxing(huida)
:param huida 图形
:return 0
作用：进行图形计算
'''
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
            huida1 = input("请输入要计算的是面积、周长、方中圆还是圆中方：")
            huida2 = float(input("请输入半径："))
            if huida1 == "面积":
                shuchu = 3.14*(huida2**2)
                print(f"面积是：{shuchu}")
            elif huida1 == "周长":
                shuchu = 2*3.14*huida2
                print(f"周长是：{shuchu}")
            elif huida1 == "方中圆":
                shuchu = 0.86 * (r ** 2)
                print(f"S阴 = {shuchu}")
            elif huida1 == "圆中方":
                shuchu = 1.14 * (r ** 2)
                print(f"S阴 = {shuchu}")
            else:
                print("不支持此功能！")
        else:
            print("暂不支持此图形的计算！！！")
            time.sleep(2)
            break
    return 0
