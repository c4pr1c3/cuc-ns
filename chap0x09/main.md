# 第九章 入侵检测

## 9.1 入侵检测概述

### 9.1.1 入侵检测发展简史

![图 9-1 入侵检测发展简史](attach/media/image1.png)

1980年，James P. Anderson 在题为“计算机安全威胁监控与监视”的技术报告中首次提出了入侵检测的概念，将入侵尝试（Intrusion attempt）或威胁（Threat）定义为潜在的、有预谋的且未经授权而访问信息、操作信息、致使系统不可靠或无法使用的企图。此外，James P. Anderson 针对计算机系统风险和威胁提出了相应的分类方法，将威胁分为外部渗透、内部渗透和不法行为三种，还提出了利用审计跟踪数据监视入侵活动的思想。这份报告被认为是入侵检测的开山之作。

1986年，为检测用户对数据库异常访问，W.T.Tener 在 IBM 主机上用 COBOL 开发了 Discovery 系统，是最早的基于主机的入侵检测系统（Host-based Intrusion Detection System, HIDS）原型。1987年，Dorothy E. Denning 提出了一种通用的入侵检测系统抽象模型，首次提出将入侵检测的概念作为一种计算机系统安全防御问题的措施。在此模型中系统框架由主体（Subjects）、对象（Objects）、审计记录（Audit records）、活动档案（Profiles）、异常记录（Anomoly records）和活动规则（Activity rules）组成。它独立于特定的系统平台、应用环境、系统弱点以及入侵类型，为构建入侵检测系统提供了一个通用的框架。

1988年的莫里斯蠕虫事件发生之后，网络安全才真正引起了军方、学术界和企业的高度重视。美国空军、国家安全局和能源部共同资助空军密码支持中心、劳伦斯利弗摩尔国家实验室、加州大学戴维斯分校、Haystack 实验室，开展对分布式入侵检测系统（Distributed Intrusion Detection System, DIDS）的研究，将基于主机和基于网络的检测方法集成到一起。DIDS 是分布式入侵检测系统历史上的一个里程碑式的产品，它的检测模型采用了分层结构，包括数据、事件、主体、上下文、威胁、安全状态等6层。同年，SRI/CSL 的 Teresa Lunt 等人改进了 Denning 的入侵检测模型，并实际开发出了一个入侵检测专家系统(Intrusion Detection Expert System, IDES）。该系统用于检测单一主机的入侵尝试，提出了与系统平台无关的实时检测思想，包括一个异常检测器和一个专家系统，分别用于统计异常模型的建立和基于规则的特征分析检测。

1990年是入侵检测系统发展史上的一个分水岭。这一年，加州大学戴维斯分校的 L. T. Heberlein 等人开发出了基于网络的入侵检测系统（Network Intrusion Detection System, NIDS）：网络安全监测（Network Security Monitor, NSM）。该系统第一次直接将网络流作为审计数据来源，因而可以在不将审计数据转换成统一格式的情况下监控异构主机。从此之后，入侵检测系统发展史翻开了新的一页，两大阵营正式形成：基于网络的IDS和基于主机的 IDS。

从20世纪90年代到现在，入侵检测系统的研发呈现出百家争鸣的繁荣局面，1995年，下一代入侵检测专家系统（Next Generation IDES, NG-IDES）产生，可以检测多个主机上的入侵。1996年，基于图的入侵检测系统（Graph-based Intrusion Detection System, GrIDS）出现，主要用于针对大规模协同、自动化检测。1998年，S.Staniford 等人提出一个公共入侵检测框架（Common Intrusion Detection Framework, CIDF），将入侵检测系统分为4个组件：事件产生器、事件分析器、响应单元及事件数据库，并将入侵检测系统需要分析的数据统称为事件，它可以是网络中的数据包，也可以是从系统日志等其他途径得到的信息，定义了 IDS 表达检测信息的标准语言以及IDS组件之间的通信协议，能够集成各种 IDS 使之协同工作，实现各 IDS 之间的组件重用，所以 CIDF 也是构建分布式 IDS 的基础。2007年，CIDF 工作组再次发布了3篇 IETF RFC 标准草稿，分别为 RFC 4765 入侵检测消息交换格式（The Intrusion Detection Message Exchange Format, IDMEF）、RFC 4766 入侵检测消息交换要求（The Intrusion Detection Message Exchange Format, IDMEF）和 RFC 4767 入侵检测交换协议（The Intrusion Detection Exchange Protocol, IDXP）。

### 9.1.2 入侵检测的意义和作用

![图 9-2 入侵检测](attach/media/image2.png)

入侵检测可以识别入侵者，识别入侵行为，监视和检测已成功的安全突破，为对抗入侵及时提供重要信息，以阻止事件的发生和事态的扩大，具有如下作用：
1. 实时检测网络系统的非法行为，持续地监视、分析网络中所有的数据报文，发现并及时处理所捕获的数据报文；
2. 安全审计，通过对入侵检测系统记录的网络事件进行统计分析，发现其中的异常现象，为评估系统的安全状态提供相关证据；
3. 不占用被保护系统的任何资源，作为独立的网络设备，可以做到对黑客透明，本身的安全性较高；
4. 主机入侵检测系统运行于被保护系统之上，可以直接保护、恢复系统；

![图 9-3 入侵检测系统的作用](attach/media/image3.png)


在安全体系中，入侵检测系统是通过数据和行为模式判断其风险水平的典型系统，防火墙相当于第一道安全闸门，可以组织一类人群的进入，但无法阻止同一类人群中的破坏分子，也不能组织内部的破坏分子，也不能组织内部的破坏分子；访问控制系统可以不让低级权限的人做越权工作，但无法保证拥有高级权限的人不做破坏行为，也无法保证低级权限的人通过非法行为获得高级权限。入侵检测系统可以说是防火墙系统的合理补充和有力延伸，它的目的是为响应决策提供威胁证据，在不影响网络部署的前提下，实时、动态地检测来自内部和外部的各种攻击，及时、准确、全面的发现入侵。这可以有效覆盖到防火墙检测和保护的盲区，通过与防火墙协同联动，达到有效网络安全防护。


## 9.2 入侵检测理论

### 9.2.1 入侵检测基本概念

入侵检测(Intrusion Detection)，指对系统的运行状态进行监视，发现各种攻击企图、攻击行为或者攻击结果，以保证系统资源的机密性、完整性和可用性。进行入侵检测的软件与硬件的组合便是入侵检测系统（Intrusion Detection System，IDS）

警报(Alert)，当一个入侵正在发生或者试图发生时，IDS将发布一个警报信息通知系统管理员。如果控制台与IDS同在一台机器，警报信息将显示在监视器上，也可能伴随着声音提示，如果是远程控制台，那么警报将通过IDS内置方法（通常是加密的）、简单网络管理协议（Simple Network Management Protocol, SNMP)（通常不加密）、电子邮件（Electronic Mail, E-mail）、短信息服务（Short Message Service, SMS）、IM（即时通信）或者以上几种方法的混合方式传递给管理员。

