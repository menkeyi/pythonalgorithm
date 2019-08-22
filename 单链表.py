#!/usr/bin/env python
"""
Create by @Time    : 2019/6/15 0015 下午 4:05
@Contact : 2826634711@qq.com
"""
__author__ = "menkeyi"

#模拟链表第一种方式
Listvalue =   [1,5,6,2,4,3]
Listpointer = [3,2,-1,5,1,4]

head = 0

print(Listvalue[head])
next = Listpointer[head]  #获取下一个指针

while next != -1:
    print(Listvalue[next])
    next = Listpointer[next]


#模拟链表第二种方式
Linkedlist = [[1,3], [5,2], [6,-1], [2,5], [4,1], [3,4]]
value = 0    #值
pointer = 1  #指针地址
head = 0

print(Linkedlist[head][value])
next = Linkedlist[head][pointer]

while next !=  -1:

    print(Linkedlist[next][value])
    next = Linkedlist[next][pointer]  #获取下一个指针

