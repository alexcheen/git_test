#docker

[原文地址](http://www.sel.zju.edu.cn/?p=573)
## Overall
1. Docker本质时宿主机的一个进程
2. 通过namespace实现资源隔离 
3. cgroups实现资源限制
4. UnionFs实现Copy on Write的文件操作
   
###  CGroups (Control Groups)