异常（Anomoly），当有某个事件与一个已知攻击的信号相匹配时，多数IDS都会告警；一个基于异常的 IDS 会构造一个当时活动的主机或网络的大致轮廓，当有一个在这个轮廓以外的事件发生时，IDS 就会告警。

特征(Signature)，IDS的核心是攻击特征（签名），它使IDS在（入侵）事件发生时触发警报。如果特征信息过短会经常触发 IDS，导致误报或错报，过长则会减慢IDS的工作速度。将 IDS 所支持的特征数视为 IDS 好坏的标准是评价 IDS 产品优劣的常见误区，例如有的厂商用一个特征涵盖许多攻击，而有些厂商则会将这些特征单独列出，特征数量的多少并不能决定威胁检测能力的高低。



### 9.2.2 入侵检测系统评价指标

入侵检测系统主要从以下方面进行的评价：
- 可靠性，指系统的容错能力和可持续运行能力；
- 可用性，指系统开销大小，对网络性能影响的大小；
- 可测试，指系统能够通过模拟攻击进行检测测试；
- 适应性，指系统易于开发和扩展；
- 实时性，指系统能够及早发现入侵企图；
- 安全性，指系统可确保自身的安全；
- 准确性，指系统正确识别入侵行为的能力。

准确性主要通过误报率和漏报率进行评估，误报率和漏报率是衡量入侵检测系统效率的两个重要指标。在我国，入侵检测系统的评价有国家标准：[《信息安全技术 网络入侵检测系统技术要求和测试评价方法 GB/T 20275-2013》](http://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8069AD3A7E05397BE0A0AB82A) 。

误报率（False Positive Rate ，FPR）的计算公式为:

    FPR = FP / N

漏报率（False Negative Rate ，FNR)的计算公式为：

    FNR = FN / N

其中，N 是警报总数，FP 是误报事件总数。FN 为漏报事件总数。最理想的入侵检测系统的评估结果是误报率 FPR=0 且漏报率 FNR=0，但实际上误报率和漏报率常常是成反比的。

![图 9-4 漏报率和误报率间关系](attach/media/image4.png)



使用上述指标可以对异常检测和误用检测两种模型进行比较，结果如下表：

| | 异常检测 | 误用检测 |
|--------|-------|-----------|
| 可靠性 | 不稳定 | 较稳定|
| 可用性 | 较低 | 较高 |
| 可测试 | 测试结果波动较大 | 测试结果较稳定 |
| 适应性 | 较强 | 较弱（难以检测未知攻击） |
| 实时性 | 易造成延时 | 延时较小 |
| 准确性 | 误报率较高 | 漏报率较高 |
| 安全性 | - | - |

## 9.3 入侵检测关键技术

### 9.3.1 入侵检测基本技术

