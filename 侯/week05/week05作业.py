"""
@Project ：cgNLPproject
@File    ：week05_02.py
@Date    ：2024/12/26 12:22
使用kmeans，将一个文本进行聚集分类
第一步：
训练出词向量
第二步：
根据词向量，得到目标文本，每句话的句向量（此处使用的是将所有词向量加起来取平均）
第三步：
使用kmeans，对所有句向量进行分类
第四步：
对分类好的所有类别，做类内平均距离计算统计
第五步：
根据距离排序
"""
