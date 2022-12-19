import random,math,os,time
def menu():
    print("------多功能一体机------")
    print("--------------------")
    print("序号          功能")
    print("1            抽取随机数")
    print("2            图形计算器")
    print("3            多功能计算器")
    print("4            math库计算器")
    print("5            退出")
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
        raise Exception("模式错误！")
def main():
    while True:
        os.system("clear")
        menu()
        a = int(input("请输入序号："))
        if a == 1:
            c = int(input("请输入最小值："))
            d = int(input("请输入最大值："))
            while True:
                try:
                    e = input("请输入模式（二进制：bin;八进制：oct,十进制：int，十六进制：hex）：")
                    print(randomint(d,c,e))
                    break
                except Exception as e:
                    print(e.__rept__)
        elif a == 2:
            pass
        elif a == 3:
            pass
        elif a == 4:
            pass
        elif a == 5:
            break
        else:
            print("序号错误！")
            time.sleep(1)
    print("感谢你的使用！希望学生们早日完成作业！再见！")
if __name__ == "__main__":
    main()