前面我们介绍了 Dorothy Denning 的通用入侵检测模型，其中审计记录/网络数据包/应用程序记录、事件产生器、活动记录、更新活动记录、动态产生活动记录均是信息收集操作；而增加/修改规则、规则集则是进行信息分析；产生异常活动记录、时钟便是结果处理。

在信息收集中，其信息来源主要有系统或网络的日志文件、网络流量、或观察系统目录和文件的变化、程序执行行为（资源加载/API调用序列/IO规律等），其详细内容均以在本书前几章节中进行了介绍。

信息收集的方法可以是基于主机、基于网络或是基于传感器，例如使用基于主机运行的软件，基于网络的数据捕获传感器，以及物联网中的各种传感器。

信息分析，在异常检测中有统计分析、完整性分析，误用检测中的模式匹配。融合使用异常检测和误用检测模型是实用 IDS 系统的普遍产品策略。下面进行详细介绍。

关于异常检测，方法如下：

(1) 统计分析

统计分析对象主要是用户、文件、目录和设备等，方法是为统计分析对象创建一个统计描述，来统计正常使用时的一些测量属性，如访问次数、操作失败次数和延时等。后进行统计匹配，测量属性的平均值将被用来与网络、系统的行为进行比较，任何观测/测量值在正常值范围之外时，就认为有入侵发生。

(2) 完整性分析

完整性分析的对象是文件、目录、任意数字资源，例如：文件和目录的内容及属性。完整性分析方法是建立完整性分析对象在正常状态时的完整性签名来进行完整性分析匹配，查看匹配签名值是否发生改变，若发生改变，则认定目标对象被入侵篡改。

除去上面介绍的两种方法，其他常见的异常检测算法有：基于特征选择异常检测、基于贝叶斯推理异常检测、基于贝叶斯网络异常检测、基于神经网络异常检测、基于贝叶斯聚类异常检测等。

关于误用检测，模式匹配方法就是将收集到的信息与已知的网络入侵和系统误用模式规则集进行比较，从而发现违反安全策略的行为。入侵模式的表示方法包括一个过程（如执行一条指令）和一个输出（如获得权限）。入侵模式的匹配过程有字符串匹配，包括精确匹配、模糊匹配，还有状态机迁移序列匹配。

此外其他常见误用检测算法有基于条件概率误用检测、基于专家系统误用检测和基于状态迁移误用检测等。

融合使用异常检测和误用检测模型的技术方法如下图：

![图 9-5 融合使用异常检测和误用检测模型的技术方法](attach/media/image6.png)


将捕获的网络数据进行预处理，并将应用层数据通过白名单数据库进行白名单匹配，如果匹配成功，则和指令数据放入状态机执行，后进行状态分析，若不匹配则直接进行状态统计。最后进行汇总分析和相应处理，同时应将无法关联的异常模式加入异常数据集合，通过数据挖掘反馈给黑名单数据库和白名单数据库进行更新。

最后关于结果处理阶段，就是产生告警，记录告警日志。请求其他安全设备的协作联动如防火墙联动。

### 9.3.2 入侵检测体系架构

主机入侵检测系统是监视与分析主机的审计记录，判断能否及时采集到审计记录。可以不运行在监控主机上。
网络入侵检测系统是对通信数据进行侦听采集数据。提供对网络通用的保护，不消耗主机额外资源。

无论是主机入侵检测系统，还是网络入侵检测系统，都可以采用的系统体系结构包括集中式结构、等级分布式结构以及完全分布式结构。详细介绍如下：
集中式结构是采用分布式的信息收集，然后将收集信息汇总上报，进行集中关联分析的结构形式，具体结构如图 9-7 所示。典型的集中式结构代表有：DIDS（Distributed Intrusion Detection System）（Snapp et al., 1991）、DShield（Internet Storm Center，2000）、NSTAT（Kemmerer,1998）。集中式结构的挑战是单点故障和单点瓶颈。单点故障是指汇总关联分析节点一旦出现故障，则整个系统就会无法工作。单点瓶颈是指汇总关联分析节点的处理能力决定了整个系统的处理能力。因此，集中式结构的应用场景为小型公司网络范围内的IDS协作，不适用于互联网范围内的大规模IDS协作。

![图 9-6 集中式结构](attach/media/image7.png)

分布式结构是指引擎和控制中心在2个系统之上，可通过网络通讯进行远距离查看和操作的结构形式，可细分为等级分布式和完全分布式。

等级分布式结构的特点是存在分区和“逐层”汇聚式关联分析。分区可分为地理位置、管理域、相近软件平台以及预期入侵种类，具体结构如图 9-8 所示。等级分布式结构的典型代表是：GrIDS(Staniford-Chen et al., 1996)、The EMERALD project (Porras and Neumann, 1997)、DSOC (Distributed Security Operation Center, Abdoul Karim Ganame et al., 2008)、Servin and Kudenko (2008) 、reinforcement learning based、AAFID(Balasubramaniyan et al., 1998)、NetSTAT (Vigna, 1999)。等级分布式结构的优点是可扩展性略高于集中式结构，挑战是整个系统的处理能力仍受到高层次节点能力的制约；高层节点引发的单点故障也仍可能存在；并且系统的检出率较低，信息在“汇聚”的过程中会由于“压缩”而导致“损失”和“失真”。

