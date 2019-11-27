# -*- coding: utf-8 -*-



def division():
    """功能：  分苹果"""
    print("================分苹果了=============")
    apple = int(input("请输入苹果的个数： "))
    children = int(input("请来了几个小朋友： "))

    result = apple // children

    remain = apple - result * children

    if remain > 0:
        print(apple, "个苹果， 平均分给", children, "个小朋友, 每个人分", result, "个, 剩下", remain, "个")
    else:
        print(apple, "个苹果， 平均分给", children, "个小朋友, 每个人分", result, "个")


if __name__ == '__main__':
    try:
        division()
    except ZeroDivisionError:
        print("\n 出错了 ～_～ -----苹果不能被0个小朋友分！")
    except ValueError as e:
        print("输出错误：", e)
    else:
        print("分苹果顺利完成...")
    finally:
        print("进行了一次分苹果操作...")









