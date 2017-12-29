#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zzwwsun

import os
import sys
from pypinyin import pinyin
from itertools import chain
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag
import pypinyin
import Pinyin2Hanzi

'''
构建共享字典：
1、将2000个常用汉字转化成英式拼音；
2、找出400字节和5种声调的组合中没被用到的情况，两个列表相减；
3、找出除第一个之外的同音字列表；
4、构造两者之间的一一映射关系；
'''

with open("G:\\python_py\\PinYin-multiple-mapping-steganography-method\\PMMSM\\docs\\2000常用字", "r",
          encoding="utf-8") as f:
    Lst = list(f.read())
    # print(Lst)
with open("G:\\python_py\\PinYin-multiple-mapping-steganography-method\\PMMSM\\docs\\汉语音节表", "r",
          encoding="utf-8") as f:
    SyllableLst = list(f.read().split(" "))
    # print(SyllableLst)
    # print(len(SyllableLst))      #长度：413个音节


class BuildShareDict(object):

    def BuildAllSyllable(self,SyllableLst):

        '''
        构建2065种音节：

        :return:
        1、413个音节表，如：['a', 'ai', 'an', 'ang', 'ao']
        2、2065种英式拼音，如：['a0', 'ai0', 'an0', 'ang0', 'ao0']
        '''
        AllEnPinyin = []
        ToneLst = ['','1','2','3','4']       #轻声，一声，二声，三声，四声

        for i in range(len(ToneLst)):
            for j in range(len(SyllableLst)):
                AllEnPinyin.append(SyllableLst[j]+ToneLst[i])
        #print(AllEnPinyin)               #2065种英式拼音，如：['a0', 'ai0', 'an0', 'ang0', 'ao0']
        return AllEnPinyin

    def BuildDictMapping(self,Lst,SyllableLst):
        AllEnPinyin = BuildShareDict().BuildAllSyllable(SyllableLst)
        ShareDict = dict(zip(Lst,AllEnPinyin))
        #print(ShareDict)
        return ShareDict


BuildShareDict().BuildDictMapping(Lst,SyllableLst)





















