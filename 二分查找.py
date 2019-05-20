#!/usr/bin/env python
"""
Create by @Time    : 2019/5/20 0020 下午 9:02
@Contact : 2826634711@qq.com
"""
__author__ = "menkeyi"


numbers = [1,3,5,7,9,13,14,17,20,33,55,56,89,90]

#搜索数组中的数
search = 14

head, tail = 0 , len(numbers)

while tail - head > 1:

   mid = (head + tail)//2

   if search < numbers[mid]:
       tail = mid
   elif search > numbers[mid]:
       head = mid + 1
   elif search == numbers[mid]:
       result = mid
       break
else:#tail - head 小于等于1的时候走这个判断
    if search == numbers[head]:
        result = head
    else:#查询的数不在数组中返回数组最后一个下标
        result = -1



print(numbers[result])
