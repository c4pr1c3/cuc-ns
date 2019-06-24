# 什么是**数据驱动安全**

2013年RSA信息安全大会的主题是[“Mastering data. Securing the world”（掌控数据，保护世界）](http://www.countertack.com/news/bid/240457/Visit-Us-at-RSA-Conference-2013-Cyber-Attack-Intelligence)，自此数据分析开始被信息安全工业界所重视。事实上，在此之前，入侵检测领域已经在学术界和工业界产品中使用``数据分析``技术在解决网络安全问题。正如在[第九章 入侵检测](../chap0x09/main.md)中所述，入侵检测技术中所使用的基于异常的检测本质上就是数据分析技术。

相比较于``入侵检测``技术主要关注的``入侵``风险，数据分析技术关注的焦点问题涵盖了信息安全领域的方方面面，包括：拒绝服务攻击检测、欺诈检测、钓鱼攻击检测、服务滥用和搭便车行为检测等等。

卡佩利指出，技术需求如今仍然非常强劲。他在接受信息安全媒体集团采访时表示，Gartner估计2016年市场规模，全球将大数据和机器学习应用到安全用例的花费近8亿美元（约55亿人民币），大数据占比约80%，机器学习20%。

企业正将这些技术视为一个架构的两大组成部门。典型的用例是部署大数据日志管理平台，然后在平台上部署某类机器学习能力，以自动发现数据中的隐藏模式，例如未授权访问。

又比如，许多大数据客户使用大数据技术获取应用程序日志，然后利用机器学习发现异常行为。

卡佩利预测，对许多组织机构而言，大数据和机器学习这两大技术均能作为强大的网络安全工具，未来将必不可少。卡佩利还讨论了大数据和机器学习从广泛的IT应用演进到特定的安全功能、这些技术的新兴用例、以及部署这些技术的先决条件。

## 数据驱动安全的现有代表作

> 近年，越来越多的企业开始利用数据驱动的人工智能技术对抗网络黑产，百度安全利用机器学习进行非法网页检测；阿里巴巴基于云上实时计算平台和机器学习能力， 对于网站攻击进行防御等；腾讯优图DeepEye智能鉴黄技术，可对目标图片进行系统识别，承载着每日数亿张的图片识别，大幅度降低企业因色情违规收到通报的次数，准确率高达99.9%。

> 蚂蚁金服在其生态体系中的诸多业务中应用了大数据技术。蚂蚁金服主导的网商银行，及其前身“阿里小贷”，多年来通过大数据模型来发放贷款。蚂蚁金服通过对客户相关数据的分析，依照相关的模型，综合判断风险，形成了网络贷款的“310”模式，即：“3分钟申请、1秒钟到账、0人工干预”的服务标准。5年多来，为400多万小微企业提供了累计超过7000亿的贷款，帮助了他们解决了资金难题，促进了这些小微企业生存和发展，并创造了更多的就业机会。

> 类似地，大数据的应用也充分得体现在蚂蚁金服生态中的第三方征信公司芝麻信用。“芝麻信用分”是芝麻信用对海量信息数据的综合处理和评估，主要包含了用户信用历史、行为偏好、履约能力、身份特质、人脉关系五个维度。芝麻信用基于阿里巴巴的电商交易数据和蚂蚁金服的互联网金融数据，并与公安网等公共机构以及合作伙伴建立数据合作，与传统征信数据不同，芝麻信用数据涵盖了信用卡还款、网购、转账、理财、水电煤缴费、租房信息、住址搬迁历史、社交关系等等。 

> “芝麻信用”通过分析大量的网络交易及行为数据，可对用户进行信用评估，这些信用评估可以帮助互联网金融企业对用户的还款意愿及还款能力得出结论，继而为用户提供快速授信及现金分期服务。

> 创立于2004年12月的支付宝通过多年的探索，已经实现了风险控制的智能化，防控效果显著。
支付宝风控系统利用原来的历史交易数据进行个性化的验证，提高账户安全性。80%左右的风险事件在智能风控环节就能解决。除了事后审核，事前预防、事中监控也非常重要——事前,将账户的风险分级，不同账户对应不同风险等级；事中，对新上线的产品进行风险评审以及监控策略方案评审。

## 附录A：RSA 2013信息安全大会上的数据分析相关议题

* [Data-Driven Security - Where's the Data?](https://www.rsaconference.com/videos/data-driven-security-wheres-the-data)
* [Big Data Transforms Security](https://www.rsaconference.com/videos/big-data-transforms-security-video)

* [GOOD GUYS VS BAD GUYS: USING BIG DATA TO COUNTERACT ADVANCED THREATS](https://www.rsaconference.com/writable/presentations/file_upload/spo-w09-good-guys-vs.-bad-guys.-using-big-data-to-counteract-advanced-threats.pdf)
* [BIG DATA FOR SECURITY: HOW CAN I PUT BIG DATA TO WORK FOR ME?](https://www.rsaconference.com/writable/presentations/file_upload/ht-t08-_big-data_-for-security-purposes_how-can-i-put-big-data-to-work-for-me_copy1.pdf)

## 参考资料

* [安全和技术创新探索 from 蚂蚁金服官网](https://www.antfin.com/exploration.htm)
* [人工智能：网络安全的关键“盟友” from TechWeb](https://mp.weixin.qq.com/s?__biz=MTE3MzE4MTAyMQ==&mid=2651145730&idx=4&sn=c460495567dc2f020f90aad61d155524)

