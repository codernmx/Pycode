#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2022/3/1'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import pandas as pd
# 2007-2019
mda = pd.read_excel('全年度管理层讨论与分析用于MDA信息含量试验.xlsx', sheet_name = 0)
# 读取行业数据
industry = pd.read_excel('证监会2012年版行业分类.xlsx',sheet_name = 0)
# 与行业数据进行合并
data = pd.merge(mda, industry,on=['股票代码','会计年度'], how = 'inner')

# 重命名字段
#data = data.rename(columns={"shortname":"证券简称", "INDCDBASIC":"行业代码"})
data = data.rename(columns={"INDCDBASIC":"行业代码"})
# 选择需要分析的字段
data = data[["股票代码","会计年度","经营讨论与分析内容","行业代码"]]
# 剔除金融行业
data = data[~data["行业代码"].str.contains("J")]
# 仅处理2019年的文本
data = data[data["会计年度"] == 2019]
# 重置索引
data = data.reset_index(drop=True)


#3. 分词处理
import jieba
import re
def get_cut_words(content):
    # 读入停用词表
    stop_words = []
    with open('01-整合哈工大川大百度中文四大停用词库.txt', encoding = 'utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())
    # 分词
    cutword = [w for w in jieba.cut(content) if w not in stop_words and len(w) > 1 and not re.match('^[a-z|A-Z|0-9|.]*$',w)]
    strword = " ".join(cutword)
    return strword

data['strword'] = data['经营讨论与分析内容'].apply(get_cut_words)


#4. 生成BOW矩阵
from sklearn.feature_extraction.text import CountVectorizer
countvec = CountVectorizer(min_df = 50, max_df = 1000) # 在5个以上年度报告出现的词才保留，在1000个以上年报出现的词剔除

res = countvec.fit_transform(data.strword) # 稀疏bow矩阵

#5. 词频向量标准化
# 利用公司总词数进行标准化
import numpy as np
def normalizer(vec):
    denom = np.sum(vec)
    return [(el / denom) for el in vec]
doc_term_matrix_normalizer = []
for vec in doc_term_matrix_normalizer:
    doc_term_matrix_normalizer.append(normalizer(vec))
print(np.matrix(doc_term_matrix_normalizer))

#6. 行业标准化向量和市场标准化向量
for i in range(0,3568):
    df_firm = data1.iloc[i:i+1]
    df_firm = df_firm.melt(id_vars=['code','year','ind'],    # 要保留的字段
                           var_name="wordid",   # 拉长的分类变量
                           value_name="freq")   # 拉长的度量值名称

    ind_matrix = data1[(data1["ind"] == data1.iloc[i]["ind"]) & (data1["code"] != data1.iloc[i]["code"])]
    ind_matrix = ind_matrix.drop(["code","year","ind"],axis=1)
    normind = ind_matrix.mean(axis = 0)

    market_matrix = data1[data1["ind"] != data1.iloc[i]["ind"]]
    market_matrix = market_matrix.drop(["code","year","ind"],axis=1)
    normmarket = market_matrix.mean(axis = 0)

    df_firm["freq_ind"] = normind.tolist()
    df_firm["freq_market_ind"] = normmarket.tolist()

    df_firm.to_excel("{}词条.xls".format(data1.iloc[i]["code"]),index=None)



