#!/usr/bin/env python3.5
# -*-coding:utf8-*-
'''
{"backend":"www.oldboy.org","record":{"server":"100.1.7.999","weight":20,"maxconn":3000}}
'''
import json
# 增加配置文件函数
def add_conf(dic_conf):
    # 循环取出相对应的键与值
    for k, v in dic_conf.items():
        # 获取配置主机名
        if k == "backend":
            back = "%s %s" % (k, v)
        elif k == "record":
            # 获取配置文件内容
            for k1, v1 in v.items():
                if k1 == "server":
                    x1 = v1
                elif k1 == "weight":
                    x2 = v1
                elif k1 == "maxconn":
                    x3 = v1
                else:
                    print("转换赋值出错，请检查！")
            modi = "\t\tserver %s %s weight %s maxconn %s\n" % (x1, x1, x2, x3)
    # 进行相关配置文件查找及写入
    with open("ha.py", "r") as f:
        lines = f.readlines()
        #  获取配置文件总行数
        le = len(lines)
        for line in range(le):
            # 查找配置文件进行相关匹配
            if back == lines[line].strip():
                    while len(lines[line].strip()) != 0:
                        line += 1
                    else:
                        lines.insert(line, modi)
                    # 打开文件进行修改后的数据写入
                    xf = open("ha.py", "w")
                    xf.writelines(lines)
                    xf.close()
                    print("插入成功！")
                    break
def add():
    T = True
    while T:
        conf_input = input("请输入要增加的配置:").strip()
        # 异常处理
        try:
            dic_conf = json.loads(conf_input)  # 将字符串转为字典
            add_conf(dic_conf)
            T = False
        except:
            print("你输入的配置有误，请检查后重新输入!")
            T = True
def modi_conf(dic_conf, num_input):
    # 循环取出相对应的键与值
    for k, v in dic_conf.items():
        # 获取配置主机名
        if k == "backend":
            str_back = "%s %s" % (k, v)
        elif k == "record":
            # 获取配置文件内容
            for k1, v1 in v.items():
                if k1 == "server":
                    x1 = v1
                elif k1 == "weight":
                    x2 = v1
                elif k1 == "maxconn":
                    x3 = v1
                else:
                    print("转换赋值出错，请检查！")
            str_modi = "\t\tserver %s %s weight %s maxconn %s\n" % (x1, x1, x2, x3)
    # 进行相关配置文件查找及写入
    with open("ha.py", "r") as f:
        lines = f.readlines()
        #  获取配置文件总行数
        le = len(lines)
        for line in range(le):
            sstr = lines[line].strip()
            # 查找配置文件进行相关匹配
            if str_back == sstr:
                line = line + num_input
                lines[line] = str_modi
        # 打开文件进行修改数据写入
        with open("ha.py", "w")as xf:
            xf.writelines(lines)
            xf.close()
            print("修改成功！")
def modi():
    T = True
    while T:
        num_input = input("请输入要修改该主机下第几行的数据,默认为第1条记录：").strip()
        conf_input = input("请输入修改后的配置:").strip()
        # 异常处理
        try:
            if len(num_input) == 0:
                num_input = 1
            else:
                num_input = int(num_input)
            dic_conf = json.loads(conf_input)  # 将字符串转为字典
            # 调用修改函数
            modi_conf(dic_conf, num_input)
            T = False
        except:
            print("你输入的配置有误，请检查后重新输入!")
            T = True
def main():
    text = """
    1、增加配置文件
    2、修改配置文件
    3、退出系统
    """
    import sys
    flag = True
    while flag:
        print(text)
        user_input = int(input("请输入要进行的操作序号:"))
        if user_input == 1:
            add()
            break
        elif user_input == 2:
            modi()
            break
        elif user_input == 3:
            sys.exit()
    else:
        print("输入错误，请重新输入！")

if __name__ == "__main__":
    main()