#!/usr/bin/env python
"""
Create by @Time    : 2019/6/23 0023 下午 12:57
@Contact : 2826634711@qq.com
"""
__author__ = "menkeyi"


def insert(Listvalue, Listpointer, head):
    print(Listvalue[head])
    next = Listpointer[head]  # 获取下一个指针

    while next != -1:
        print(Listvalue[next])
        next = Listpointer[next]

#模拟链表第一种方式
Listvalue =   [1,5,6,2,3]
Listpointer = [3,2,-1,4,1]

head = 0
#正常数据
insert(Listvalue, Listpointer, head)


print("追加4到列表中:")
num = 4  #增加的数
appendNumP =  4 #3的指针需要改成4

#插入数据,直接追加即可，排列顺序有指针决定
Listvalue.append(4)

#之前3的指针指向的是5，我们要将三的指针指向4.这里就将指针往后移动
Listpointer.append(Listpointer[appendNumP])

#改变Listpointer[4] = 1   将1这个指针改成指向数字4的位置  len(Listvalue) - 1
Listpointer[appendNumP] = len(Listvalue) - 1


insert(Listvalue, Listpointer, head)