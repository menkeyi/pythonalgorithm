#!/usr/bin/env python
"""
Create by @Time    : 2019/6/23 0023 上午 10:43
@Contact : 2826634711@qq.com
"""
__author__ = "menkeyi"



#第一种方式
def one():
   #竖排就是双向链表完整信息 1 [-1, 3]
   Listvalue = [1, 5, 6, 2, 7, 3]
   ListRight = [3, 2, 4, 5, -1, 1]
   ListLeft =  [-1,  5, 1, 0, 2, 3]

   #获取ListLeft中-1的下标
   head = ListLeft.index(-1)
   print(Listvalue[head])

   #获取下一个指针
   next = ListRight[head]

   while next > -1:
       print(Listvalue[next])#打印值
       next = ListRight[next]  #获取下一个指针











#第二中方式
def two():
    #2个指针的下标
    right = 1
    left = 2

    value = 0

    Linkedlist = [[1, 3, -1], [5, 2, 5], [6, 4, 1], [2, 5, 0], [7, -1, 2], [3, 1, 3]]

    head = 0  #设置头指针
    print(Linkedlist[head][value])
    next = Linkedlist[head][right]


    while next > -1:
        print(Linkedlist[next][value])
        next = Linkedlist[next][right]


print("第一种双向链表方式:")
one()
print("第二种双向链表方式:")
two()