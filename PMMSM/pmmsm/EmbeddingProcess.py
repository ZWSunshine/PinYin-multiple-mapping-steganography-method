#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zzwwsun

from itertools import chain
from pypinyin import pinyin
import pypinyin

SecretMessageLst = list(input("请输入所要隐写的秘密消息："))

with open("G:\\python_py\\PinYin-multiple-mapping-steganography-method\\PMMSM\\docs\\ShareDict","r",encoding="utf-8") as f:
    ShareDict = dict(f.read())
#print(ShareDict)      #数据类型并不是字典，需要导入ShareDict包进行运算；


class StegProcess(object):

    def BuildEnPinyin(self, HanziLst , ShareDict):

        '''
        构建英式拼音：
        将汉字列表与共享字典进行映射，得到汉字列表的英式拼音列表；
        '''

        EnPinyin = []
        ShareDictLst = ShareDict.keys()
        for i in range(len(HanziLst)):
            for j in ShareDictLst:
                if HanziLst[i] == ShareDictLst[j]:
                    EnPinyin.append(ShareDict[HanziLst[i]])
                else:
                    pass
        #print(EnPinyin)
        return EnPinyin

    def BuildSyllableAndTone(self,EnPinyin):

        '''
        构建英式拼音的音节和声调，分别储存于两个列表SyllableLst和ToneLst中
        :param Enpinyin: 秘密消息或载体文本的英式拼音
        :return: 音节列表SyllableLst和声调列表ToneLst
        '''

        SyllableLst = []
        ToneLst = []
        for i in range(len(EnPinyin)):
            for j in range(1,5):
                if EnPinyin[i][-1] != j:
                    SyllableLst.append(EnPinyin[i])
                    ToneLst.append("0")
                else:
                    SyllableLst.append(EnPinyin[i])
                    ToneLst.append(EnPinyin[i][-1])
        return SyllableLst,ToneLst
        #print(SyllableLst,ToneLst)

    def BuildSTLst(self,SyllableLst):

        '''
        构建音节声调等级表
        :param SyllableLst: 载体音节列表
        :return: 载体文本不重复音节出现频次字典
        '''

        RankSyllableLst = {}
        for item in SyllableLst:
            if item in RankSyllableLst:
                RankSyllableLst[item] += 1
            else:
                RankSyllableLst[item] = 1
        return RankSyllableLst







StegProcess().BuildEnPinyin(SecretMessageLst,ShareDict)