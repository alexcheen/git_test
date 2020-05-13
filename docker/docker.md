<!--
 * @Author: your name
 * @Date: 2020-05-13 14:04:17
 * @LastEditTime: 2020-05-13 18:23:42
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \undefinedd:\git\git_test\docker\docker.md
 -->
#docker


## command

|子命令分类|子命令|
|-|-|
|Docker环境信息| info、version|
|容器生命周期管理| create、exec、kill、pause、restart、rm、run、start、stop、unpause|
|镜像仓库命令|login、logout、pull、push、search|
|镜像管理| build、images、import、load、rmi、save、tag、commit|
|容器运维操作|attach、export、inspect、port、ps、rename、stats、top、wait、cp、diff、update|
|容器资源管理|volume、network|
|系统日志信息|events、history、logs|

[原文地址](http://www.sel.zju.edu.cn/?p=573)
## Overall
1. Docker本质时宿主机的一个进程
2. 通过namespace实现资源隔离 
3. cgroups实现资源限制
4. UnionFs实现Copy on Write的文件操作
   
###  CGroups (Control Groups)

