
# 大纲
1. chatgpt的成功与技术挑战
   1. chatgpt有多成功: 1亿用户里程碑与抖音对比
   2. 挑战：
      1. 几个月用户从0增长到1亿，对扩展性要求很高
      2. 1亿用户也很难
2. 背后的应用框架是ray
3. ray有多成功？chatgpt现在正式开放API，价格是2$/百万token，为何能做得这么便宜？

# 素材

Ray背后的公司是Anyscale， https://s7.51cto.com/oss/202301/03/75b2fa036bd1a19c1a6589989a3604e5c85b2c.png
被认为是下一个databricks（创始人之一Ion Stoica）是Databricks的联合创始人。Databricks现在310亿市值。由UC Berkeley的Robert Nishihara、Philipp Moritz 和 Ion Stoica创立，已融资2.6亿美元，估值10亿。

Ray 是一个基于内存共享的分布式计算框架，适用于细粒度的并行计算和异构计算，其提供了一个底层基础架构，用于管理分配机器学习模型训练工作的复杂任务。

在 2017 年，UC Berkeley 的研究人员首次提交了 Ray 的论文《 Ray: A Distributed Framework for Emerging AI Applications 》。这个套路有点象google当年发布关于map-reduce的论文，然后开创了云计算和大数据时代。



