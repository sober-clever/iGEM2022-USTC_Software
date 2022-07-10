### 描述

RxnSim 包提供了计算分子和化学反应的相似度的方法。

### 细节

Allby-all comparison of 4828 reactions (with EC number assigned) drawn from the Rhea database

R 包里的函数接收 SMILES 格式或 MOL 格式文件的反应，给出反应的相似度。

R 包里提供特征向量的缓存以减少计算时间。

R 包里包含了下列函数：

- rs.compute 计算两个反应的相似度
- rs.compute.list 计算两个列表中所有反应对的相似度
- rs.compute.sim.matrix 一个列表中所有反应的两两相似度
- rs.compute.DB 从反应数据库对象中读取数据并计算反应相似度
- rs.makeDB 将包含 EC 编码、反应名称、反应 SMILES 的文本文件转化成数据库对象
- ms.compute 计算两个分子的相似度
- ms.compute.sim.matrix 计算一个列表中所有分子的两两相似度
- rs.clearCache 清空特征向量（fingerprints or feature vectors）的缓存
- rs.mask 将给定反应中分子（可以是多个）的子结构替换成用户定义的掩膜
- ms.mask 将一个分子中的给定子结构替换成用户定义的掩膜

### 相关文献的介绍

RxnSim 通过比较反应内分子的特征来比较反应的相似度。每个反应都和一个二进制的特征向量相关联，该特征向量源于组成反应的分子。

特征向量可以通过三种方法来构建，分别对应于对分子特征的不同捕捉粒度：

1. 第一种，提取单个分子的特征构成特征向量集合，集合中的每一个特征向量对应一个参与反应的分子
2. 第二种，构建两个特征向量，分别对应反应物和生成物的特征向量，反应物的特征向量是各反应物分子特征向量的二进制和（逻辑或），生成物的特征向量同理
3. 第三种，构建一个特征向量，它是所有参与反应的分子的特征向量的二进制和（逻辑或）



在此基础上，有四种计算相似度的算法：

- msim，msim_max 利用第一种方法提取的特征向量集来计算相似度

  > **msim_max** reaction similarity is computed in the same way as described for **msim** except that **the unpaired molecules are not used for computing average**

- rsim 利用第二种方法提取的特征向量来计算相似度

- rsim2 利用第三种方法计算相似度

AUC 测试结果：msim > rsim > rsim2 （AUC 越大，分类效果越好）



同时，为了减少不参与反应的大分子对判断反应相似度的不利影响，RxnSim 提供了途径来减少它们的权重。RxnSim 还可用于局部反应和不平衡反应的相似度比对（msim_max）。