![图 9-7 等级分布式结构](attach/media/image8.png)


完全分布式结构的特点是无超级管理节点，节点间通信方式为P2P、Gossip协议、组播或发布/订阅机制，具体结构如图9-9所示。典型代表有：Locasto et al. (2005): P2P based 、The DOMINO project (Yegneswaran et al., 2004; Barford and Jha, 2004)、Dash et al. (2006)、Garcia et al. (2004)、MADIDF (Mobile Agents based Distributed Intrusion Detection Framework) (Dayong Ye et al., 2008) 、Indra (Janakiraman and Zhang, 2003)、CSM (White et al., 1996)。完全分布式的挑战是检测精度低、可扩展性差、负载均衡难度高。

![图 9-8 完全分布式结构](attach/media/image9.png)


协作式攻击的特点主要是：采用分布式、协同，且有发起源。分布式检测的优势为可快速定位协作式攻击的真正源头，可避免对同源攻击的重复报警。

## 9.4 入侵检测标准化

### 9.4.1 通用入侵检测框架

通用入侵检测框架（Common Intrusion Detection Framework, CIDF）是美国国防高级研究项目局（Defense Advanced Research Projects Agency, DARPA）为 IDS 数据交换而作出的一个尝试。定义了 IDS 表达检测信息的标准语言以及IDS组件之间的通信协议，符合 CIDF 规范的 IDS 和安全设备可以共享检测信息，进行协同工作。并集成了各种安全设备使之协同工作，是分布式入侵检测的基础。

CIDF的规范文档包括四部分，分别是体系结构（The Common Intrusion Detection Framework Architecture, CIDFA），提出了一个标准的 IDS 的通用模型；规范语言（A Common Intrusion Specification Language, CISL），定义了一个用来描述各种检测信息的标准语言；内部通讯（ Communication in the Common Intrusion Detection Framework），定义了 IDS 组件之间进行通信的标准协议；程序接口（(Common Intrusion Detection Framework APIs, CIDF APIs），提供一整套标准的应用程序接口（API 函数）。

CIDF 的体系结构文档将一个 IDS 分为以下四个组件:事件产生器(Event generators)、事件分析器(Event analyzers)、事件数据库(Event databases)响应和单元(Response units)。并将 IDS 需要分析的数据统称为事件(event)，它可以是基于网络的 IDS 从网络中提取的数据包，也可以是基于主机的 IDS 从系统日志等其它途径得到的数据信息。CIDF 组件之间是以通用入侵检测对象(generalized intrusion detection objects，gido)的形式交换数据的，一个 gido 可以表示在一些特定时刻发生的一些特定的事件，也可以表示一系列事件中得出的一些结论，还可以表示执行某个行动的指令。

![图 9-9 通用入侵检测框架（CIDF）体系结构](attach/media/image10.png)


事件产生器进行数据采集，从入侵检测系统外的整个计算环境中获得事件，并以 CIDF gido 格式向系统的其他部分提供此事件。事件产生器是所有IDS所需要的，同时也是可以重用的。

事件分析器是分析部分，从其他组件接收 gido，分析得到的数据，并产生新的 gido。误用/异常检测算法均可以在此得到应用。

响应单元为响应部分，是对分析结果作出作出反应的功能单元，它可以终止进程、重置连接、改变文件属性等，也可以只是简单的报警，也可以和防火墙等其他安全设备联动响应。

事件数据库，包含日志，是存放各种中间和最终数据的地方的统称，它可以是复杂的数据库，也可以是简单的文本文件。可以持久化存储。

通用入侵检测框架的规范语言，是各 IDS 使用统一的 CISL 来表示原始事件信息（审计踪迹记录和网络数据流信息）、分析结果（系统异常和攻击特征描述）、响应指令（停止某些特定的活动或修改组件的安全参数），建立了 IDS 之间信息共享的基础。CISL 是 CIDF 的最核心也是最重要的内容。gido 的构建与编码是 CISL 的重点。

内部通讯的匹配服务为 CIDF 各组件之间的相互识别、定位和信息共享提供了一个标准的统一的机制，是基于轻量目录访问协议（Lightweight Directory Access Protocol, LDAP）实现的。内部通讯机制的消息层在易受攻击的环境中实现了几种安全（保密、可信、完整）并可靠的信息交换机制，使通信与阻塞和非阻塞处理无关、使通信与数据格式无关、使通信与操作系统无关、使通信与编程语言无关。

关于通用入侵检测框架的程序接口，程序员可以在不了解编码和传递过程具体细节的情况下，以一种很简单的方式构建和传递 gido，如使用 gido 编解码 API、消息层 API 、gido 传输 API 、gido 动态追加 API 、签名 API 和顶层 CIDF 的 API。


### 9.4.2 安全开放平台

安全开放平台（Open Platform for Security, OPSEC）联盟成立于1997年，由软件技术公司 Checkpoint 发起。成立目的是向用户提供完整的、能够在多厂商之间进行紧密集成的网络安全解决方案。联盟提供集成的应用程序和基于 Checkpoint 平台的安全服务。OPSEC 扩展了 Check Point 安全虚拟网络（Secure Virtual Network, SVN）的体系结构，具体构成如下：
* 内容安全，采用内容安全协议（Content Vectoring Protocol, CVP）允许用户扫描经过网络的所有数据包内容；
* Web资源管理，采用Web资源管理协议（URL Filtering Protocol, UFP）定义 Client/Server 异步接口来分类和控制基于特定URL地址的通信；
* 入侵检测，采用 ** 可疑行为监测协议？ **（Suspicious Activity Monitoring Protocol, SAMP）识别网络中的可疑行为，并通知防火墙及时处理；
* 事件集成，提供 Log Export API 和 Event Logging API 两个事件集成 API，允许第三方访问日志数据；
* 管理分析，采用 Check Point 中央策略数据库接口（Check Point Management Interface, CPMI），允许第三方应用安全地访问存储在管理服务器上的安全策略；
* 双机热备份，即带负载平衡的高可用性（Load Balancing, HA/LB）和双机热备份（Hot Standby, HA-HS) ；
* 用户到地址的映射 UAM (User Address Mapping)；
* 安全的电子商务应用，采用用户权限 API（UserAuthority API, UAA）；
* 工业标准协议，包括认证协议（Radius/TACACS+）、SNMP、LDAP 。


