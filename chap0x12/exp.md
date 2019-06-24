# 实验

[课件内配套案例：pcap attack trace实验使用的pcap包下载](attack-trace.pcap)

## 使用bro来完成取证分析

### 安装bro

```bash
# apt-get install bro bro-aux
```

### 实验环境基本信息

```bash
root@KaliRolling:/usr/share/bro/site# lsb_release -a
No LSB modules are available.
Distributor ID: Kali
Description:    Kali GNU/Linux Rolling
Release:    kali-rolling
Codename:   kali-rolling
root@KaliRolling:/usr/share/bro/site# uname -a
Linux KaliRolling 4.6.0-kali1-amd64 #1 SMP Debian 4.6.4-1kali1 (2016-07-21) x86_64 GNU/Linux
root@KaliRolling:/usr/share/bro/site# bro -v
bro version 2.4.1
```

### 编辑bro配置文件

* 编辑 ```/etc/bro/site/local.bro```，在文件尾部追加两行新配置代码

```bash
@load frameworks/files/extract-all-files
@load mytuning.bro
```

* 在```/etc/bro/site/```目录下创建新文件mytuning.bro，[内容为](https://www.bro.org/documentation/faq.html#why-isn-t-bro-producing-the-logs-i-expect-a-note-about-checksums)：

```bash
redef ignore_checksums = T;
```

### 使用bro自动化分析pcap文件

```bash
bro -r attack-trace.pcap /etc/bro/site/local.bro
```

出现警告信息```WARNING: No Site::local_nets have been defined.  It's usually a good idea to define your local networks.```对于本次入侵取证实验来说没有影响。

如果要解决上述警告信息，也很简单，同样是编辑```mytuning.bro```，增加一行变量定义即可

```bash
redef Site::local_nets = { 192.150.11.0/24 };
```

注意添加和不添加上述一行变量定义除了bro运行过程中是否会产生警告信息的差异，增加这行关于本地网络IP地址范围的定义对于本次实验来说会新增2个日志文件，会报告在当前流量（数据包文件）中发现了本地网络IP和该IP关联的已知服务信息。

在attack-trace.pcap文件的当前目录下会生成一些```.log```文件和一个extract_files目录，在该目录下我们会发现有一个文件。

```bash
# file extract-1240198114.648099-FTP_DATA-FHUsSu3rWdP07eRE4l 
extract-1240198114.648099-FTP_DATA-FHUsSu3rWdP07eRE4l: PE32 executable (GUI) Intel 80386, for MS Windows
```

将该文件上传到[virustotal](https://virustotal.com/)我们会发现匹配了一个[历史扫描报告](https://virustotal.com/en/file/b14ccb3786af7553f7c251623499a7fe67974dde69d3dffd65733871cddf6b6d/analysis/)，该报告表明这是一个已知的后门程序！

至此，基于这个发现就可以进行逆向倒推，寻找入侵线索了。

通过阅读```/usr/share/bro/base/files/extract/main.bro```的源代码

```bash
if ( ! args?$extract_filename )
        args$extract_filename = cat("extract-", f$last_active, "-", f$source,
                                    "-", f$id);

    f$info$extracted = args$extract_filename;
```

我们了解到该文件名的最右一个-右侧对应的字符串```FHUsSu3rWdP07eRE4l```是```files.log```中的文件唯一标识。

通过查看```files.log```，发现该文件提取自网络会话标识（bro根据IP五元组计算出的一个会话唯一性散列值）为```CP0WpmULcjBpkDTQf```的FTP会话。

该```CP0WpmULcjBpkDTQf```会话标识在```conn.log```中可以找到对应的IP五元组信息。

通过```conn.log```的会话标识匹配，我们发现该PE文件来自于IPv4地址为：```98.114.205.102```的主机。

### Bro的一些其他技巧

* ```ftp.log``` 中默认不会显示捕获的FTP登录口令，我们可以通过在 ```/etc/bro/site/mytuning.bro``` 中增加以下变量重定义来实现：

```bash
redef FTP::default_capture_password = T;
```

* SMB协议识别

Bro从2.5Beta版开始增加了对SMB协议的识别支持，根据SMB协议识别插件作者在2016年9月的一次[公开技术分享PPT](https://www.bro.org/brocon2016/slides/hall_smb.pdf)的描述我们可以了解到：自2014年起开始出行并快速流行起来的勒索软件威胁，人们重新开始审视企业内部的文件共享机制，SMB作为一种常见的局域网（文件、打印机和串口等）共享技术通信协议规范，Bro2.5Beta之前并没有提供SMB协议的开箱即用识别和还原能力。

本文写作之时，如果想体验Bro的SMB协议识别功能需要使用Bro官网git主干分支上的代码在本地自行编译。好在官网的源代码编译指南写的很详细清楚，我在完成上述实验笔记的环境中对照官网的编译指南成功的编译了Bro2.5Beta。

```bash
root@kali:~/Downloads# ls -l 2.4.1
total 240
-rw-r--r-- 1 root root 189103 Dec 21 09:04 attack-trace.pcap
-rw-r--r-- 1 root root   1194 Dec 21 10:05 conn.log
drwxr-xr-x 2 root root   4096 Dec 21 10:05 extract_files
-rw-r--r-- 1 root root    821 Dec 21 10:05 files.log
-rw-r--r-- 1 root root    849 Dec 21 10:05 ftp.log
-rw-r--r-- 1 root root    206 Dec 21 10:05 known_hosts.log
-rw-r--r-- 1 root root    275 Dec 21 10:05 known_services.log
-rw-r--r-- 1 root root  16505 Dec 21 10:05 loaded_scripts.log
-rw-r--r-- 1 root root    253 Dec 21 10:05 packet_filter.log
-rw-r--r-- 1 root root    565 Dec 21 10:05 pe.log
root@kali:~/Downloads# ls -l 2.5
total 260
-rw-r--r-- 1 root root 189103 Dec 20 21:15 attack-trace.pcap
-rw-r--r-- 1 root root    278 Dec 21 09:08 capture_loss.log
-rw-r--r-- 1 root root   1197 Dec 21 09:08 conn.log
-rw-r--r-- 1 root root    470 Dec 21 09:08 dpd.log
drwxr-xr-x 2 root root   4096 Dec 21 09:07 extract_files
-rw-r--r-- 1 root root    821 Dec 21 09:08 files.log
-rw-r--r-- 1 root root    849 Dec 21 09:08 ftp.log
-rw-r--r-- 1 root root    206 Dec 21 09:08 known_hosts.log
-rw-r--r-- 1 root root    276 Dec 21 09:08 known_services.log
-rw-r--r-- 1 root root  23552 Dec 21 09:08 loaded_scripts.log
-rw-r--r-- 1 root root    397 Dec 21 09:08 ntlm.log
-rw-r--r-- 1 root root    253 Dec 21 09:08 packet_filter.log
-rw-r--r-- 1 root root    565 Dec 21 09:08 pe.log
-rw-r--r-- 1 root root    705 Dec 21 09:08 stats.log
```

使用Bro 2.4.1和2.5Beta使用相同的检测规则（2.5Beta启用了```“@load protocols/smb```）的情况下生成的日志文件如上所示。

对比 ```known_services.log``` 可以看到2.5Beta可以很好的识别出SMB协议流量了。

```bash
root@kali:~/Downloads# cat 2.4.1/known_services.log
#separator \x09
#set_separator  ,
#empty_field    (empty)
#unset_field    -
#path   known_services
#open   2016-12-21-10-05-56
#fields ts  host    port_num    port_proto  service
#types  time    addr    port    enum    set[string]
1240198118.462473   192.150.11.111  445 tcp (empty)
#close  2016-12-21-10-05-56
root@kali:~/Downloads# cat 2.5/known_services.log
#separator \x09
#set_separator  ,
#empty_field    (empty)
#unset_field    -
#path   known_services
#open   2016-12-21-09-08-22
#fields ts  host    port_num    port_proto  service
#types  time    addr    port    enum    set[string]
1240198108.976883   192.150.11.111  445 tcp SMB,NTLM
#close  2016-12-21-09-08-22
```

* 使用正确的分隔符进行过滤显示的重要性

```bash
# 从头开始查看日志文件，显示前1行
head -n1 conn.log

# Bro的日志文件默认使用的分隔符显示为ASCII码\x09，通过以下命令可以查看该ASCII码对应的“可打印字符”
echo -n -e '\x09' | hexdump -c

# 使用awk打印给定日志文件的第N列数据
awk -F '\t' '{print $12}' conn.log 
```

* 查看Bro的超长行日志时的横向滚动技巧

```bash
less -S conn.log
```

* 使用bro-cut（在```bro-aux```软件包中）更“优雅”的查看日志中关注的数据列

```bash
# 查看conn.log中所有可用的“列名”
grep ^#fields conn.log | tr '\t' '\n'

# 按照“列名”输出conn.log中我们关注的一些“列”
bro-cut ts id.orig_h id.orig_p id.resp_h id_resp_p proto < conn.log

# 将UNIX时间戳格式转换成人类可读的时间（但该方法对于大日志文件处理性能非常低）
bro-cut -d < conn.log
```

## 参考文献

* [Frequently Asked Questions from Official Bro WebSite](https://www.bro.org/documentation/faq.html)
* [Bro官方推荐的一些辅助工具](https://www.bro.org/community/software.html)

