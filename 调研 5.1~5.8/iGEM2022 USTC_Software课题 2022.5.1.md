### 课题

用户给出某一有机物的结构式，并指定有机物上需要反应的基团和目标基团。

我们的平台需要先在数据库中找出能与该基团作用的酶（大概有上千种），再去另一数据库中找出这些酶对应的底物（每种酶对应的底物并不多），接着把用户给出的有机物与酶对应的底物进行相似度比对，根据计算所得的相似度对酶进行排序，从而找出最有可能与用户给出的有机物上的基团作用的酶，最后输出比对结果和对应的酶。

### 课题的开展分为以下 6 步

#### 1. 数据导入

- 前端通过 mol 文件（[CT file](https://en.wikipedia.org/wiki/Chemical_table_file)）提供**结构式**的信息，或者 以 [SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)的形式给出**结构式**

- **要反应的基团** 和 **目标基团** 也通过文件提供

#### 2. 酶初筛

- 根据前端提供的信息，确定反应的 大类、小类 和 基团的类型（羟基、羧基什么的），通过这三项可以直接确定所需要酶的大致类别
- 把这些信息放到去数据库（如 [BRENDA](https://www.brenda-enzymes.org/)）里查询（爬虫+sql 或者 调用现有的 API），初步确定适合的酶的 EC 编码

#### 3. 比对

- 把酶的 EC 编码放到数据库（如 [KEGG](https://www.genome.jp/kegg/)）来查询这些酶对应的底物
- 将这些底物与用户提供的反应物进行比对（通过聚类算法等机器学习算法来实现）
- 注意： 比对要考虑的因素有基团周围的小环境（局部比对）和整个反应物的大环境（整体比对）

反应物比对的相关论文

[Application of kernel functions for accurate similarity search in large chemical databases | BMC Bioinformatics | Full Text (biomedcentral.com)](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-11-S3-S8)

[Chemical similarity searching-Web of Science Core Collection](https://www.webofscience.com/wos/woscc/full-record/WOS:000077186300007?SID=USW2EC0A6427eMF4WFjIH5WD8w7nd)

#### 4. 排序

- 排序的因素 ：来源、相似度、动力学数据、产率

#### 5. 输出

#### 6. 可供选择的扩展功能

- 用户提供新的信息