## 9.5 实战入侵检测系统

### 9.5.1 典型部署方式

![图9-10 入侵检测的典型部署模式](attach/media/image11.png)


图9-10是一个 IDS 的典型部署图。在网络中部署 IDS 时，可以使用多个 NIDS 和 HIDS，根据网络的实际情况和自己的需求确定具体的部署情况。入侵检测系统的开源代表是 Snort， Snort 是一个轻量级的NIDS，它具有多模式报文分析工具、嗅探工具、报文记录以及数据取证分析工具。应用场景有在线分析和离线分析。


### 9.5.2 Snort

#### 9.5.2.1 Sonrt概述

Snort 具有以下特性：轻巧，源代码不到1MB；具有移植性，在 Linux, Windows, MacOS X, Solaris, BSD, IRIX, Tru64, HP-UX 平台下均可使用；高性能，使用百兆网络线速处理；可配置，使用简单的规则语言，丰富的日志/配置分析工具；免费，GPL 开源。

Snort 的设计遵守轻量级的网络入侵检测系统，基于 Libpcap 的报文嗅探接口，基于规则的检测引擎和支持无限扩展的插件系统。

Snort 的检测引擎是基于指纹的规则，采用模块化设计。具有丰富的检测能力（内置规则），可进行隐蔽扫描，操作系统识别扫描,、缓冲区溢出攻击、后门和CGI漏洞利用等等。规则系统设计十分灵活，易于创建新规则。

Snort 的插件有预处理器，报文在被送到检测引擎之前可以先进行预处理；检测功能，针对单个报文/报文字段的快速检测；输出功能，获取其他插件的输出结果。

Snort 有三种主要的工作模式，嗅探模式、报文记录模式和 NIDS 模式，通过命令行选项配置不同的工作模式，NIDS 模式是默认的启动模式。嗅探模式类似 tcpdump，解码报文后输出到标准输出(控制台)，可支持 BPF 过滤规则，图 9-11 为捕获的数据报文截图。报文记录模式，可使用 ASCII, tcpdump, XML 和数据库等多种方式对记录的报文进行后续的分析、取证。NIDS 模式，在 BackTrack5 自带的 Snort 2.8.5.2 (Build 121) 上有4000多条规则，可支持多种检测模式，例如基于规则、统计异常、基于协议等。

![图 9-11 捕获的数据报文](attach/media/image12.png)

#### 9.5.2.2 Snort规则

![图 9-12 Snort规则](attach/media/image13.png)


Snort 为单行规则，大多数 snort 规则都写在一个单行上，或者在多行之间的行尾用"/"分隔。Snort 规则被分成两个逻辑部分：规则头和规则选项。规则头包含规则的动作，协议，源和目标ip地址与网络掩码，以及源和目标端口信息；规则选项部分包含报警消息内容和要检查的包的具体部分。

snort.conf 定义了默认规则文件的位置：var RULE_PATH /etc/snort/rules

