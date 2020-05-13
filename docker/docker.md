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


## 部署Docker集群

### 下载
```shell
sudo docker pull ubuntu
sudo docker pull django
sudo docker pull haproxy
sudo docker pull redis
```
### 应用栈容器节点互联
使用(--link)建立容器间的连接是，Docker将自动维护映射关系中的IP地址。**host文件**。

### 应用栈容器节点启动
```shell
# 启动Redis容器
sudo docker run -it --name redis-master redis /bin/bash
sudo docker run -it --name redis-slave1 --link redis-master:master redis /bin/bash
sudo docker run -it --name redis-slave2 --link redis-master:master redis /bin/bash

# 启动Django容器
sudo docker run -it --name APP1 --link redis-master:db -v ~/Projects/Djago/App1:/usr/src/app django /bin/bash
sudo docker run -it --name APP2 --link redis-master:db -v ~/Projects/Djago/App2:/usr/src/app django /bin/bash

# 启动HAProxy容器
sudo docker run -it --name HAProxy --link APP1:APP1 --link APP2:APP2 -p 6301:6301 -v ~/Projects/HAProxy:/tmp haproxy /bin/bash
```

### 应用栈容器配置

```shell
sudo docker inspect --format "{{.Volumes}}" ContainerID
```

[原文地址](http://www.sel.zju.edu.cn/?p=573)
## Overall
1. Docker本质是宿主机的一个进程
2. 通过namespace实现资源隔离 
3. cgroups实现资源限制
4. UnionFs实现Copy on Write的文件操作
   
###  CGroups (Control Groups)

