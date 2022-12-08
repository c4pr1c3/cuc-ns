# Web 应用漏洞攻防

## 实验目的

* 了解常见 Web 漏洞训练平台；
* 了解 常见 Web 漏洞的基本原理；
* 掌握 OWASP Top 10 及常见 Web 高危漏洞的漏洞检测、漏洞利用和漏洞修复方法；

## 实验环境

* WebGoat
* Juice Shop

## 实验要求

* [ ] 每个实验环境完成不少于 **5** 种不同漏洞类型的漏洞利用练习；
* [ ] （可选）使用不同于官方教程中的漏洞利用方法完成目标漏洞利用练习；
* [ ] （可选）**最大化** 漏洞利用效果实验；
* [ ] （可选）编写 **自动化** 漏洞利用脚本完成指定的训练项目；
* [ ] （可选）定位缺陷代码；
* [ ] （可选）尝试从源代码层面修复漏洞；

## WebGoat 训练平台与其他常见漏洞训练平台横向对比

| 漏洞类型  | [WebGoat 7.1](https://hub.docker.com/r/webgoat/webgoat-7.1/)  | [WebGoat 8.0](https://hub.docker.com/r/webgoat/webgoat-8.0/)  | [DVWA](https://hub.docker.com/r/vulnerables/web-dvwa/)  | [Vulhub](https://vulhub.org/#/environments/)  |  
|---|---|---|---|---|
| 未验证的用户输入  | Parameter Tampering->Bypass HTML Field Restrictions / Bypass Client Side JavaScript Validation | Client side  |   | Weblogic 常规渗透测试环境  | 
| CSRF  |   | Cross-Site Request Forgeries  | ✓  |   | 
| 缓冲区溢出  | Buffer OverFlaws->Off-by-One OverFlaws  |   |   |   | 
| 文件上传漏洞  | Malicious Execution  |   | ✓  | CVE-2018-2894  |  
| 文件包含  |   |   |  ✓ | PHP文件包含漏洞（利用phpinfo）  |  
| XXE  |  Parameter Tampering->XXE | XXE  |   |   |  
| 反序列化  |   | Insecure Deserialization  |   | CVE-2015-5254, CVE-2017-3066, fastjson 反序列化导致任意命令执行漏洞  | 
| 第三方组件缺陷  |   | Vulnerable Components  |   | CVE-2017-12794, CVE-2018-14574, CVE-2014-3120, CVE-2015-5531, fastjson 反序列化导致任意命令执行漏洞, Flask（Jinja2） 服务端模板注入漏洞, S2-系列漏洞一箩筐, Imagetragick 命令执行漏洞（CVE-2016–3714）  | 
| SQL 注入 | Injection Flaws->SQL Injection  | Injection Flaws->SQL Injection  |   | CVE-2014-3704 |  
| 命令注入 | Injection Flaws->Command Injection   |   | ✓  | CVE-2017-12636  |  
| SSRF |   |   |   | CVE-2016-1897/CVE-2016-1898, Weblogic SSRF漏洞  |  
| XSS |   | Cross Site Scripting | ✓  | CVE-2017-12794  |  
| 信息泄漏 |   |   |   | ThinkPHP5 SQL注入漏洞 && 敏感信息泄露  |
| Web 服务器 URI 解析类漏洞 |   |   |   | CVE-2017-15715 / Apache HTTPD 未知后缀解析漏洞 / HTTPoxy漏洞（CVE-2016-5385） | 
| 不当配置缺陷 |   |   |   | Nginx 配置错误导致漏洞 / Nginx 解析漏洞复现  | 
| 脆弱的访问控制 | Session Management Flaws | Authentication Flaws / Access Control Flaws  | Weak Session IDs  | CVE-2017-12635  | 


### WebGoat 7.0.1 实验

基于[WebGoat 7.0.1 Release](https://github.com/WebGoat/WebGoat/tree/7.0.1)

* Authentication Flaws ( 6.脆弱的访问控制 )
    * Forgot Password
    * Multi Level Login 2
* Cross-Site Scripting 
    * Stored XSS Attacks ( 4.跨站点脚本(XSS) )
    * Cross Site Request Forgery (CSRF) ( 11.跨站点请求伪造 )
* Injection Flaws ( 3. 注⼊缺陷 )
    * Command injection
    * LAB: SQL Injection
* Malicious Execution
    * Malicious File Execution ( 13. ⽂件上传漏洞 )
* Parameter Tampering ( 1. 未验证的用户输⼊ )
    * Bypass HTML Field Restrictions
    * Exploit Hidden Fields
* Session Management Flaws ( 7.脆弱认证和会话管理 )
    * Session Fixation

#### 修改WebGoat 7.0.1的默认监听IP地址

编辑 ``.extract/webapps/WebGoat/WEB-INF/web.xml``，将其中的所有localhost替换成你想要让WebGoat内置Web服务器监听的IP地址。修改后的相关行配置类似如下：

```
http://192.168.56.101:8080/{context-path}/servlet/{classname}
http://192.168.56.101:8080/{contextpath}/graph
http://192.168.56.101:8080/{contextpath}/saveCustomer.mvc
```

## <del>真实</del> Web 应用训练平台 

> [OWASP Juice Shop](https://github.com/bkimminich/juice-shop) : Probably the most modern and sophisticated insecure web application

### 项目特色

* [使用现代 Web 开发技术](https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/introduction/motivation.html) 开发的 `富互联网应用`（ ***Rich Internet Application, RIA*** ）或 `单页应用` （ ***Single Page Application, SPA*** ）。

![](attach/media/juice-shop-architecture-diagram.png)

* 相比较于现有的其他「漏洞训练」项目，本项目在产品「仿真」程度上更贴近一个「真实」应用：电商系统。
* DevOps 最佳实践: Automated Build, CI/CD & Code Analysis
* 支持 `CTF` 模式运行：官方支持集成到 [CTFd](https://ctfd.io) 或 [FBCTF](https://github.com/facebook/fbctf)
* [教程完备](https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content)

### 包含漏洞类型

根据 [官方项目介绍 PPT](http://bkimminich.github.io/juice-shop/#/5) ，本项目包含超过 85 个安全挑战，包含的漏洞类型如下图：

[![vulnerability categories breakdown](attach/media/juice-shop-categories.png)](https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part1/categories.html)

| Category                    | OWASP                                                                                                                                      | CWE                                                                                                                                                                                                                                            |
|:----------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 注入 | [A1:2017](https://www.owasp.org/index.php/Top_10-2017_A1-Injection)                                                                        | [CWE-74](https://cwe.mitre.org/data/definitions/74.html)                                                                                                                                                                                       |
| 身份认证失效 | [A2:2017](https://www.owasp.org/index.php/Top_10-2017_A2-Broken_Authentication)                                                            | [CWE-287](https://cwe.mitre.org/data/definitions/287.html), [CWE-352](https://cwe.mitre.org/data/definitions/352.html)                                                                                                                         |
| 遗忘信息 | [OTG-CONFIG-004](https://www.owasp.org/index.php/Review_Old,_Backup_and_Unreferenced_Files_for_Sensitive_Information_%28OTG-CONFIG-004%29) |                                                                                                                                                                                                                                                |
| 自身安全加固 | [A10:2017](https://www.owasp.org/index.php/Top_10-2017_A10-Insufficient_Logging%26Monitoring)                                              | [CWE-326](https://cwe.mitre.org/data/definitions/326.html), [CWE-601](https://cwe.mitre.org/data/definitions/601.html)                                                                                                                         |
| 敏感数据曝光 | [A3:2017](https://www.owasp.org/index.php/Top_10-2017_A3-Sensitive_Data_Exposure)                                                          | [CWE-200](https://cwe.mitre.org/data/definitions/200.html), [CWE-327](https://cwe.mitre.org/data/definitions/327.html), [CWE-328](https://cwe.mitre.org/data/definitions/328.html), [CWE-548](https://cwe.mitre.org/data/definitions/548.html) |
| XXE | [A4:2017](https://www.owasp.org/index.php/Top_10-2017_A4-XML_External_Entities_%28XXE%29)                                                  | [CWE-611](https://cwe.mitre.org/data/definitions/611.html)                                                                                                                                                                                     |
| 输入校验不当 | [ASVS V5](https://www.owasp.org/index.php/ASVS_V5_Input_validation_and_output_encoding)                                                    | [CWE-20](https://cwe.mitre.org/data/definitions/20.html)                                                                                                                                                                                       |
| 访问控制失效 | [A5:2017](https://www.owasp.org/index.php/Top_10-2017_A5-Broken_Access_Control)                                                            | [CWE-22](https://cwe.mitre.org/data/definitions/22.html), [CWE-285](https://cwe.mitre.org/data/definitions/285.html), [CWE-639](https://cwe.mitre.org/data/definitions/639.html)                                                               |
| 安全配置缺陷 | [A6:2017](https://www.owasp.org/index.php/Top_10-2017_A6-Security_Misconfiguration)                                                        | [CWE-209](https://cwe.mitre.org/data/definitions/928.html)                                                                                                                                                                                     |
| XSS  | [A7:2017](https://www.owasp.org/index.php/Top_10-2017_A7-Cross-Site_Scripting_%28XSS%29)                                                   | [CWE-79](https://cwe.mitre.org/data/definitions/79.html)                                                                                                                                                                                       |
| 反序列化漏洞 | [A8:2017](https://www.owasp.org/index.php/Top_10-2017_A8-Insecure_Deserialization)                                                         | [CWE-502](https://cwe.mitre.org/data/definitions/502.html)                                                                                                                                                                                     |
| 缺陷组件（供应链安全） | [A9:2017](https://www.owasp.org/index.php/Top_10-2017_A9-Using_Components_with_Known_Vulnerabilities)                                      |                                                                                                                                                                                                                                                |
| 混淆不等于安全 |                                                                                                                                            | [CWE-656](https://cwe.mitre.org/data/definitions/656.html)                                                                                                                                                                                     |
| 条件竞争 | [OWASP-AT-010](https://www.owasp.org/index.php/Testing_for_Race_Conditions_%28OWASP-AT-010%29)                                                 | [CWE-362](http://cwe.mitre.org/data/definitions/362.html)                                                                                                                                                                                      |

## Kali 上安装 Docker 注意事项

以本书写作时使用 Kali 系统版本为例，如下所示：当前 Kali 版本为 `2019.2` ，注意到其中的 `Codename` 字段为 `n/a` ，即不可用。

```bash
lsb_release -a
# No LSB modules are available.
# Distributor ID: Kali
# Description:    Kali GNU/Linux Rolling
# Release:        2019.2
# Codename:       n/a

# 当前 Kali 版本自带的 Docker 最新版软件包名为 docker.io
apt-cache policy docker.io
# docker.io:
#   Installed: (none)
#   Candidate: 19.03.4+dfsg2-2
#   Version table:
#      19.03.4+dfsg2-2 500
#         500 http://http.kali.org/kali kali-rolling/main amd64 Packages

# Docker 官方当前使用的软件包名为 docker-ce ，但在 Kali 上没有使用这个软件包名
apt-cache policy docker-ce
# docker-ce:
#   Installed: (none)
#   Candidate: (none)
#   Version table:
```

根据 [`Kali` 官方的介绍](https://www.kali.org/docs/policy/kali-linux-relationship-with-debian/)，`Kali` 是基于 [Debian Testing](https://www.debian.org/releases/testing/) 版本进行二次构建的，因此绝大部分 `Kali` 上的软件包都是来自 `Debian Testing` 版本。在某些情况下，一些较新版本的软件甚至是来自于 `Debian Unstable` 或者 `Debian Experimental` 版本。

以下命令是在 `Debian buster` 版本上执行 `lsb_release -a` 的结果，注意到其中的 `Codename` 字段值为：`buster` 。当我们在执行 `lsb_release -cs` 的时候输出的值就是这里的 `Codename` ，记住这里 `lsb_release -cs` 的输出结果差异对于理解后续 [Docker 官方的安装指南中](https://docs.docker.com/install/linux/docker-ce/debian/) 的安装指令为什么不能直接在 `Kali` 上执行是有帮助的。

```bash
lsb_release -a
# No LSB modules are available.
# Distributor ID: Debian
# Description:    Debian GNU/Linux 10 (buster)
# Release:        10
# Codename:       buster
```

推荐按照 [Docker 官方的安装指南](https://docs.docker.com/install/linux/docker-ce/debian/) 在 Kali 上安装 `Docker` ，但需要注意的是：不能在 Kali 上直接使用以下命令去添加 `Docker` 官方的 apt 镜像源地址：

```bash
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"
```

一来，在 `Kali` 上 `lsb_release -cs` 的输出结果是 `n/a` ，这是一个非法的 `Debian` 发行版代号。所以，此处应该替换成当前最新的 `Debian` 稳定版代号（`Docker` 官方通常不支持 `Debian Testing` 版本，例如 `buster` 是当前 `Debian` 系列最新的稳定版本，此时的 `Testing` 版本代号为 `bullseye`），例如当前是 `buster` 。
二来，建议用浏览器打开 [https://download.docker.com/linux/debian/dists/](https://download.docker.com/linux/debian/dists/) 确认存在 `buster` 子目录（当前确实不存在 `bullseye` 子目录，证明 `Docker` 官方确实还不支持 `Debian Testing` 版本）。

需要注意的是，以下修改后添加 apt 镜像源地址的方法执行依然会报错：

```bash
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   buster \
   test"
# Traceback (most recent call last):
#  File "/usr/bin/add-apt-repository", line 95, in <module>
#    sp = SoftwareProperties(options=options)
#  File "/usr/lib/python3/dist-packages/softwareproperties/SoftwareProperties.py", line 109, in __init__
#    self.reload_sourceslist()
#  File "/usr/lib/python3/dist-packages/softwareproperties/SoftwareProperties.py", line 599, in reload_sourceslist
#    self.distro.get_sources(self.sourceslist)
#  File "/usr/lib/python3/dist-packages/aptsources/distro.py", line 93, in get_sources
#    (self.id, self.codename))
#aptsources.distro.NoDistroTemplateException: Error: could not find a distribution template for Kali/n/a
```

可以使用以下单行命令在 `/etc/apt/sources.list` 中添加 `Docker` 官方的 apt 镜像源地址：

```bash
if [[ $(grep -c "docker.com" /etc/apt/sources.list) -eq 0 ]];then echo "deb https://download.docker.com/linux/debian buster stable" >> /etc/apt/sources.list;fi
```

在执行 `apt update` 之前应先添加 `Docker` 官方的 GPG 公钥到系统受信任公钥数据库，如下操作：

```bash
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
apt update
```

此时再执行 `apt-cache policy docker-ce` 就能看到是由 `Docker` 官方 apt 镜像源提供的最新 `Docker` 社区稳定版了。

```bash
apt-cache policy docker-ce | head
# docker-ce:
#   Installed: (none)
#   Candidate: 5:19.03.5~3-0~debian-buster
#   Version table:
#      5:19.03.5~3-0~debian-buster 500
#         500 https://download.docker.com/linux/debian buster/stable amd64 Packages
#      5:19.03.4~3-0~debian-buster 500
#         500 https://download.docker.com/linux/debian buster/stable amd64 Packages
#      5:19.03.3~3-0~debian-buster 500
#         500 https://download.docker.com/linux/debian buster/stable amd64 Packages
```

接下来的 `Docker` 安装就可以使用 `apt install docker-ce` 完成了。`docker-compose` 的安装依然建议按照 [Docker 官方文档的安装指南](https://docs.docker.com/compose/install/) 进行操作。

## 工具推荐

* [burpsuite (Kali内置），免费版即可满足课程实验和大部分实战渗透测试之手工测试需求](https://portswigger.net/burp/)
* [本章实验所需实验环境 `docker-compose up -d` 一键搭建](https://github.com/c4pr1c3/ctf-games)

## 参考资料推荐

* [Burp Suite 实战指南](https://www.gitbook.com/book/t0data/burpsuite/details)


