#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zzwwsun

'''
import os
import sys
import pypinyin
from pypinyin import pinyin, lazy_pinyin
lst = "孙志文"
lstPinyin = pinyin(lst,style=pypinyin.TONE3,heteronym=True)
print(lstPinyin)

JDRoute = os.path.abspath("2000常用字")
FileML = os.path

print(FileML)


#with open("G:\\python_py\\PinYin-multiple-mapping-steganography-method\\PMMSM\\docs\\2000常用字","r",encoding="utf-8") as f:
#    lst = f.read()
#    print(lst)

lst = []
lst1 = ['1','2','3','4','5','a']
lst2 = ['a','b','c','d','e']

s = set(lst1).difference_update(set(lst2))
print(s)

for i in range(len(lst1)):
    for j in range(len(lst2)):
        lst.append(lst2[j]+lst1[i])


print(lst)


with open("G:\\python_py\\PinYin-multiple-mapping-steganography-method\\PMMSM\\docs\\2000常用字", "r",
          encoding="utf-8") as f:
    Lst = list(f.read())
print(Lst)
print(len(Lst))

s = input("请输入：")
print(s)
'''

Lst_ =[]
Lst = ["name","age","school"]
dict = {"name":"孙志文","age":"25","school":"QDU"}
dictLst = list(dict.keys())
print(dictLst)

for i in range(len(Lst)):
    for j in range(len(dictLst)):
        if Lst[i] == dictLst[j]:
            Lst_.append(dict[Lst[i]])
        else:
            pass
print(Lst_)
print(Lst_[2][-1])
print([i for i in range(1,5)])