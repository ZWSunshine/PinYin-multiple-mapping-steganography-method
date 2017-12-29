#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zzwwsun

ShareDict().NotUsedHanzi(Lst)
ShareDict().BuildEnPinyin(Lst)
ShareDict().BuildAllSyllable(SyllableLst)
ShareDict().NotUsedPinyin(Lst,SyllableLst)


def BuildEnPinyin(self, Lst):
    '''
    构建英式拼音：
    1、借助第三方库pypinyin
    2、style:是拼音标注类型，共有三种
    3、heteronym:指多音字情况是输出一个还是多个拼音
    :return: 二维英式拼音列表；2000常用字的不重复英式拼音集合
    '''

    PinyinLst = pinyin(Lst, style=pypinyin.TONE3, heteronym=False)
    PinyinSet = set(chain.from_iterable(PinyinLst))  # 2000常用字的不重复英式拼音集合
    # print(PinyinSet)
    # print(len(PinyinSet))
    return PinyinSet

def NotUsedPinyin(self,Lst,SyllableLst):
    Lst1 = ShareDict().BuildAllSyllable(SyllableLst)
    Lst2 = ShareDict().BuildEnPinyin(Lst)
    RetLst = list(set(Lst1).difference(set(Lst2)))       #集合中有差集，列表中没有
    #print(RetLst)
    #print(len(RetLst))
    return RetLst

def NotUsedHanzi(self,Lst):
    UsedPinyin = list(ShareDict().BuildEnPinyin(Lst))
    DagParams = DefaultDagParams
    UsedHanzi = dag(dag_params=DagParams,pinyin_list=UsedPinyin,path_num=len(UsedPinyin),log=True)
    for item in UsedHanzi:
        result = item.path
        print(result)
    return