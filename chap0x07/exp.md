# 实验

| 漏洞类型  | [WebGoat 7.1](https://hub.docker.com/r/webgoat/webgoat-7.1/)  | [WebGoat 8.0](https://hub.docker.com/r/webgoat/webgoat-8.0/)  | [DVWA](https://hub.docker.com/r/vulnerables/web-dvwa/)  | [Vulhub](https://vulhub.org/#/environments/)  |  其他 |
|---|---|---|---|---|---|
| 未验证的用户输入  | Parameter Tampering->Bypass HTML Field Restrictions / Bypass Client Side JavaScript Validation | Client side  |   | Weblogic 常规渗透测试环境  |   |
| CSRF  |   | Cross-Site Request Forgeries  | ✓  |   |   |
| 缓冲区溢出  | Buffer Overflows->Off-by-One Overflows  |   |   |   |   |
| 文件上传漏洞  | Malicious Execution  |   | ✓  | CVE-2018-2894  |   |
| 文件包含  |   |   |  ✓ | PHP文件包含漏洞（利用phpinfo）  |   |
| XXE  |  Parameter Tampering->XXE | XXE  |   |   |   |
| 反序列化  |   | Insecure Deserialization  |   | CVE-2015-5254, CVE-2017-3066, fastjson 反序列化导致任意命令执行漏洞  |   |
| 第三方组件缺陷  |   | Vulnerable Components  |   | CVE-2017-12794, CVE-2018-14574, CVE-2014-3120, CVE-2015-5531, fastjson 反序列化导致任意命令执行漏洞, Flask（Jinja2） 服务端模板注入漏洞, S2-系列漏洞一箩筐, Imagetragick 命令执行漏洞（CVE-2016–3714）  |   |
| SQL 注入 | Injection Flaws->SQL Injection  | Injection Flaws->SQL Injection  |   | CVE-2014-3704 |   |
| 命令注入 | Injection Flaws->Command Injection   |   | ✓  | CVE-2017-12636  |   |
| SSRF |   |   |   | CVE-2016-1897/CVE-2016-1898, Weblogic SSRF漏洞  |   |
| XSS |   | Cross Site Scripting | ✓  | CVE-2017-12794  |   |
| 信息泄漏 |   |   |   | ThinkPHP5 SQL注入漏洞 && 敏感信息泄露  |   |
| Web 服务器 URI 解析类漏洞 |   |   |   | CVE-2017-15715 / Apache HTTPD 未知后缀解析漏洞 / HTTPoxy漏洞（CVE-2016-5385） |   |
| 不当配置缺陷 |   |   |   | Nginx 配置错误导致漏洞 / Nginx 解析漏洞复现  |   |
| 脆弱的访问控制 | Session Management Flaws | Authentication Flaws / Access Control Flaws  | Weak Session IDs  | CVE-2017-12635  |   |


## WebGoat 7.0.1 实验

基于[WebGoat 7.0.1 Release](https://github.com/WebGoat/WebGoat/tree/7.0.1)

* Authentication Flows ( 6.脆弱的访问控制 )
    * Forgot Password
    * Multi Level Login 2
* Cross-Site Scripting 
    * Stored XSS Attacks ( 4.跨站点脚本(XSS) )
    * Cross Site Request Forgery (CSRF) ( 11.跨站点请求伪造 )
* Injection Flows ( 3. 注⼊缺陷 )
    * Command injection
    * LAB: SQL Injection
* Malicious Execution
    * Malicious File Execution ( 13. ⽂件上传漏洞 )
* Parameter Tampering ( 1. 未验证的用户输⼊ )
    * Bypass HTML Field Restrictions
    * Exploit Hidden Fields
* Session Management Flows ( 7.脆弱认证和会话管理 )
    * Session Fixation

### 修改WebGoat 7.0.1的默认监听IP地址

编辑 ``.extract/webapps/WebGoat/WEB-INF/web.xml``，将其中的所有localhost替换成你想要让WebGoat内置Web服务器监听的IP地址。修改后的相关行配置类似如下：

```
http://192.168.56.101:8080/{context-path}/servlet/{classname}
http://192.168.56.101:8080/{contextpath}/graph
http://192.168.56.101:8080/{contextpath}/saveCustomer.mvc
```

## 工具推荐

* [burpsuite (Kali内置），免费版即可满足课程实验和大部分实战渗透测试之手工测试需求](https://portswigger.net/burp/)

## 参考资料推荐

* [Burp Suite 实战指南](https://www.gitbook.com/book/t0data/burpsuite/details)