绝大多数 snort 规则都是误用检测规则，即识别已知的入侵行为，其主要计算资源都用在了字符串匹配上。极少数的 snort 规则是异常检测规则，即基于统计异常的检测，例如 threshold.conf 使用阈值法，该方法中，Limit 是每统计周期的第一次阈值到达时就报警，每次统计周期最多报警一次。Threshold 是每统计周期的每M次阈值到达时报警，每次统计周报报警次数不限，Both 是以上2种的综合。

![图 9-13 Snort规则格式](attach/media/image14.png)


规则执行事的顺序并不是按照规则的出现顺序，而是按规则类型的优先级执行，优先级如下依次递减：

```
Pass >Drop > Alert > Log
```

![图9-14 处理流程](attach/media/image15.png)




![图 9-15 误用检测规则](attach/media/image16.png)


绝大多数 snort 规则都是误用检测规则，识别已知的入侵行为，Snort 的主要计算资源都用在了字符串匹配上。极少数的 snort 规则是异常检测，基于统计异常。有 threshold.conf 使用阈值法，Limit 是每统计周期的第一次阈值到达时就报警，每次统计周期最多报警一次。Threshold 是每统计周期的每M次阈值到达时报警，每次统计周报报警次数不限，Both 是以上2种的综合。


![图 9-16 异常检测规则](attach/media/image17.png)


#### 9.5.2.3 Snort架构

![图 9-17 Snort 数据流图](attach/media/image18.png)


Snort 的结构由4大软件模块组成，它们分别是：

（1）数据包嗅探模块——负责监听网络数据包，对网络进行分析；

（2）预处理模块——该模块用相应的插件来检查原始数据包，从中发现原始数据的“行为”，如端口扫描，IP 碎片等，数据包经过预处理后才传到检测引擎；

（3）检测引擎——该模块是 Snort 的核心模块。当数据包从预处理器送过来后，检测引擎依据预先设置的规则检查数据包，一旦发现数据包中的内容和某条规则相匹配，就通知报警模块，图9-18为检测引擎内部数据结构表示，图 9-19 为数据结构完全展开视图；

（4）输出报警/日志模块——经检测引擎检查后的Snort数据需要以某种方式输出。如果检测引擎中的某条规则被匹配，则会触发一条报警，这条报警信息会通过网络、UNIXsocket、WindowsPopup(SMB)、SNMP 协议的 trap 命令传送给日志文件，甚至可以将报警传送给第三方插件（如SnortSam），另外报警信息也可以记入 SQL 数据库。

![图 9-18 检测引擎内部数据结构表示](attach/media/image19.png)

![图 9-19 检测引擎内部数据结构展开图](attach/media/image20.png)

关于 Snort 的配置命令：/etc/snort/snort.conf，主要是定义网络环境相关变量，配置动态加载的库，配置预处理器，配置输出插件，增加运行时配置指令，定义启用的规则集。

### 9.5.3 Suricata

