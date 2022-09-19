# 实验

## HTTP代理服务器实验

Q：使用 http 代理服务器访问 HTTPS 站点时，通信传输内容是否会被代理服务器“看到”？

A：结论是代理服务器不知道客户端和服务器的 HTTPS 通信内容，但代理服务器知道客户端访问了哪个 HTTPS 站点，这是由 http 代理的协议机制决定的：代理客户端会发送 Connect 请求到 http 代理服务器。

实验验证：在 Kali Linux 中安装 tinyproxy，然后用主机设置浏览器代理指向 tinyproxy 建立的 HTTP 正向代理，在 Kali 中用 wireshark 抓包，分析抓包过程，理解 HTTP 正向代理 HTTPS 流量的特点。

提醒注意：

> HTTP 代理服务器在转发客户端请求时，可能会添加 Via 字段，从而向目标站点暴露客户端正在使用代理访问。类似的，匿名通信应用 tor 的部分出口节点也会在http请求中自动加入 via 字段，向被访问站点宣告：当前请求正在使用匿名通信网络 tor 提供的匿名通信服务。

Q: 了解什么是 HSTS

A: HSTS（HTTP Strict Transport Security）机制：

* [服务器通过实现 HSTS 机制，可以帮助客户端（例如浏览器）强制](https://www.owasp.org/index.php/HTTP_Strict_Transport_Security)
  * 客户端和服务器之间的所有通信流量必须使用 HTTPS
  * SSL 证书合法性校验

![图1 在Chrome的开发者工具中查看启用HSTS站点的通信数据](attach/HSTS.png)

![图2 未启用HSTS站点被SSL中间人攻击时Chrome浏览器的警告提示](attach/HSTS-2.png)

![图3 未启用HSTS站点被SSL中间人攻击时Chrome浏览器在用户允许继续访问情况下](attach/HSTS-3.png)

![图4 启用HSTS站点被SSL中间人攻击时Chrome浏览器禁止用户继续访问](attach/HSTS-4.png)

Ref:

- [使用HTTP代理服务器的安全性简评](http://www.williamlong.info/archives/2210.html) 
- [如何使用代理服务器上网](http://www.williamlong.info/archives/2057.html)

### tinyproxy

tinyproxy 使用主要注意事项：

```bash
apt-get update
apt-get install tinyproxy

# 编辑tinyproxy，取消Allow 10.0.0.0/8行首注释
/etc/init.d/tinyproxy start

# 设置虚拟机联网方式为NAT和端口转发，默认tinyproxy监听8888端口
# 主机浏览器设置代理指向tinyproxy的服务地址
# 虚拟机里开启wireshark抓包
# 主机访问https站点
# 结束抓包，分析抓包结果
```

wireshark 分析HTTP代理流量技巧：

* http.request.method eq CONNECT 查看所有HTTPS代理请求
* http.request.method eq GET 查看所有HTTP GET代理请求
* [使用wireshark解密HTTPS流量的方法](http://support.citrix.com/article/CTX116557) [方法2](https://wiki.wireshark.org/SSL)
* [使用wireshark提取pcap包中的SSL证书](http://mccltd.net/blog/?p=2036)
  * wireshark 首选项中确认 TCP 协议的 Allow subdissector to reassemble TCP streams 选项处于启用状态
  * 通过显示筛选过滤规则（例如：tcp.port == 443），找到 SSL 会话
  * 通过 packet list 里的 info 列找到 Certificate
      * 在 packet details 面板里依次展开Handshake Protocol: Certificate --> Certificates，如果有多个证书，会看到多个默认折叠起来的 Certificate
      * 右键选中 Certificate，在右键菜单里使用 Export Selected Packet Bytes 功能即可导出 DER 格式的 SSL 证书
  * 使用 openssl 命令行工具解析 DER 证书
  openssl x509 -in xxx.der -inform der -text -noout


### buprsuite

- [铁器 · Burp Suite](http://daily.zhihu.com/story/3905128)

# 延伸阅读

- [微软 hotmail SSL 证书被劫持的真实案例](http://www.freebuf.com/news/45929.html)
- [GoAgent 安全风险提示](https://www.bamsoftware.com/sec/goagent-advisory.html)
- [密码学应用实践的小学期 Wiki（回顾签发证书和配置 Apache 的 HTTPS 站点方法）](https://c4pr1c3.github.io/cuc-wiki/ac.html)
