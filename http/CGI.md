# CGI
CGI 即 Common Gateway Interface，译作“通用网关接口”。

## common
通用，理论上所有支持标准输出，支持获取环境变量的编程语言都可以用来编写CGI程序。
## Gateway
不同于网络通信中的网关，此处的网关是指不同协议之间的翻译转换。HTTP/FTP就是通过http转换为FTP来获取资源信息。即乙方时HTTP协议，另一方时其它协议，如组织内部的自定义协议。
CGI程序通常部署到Web服务器(like Apache)上，Web服务器调用CGI程序。
## Interface
当Web服务器在接受到用户浏览器的HTTP请求，时，Web服务器调用对应的CGI之前，会把各类HTTP请求中的信息以环境变量的方式写入OS。CGI程序本质是OS上的一个普通的可执行程序，它通过语言本身库函数来获取环境变量，从而获得数据输入。
此外CGI程序获取数据的方式也可以是标准输入STDIN。如POST请求一个CGI的URL，那么POST的数据通过标准输入传递给CGI。
CGI通过处理信息，将结果写入到标准输出即可。Web服务器已经做了重定向，将标准输出定向给Web服务器的与浏览器连接的socket。

## FastCGI
FCGI采用常驻内存的进程池技术，有调度器负责将传递过来的CGI请求发送给处理CGI的handler进程来处理。