[Suricata](https://suricata-ids.org/) 是非盈利性组织开放信息安全基金会（Open Information Security Foundation, OISF）主导和支持的一个免费、开源、成熟、高性能和健壮的网络威胁检测引擎，可以提供实时入侵检测、内联入侵保护（Intrusion Prevention System, IPS）、网络安全监控（Network Security Monitoring, NSM）和离线 pcap 处理。Suricata 使用可扩展的规则和签名语言来检查网络，流量，支持使用Lua脚本语言检测复杂威胁。Suricata 使用标准 YAML 输入格式和 JSON 输出格式，使得和第三方安全信息和事件管理（Security Information and Event Management, SIEM）工具（例如Splunk、ELK和其他数据库）集成十分容易。

![图 9-20 Suricata产生的报警日志可视化效果图](attach/media/kibana-selks4.png)

Suricata和Snort的特性对比如下表格所示：

| 对比项 | Snort |	Suricata |
|--------|-------|-----------|
| 开发者 | Sourcefire, Inc.	| Open Information Security Foundation (OISF) |
| 项目历史 |	1998 - |	2009 - |
| 编程语言 | 	C |	C |
| 操作系统 | 跨平台 | 跨平台 |
| 最新稳定版 | [2.9.11 (2017/09/05)](https://s3.amazonaws.com/snort-org-site/production/release_files/files/000/006/397/original/release_notes_2.9.11.txt?AWSAccessKeyId=AKIAIXACIED2SPMSC7GA&Expires=1511841091&Signature=JGm6my%2BW7l8Dvb%2BjakXkOYLF0pg%3D) |	4.0.1 (2017/10/18) |
| 并行处理 | 单线程（[Snort3完全重写支持多线程](https://github.com/snort3/snort3)） | 多线程 |
| IPv6支持 | 有 | 有 |
| Snort (VRT)规则语法兼容性 | 兼容 | 兼容 |
| Emerging Threats Rules 兼容性 | 兼容 | 兼容 |
| 日志格式 | Unified2 |	Unified2 / JSON |

关于Suricata的使用可以查看[官网在线手册](http://suricata.readthedocs.io/en/latest/)。

### 9.5.4 Bro / Zeek

[2018 年 10 月 11 日](https://blog.zeek.org//2018/10/renaming-bro-project_11.html) 原 `Bro` 开发者团队宣布将拥有 20 年历史的开源项目 `Bro` 更名为 `Zeek` ，原有 `Bro` 相关文档和工具包内包含的程序命名将经历一段 `Bro` 和 `Zeek` 共存的时期，最终会将所有名称中包含 `bro` 的工具和术语统一迁移到 `zeek` 相关命名规范。

> Zeek is the new name for the long-established Bro system. Note that parts of the system retain the "Bro" name, and it also often appears in the documentation and distributions.

根据 Zeek 官网的文档介绍，可以总结出 Zeek 的主要特性：

* 部署
    * 运行在普通硬件和标准UNIX系统（包括 Linux, FreeBSD, MacOS）
    * 基于网络流量分流或镜像端口方式的完全被动流量分析
    * 基于标准 libpcap 接口捕获数据报文
    * 实时和离线分析
    * 支持大规模集群部署
    * 同时支持单机和集群配置的统一管理框架
    * 基于 BSD 协议开源
* 分析
    * 全面行为日志记录用于离线分析和取证
    * 端口无关的应用层协议分析
    * 支持多种应用层协议（包括：DNS、FTP、HTTP、IRC、SMTP、SSH、SSL）
    * 应用层负载内容分析包括 MD5/SHA1 计算用于指纹
    * 完全 IPv6 支持
    * 隧道协议检测和分析（包括 Ayiya, Teredo, GTPv1）。Zeek 重组识别的隧道协议负载就像没有使用隧道协议一样去分析内层应用层协议数据。
    * 协议分析期间支持大量合法性检查方法
    * 支持 IDS 风格的模式匹配
* 可编程性
    * 使用图灵完备语言来完成任意分析任务的表达刻画
    * 基于事件编程模型
    * 内置专业领域数据结构支持，例如 IP 地址（IPv4 和 IPv6 地址透明处理）、端口号和时钟
    * 广泛支持基于时间（窗口）的追踪和网络状态管理
* 接口
    * 默认输出为格式化后的 ASCII 日志
    * 可选后端支持 ElasticSearch 和数据序列。更多数据库接口仍在开发中。
    * 支持外部数据实时导入集成分析。实时数据库仍在开发中。
    * 外部C语言编程库用于 Zeek 事件和外部程序交换。支持 Perl、Python 和 Ruby 语言混编。
    * 支持从脚本语言调用任何外部可执行程序。

![图 9-21 Bro 架构图](attach/media/Bro_Arch.png)

Zeek 在架构上有2个主要组件：事件引擎（核心）将入站报文流处理减少为一系列更高层次事件。这些事件采用策略无关术语刻画了网络行为，即：描述了观测到的表现（what）而不是为什么（why）或重要性程度。例如，每个网络 HTTP 请求都被转换为一系列相关的http_request事件，包括：参与的 IP 地址、端口、URI、HTTP 版本等。事件本身并没有任何进一步解读，例如：URI是否对应一个已知恶意站点。

上述语义特征则来自 Zeek 的第二个核心组件输出：脚本解释引擎，该引擎执行一组使用 Zeek 自定义脚本语言编写的事件处理函数。这些脚本可以描述一个站点的安全策略，即：当检测到不同行为时该采取哪些响应行动。更一般的情形是 Zeek 能够从输入流量中推导出任意想得到的特征和统计数据。Zeek 编程语言内置一系列（入侵检测）领域相关数据结构和相关处理函数，更为关键的是支持脚本维护时间状态机，从而可以跨连接会话和主机边界对观测到的行为进行追溯和关联。Zeek 脚本可以产生实时告警并按需执行任意外部程序，例如：对检测到的一个攻击触发一次主动响应。

Zeek 相比较于 Snort 和 Suricata 具有以下独特特性：

* 可扩展性。同时支持单机和集群配置的统一管理框架，这使得我们所做的系统不会局限于原型演示系统，可以随时在流量采集这个需求上实现快速扩展；
* 全面行为日志记录用于离线分析和取证，特别是这些日志还可以实时输出为 ASCII 格式文本文件，我们可以很方便的把这些日志实时导入到一个实时日志分析引擎进行二次分析。结合主机和设备日志、情景数据和威胁情报，为关联分析提供了必要的来源输入数据；
* 可编程性，使得我们可以按需实时对网络流量进行就近在线分析和关键信息抽取，可以随时根据系统架构中不同组件的实现方案进行灵活适配，满足系统总体架构设计需求。

下图就是 Zeek 集群模式运行的系统架构拓扑图，通过使用流量负载均衡设备、增加 Zeek 引擎数量，可以实现系统处理能力的水平平滑扩展升级。

![图 9-22 Bro 集群架构拓扑图](attach/media/Bro_Arch_Cluster.png)

Zeek 对网络流量实时分析并将分析结果分类存储到本地文件系统的不同文件，根据[官方文档说明](https://www.zeek.org/sphinx/script-reference/log-files.html)，具体来说分成几个大类，每个大类中又细分了多种不同的日志类别：

<table >
   <tr>
      <td>日志类别</td>
      <td>文件名</td>
      <td>文件内容</td>
   </tr>
   <tr>
      <td rowspan="6">协议解析</td>
      <td><a href="https://www.bro.org/sphinx-git/scripts/base/protocols/conn/main.bro.html">conn.log</a></td>
      <td>TCP/UDP/ICMP 连接历史记录</td>
   </tr>
   <tr>
    <td><a href="https://www.bro.org/sphinx-git/scripts/base/protocols/dns/main.bro.html">dns.log</a></td>
    <td>DNS 解析历史记录</td>
   </tr>
   <tr>
    <td><a href="https://www.bro.org/sphinx-git/scripts/base/protocols/dhcp/main.bro.html">dhcp.log</a></td>
    <td>DHCP 活动记录，可以用于发现新入网主机</td>
   </tr>
   <tr>
     <td><a href="https://www.bro.org/sphinx/scripts/base/protocols/http/main.bro.html#type-HTTP::Info">http.log</a></td>
     <td>HTTP 请求响应活动记录</td>
   </tr>
   <tr>
    <td><a href="https://www.bro.org/sphinx/scripts/base/protocols/ssh/main.bro.html#type-SSH::Info">ssh.log</a></td>
    <td>SSH 活动记录</td>
  </tr>
  <tr>
    <td><a href="https://www.bro.org/sphinx/scripts/base/frameworks/tunnels/main.bro.html#type-Tunnel::Info">tunnel.log</a></td>
    <td>隧道协议活动记录</td>
  </tr>
  <tr>
     <td rowspan="3">文件负载提取、还原和分析</td> 
     <td><a href="https://www.bro.org/sphinx/scripts/base/frameworks/files/main.bro.html#type-Files::Info">files.log</a></td>
     <td>文件分析记录（散列值计算结果、文件还原存储路径、文件大小、恶意代码开放API检索结果记录等）</td>
  </tr>
  <tr>
    <td><a href="https://www.bro.org/sphinx/scripts/base/files/x509/main.bro.html#type-X509::Info">x509.log</a></td>
    <td>识别提取成功的 X.509 证书信息</td>
  </tr>
  <tr>
    <td><a href="https://www.bro.org/sphinx/scripts/base/files/pe/main.bro.html#type-PE::Info">pe.log</a></td>
    <td>PE 文件识别记录</td>
  </tr>
  <tr>
    <td rowspan="2">检测报警</td>
    <td><a href="https://www.bro.org/sphinx/scripts/base/frameworks/intel/main.bro.html#type-Intel::Info">intel.log</a></td>
    <td>威胁情报匹配记录</td>
  </tr>
  <tr>
    <td><a href="https://www.bro.org/sphinx/scripts/base/frameworks/notice/main.bro.html#type-Notice::Info">notice.log</a></td>
    <td>Bro通知事件记录，目前已实现的包含 APT 检测相关重要告警信息类型包括：SSL 证书未通过合法性校验、请求疑似恶意 /C2 域名以及 ARP 欺骗类消息告警</td>
  </tr>
  <tr>
    <td rowspan="2">情景数据（网络概况）</td>
    <td><a href = "https://www.bro.org/sphinx/scripts/policy/protocols/ssl/known-certs.bro.html#type-Known::CertsInfo">known_certs.log</a></td>
    <td>已识别 SSL 证书记录，用于避免在 x509.log 中重复记录条目</td>
  </tr>
  <tr>
    <td><a href="https://www.bro.org/sphinx/scripts/base/frameworks/software/main.bro.html#type-Software::Info">software.log</a> </td>
    <td>已识别通信软件详细版本信息记录</td>
  </tr>
  <tr>
    <td rowspan="2">杂项</td> 
    <td><a href="https://www.bro.org/sphinx/scripts/base/frameworks/dpd/main.bro.html#type-DPD::Info">dpd.log</a></td>
    <td>深度包检测失败消息</td>
  </tr>
  <tr>
    <td><a href="https://www.bro.org/sphinx/scripts/base/frameworks/notice/weird.bro.html#type-Weird::Info">weird.log</a> </td>
    <td>异常网络协议行为记录</td>
  </tr>
  <tr>
    <td>Bro 状态诊断</td>
    <td><a href="https://www.bro.org/sphinx/scripts/base/protocols/ssl/main.bro.html#type-SSL::Info">ssl.log</a> </td>
    <td>SSL/TLS 握手信息记录</td>
  </table>
</table>

## 9.6 思考题

* 如何理解“入侵检测系统的误报率越高，漏报率低的概率就越高”这句话？
* 描述入侵检测系统的误用检测算法和异常检测算法，并各举一实际算法说明。
