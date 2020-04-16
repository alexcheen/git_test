# vs code 安装
略
# vs code 插件的离线安装
现在微软插件库下载所需插件：
```url
https://marketplace.visualstudio.com/vscode
```
然后在使用安装目录下的code工具进行安装：
```cmd
($installdir)\bin\code --install-extension extension-name.vsix
```
或在EXTENSION选项卡中，点击"More Action"(选项卡右上角三个点的图标)，"install from VSIX..."， 选择插件文件安装。

# remote-ssh
1. 如上步骤安装romote-ssh插件。
2. 在安装好remote-ssh插件后，一定要设置"remote.SSH.showLoginTerminal": true;
3. 使用rmote-ssh建立连接 username@ip，连接服务器，选择linux，并输入若干次密码;
4. 以上步骤后会报错，这是由于内网服务器是没有外网连接，内网服务器无法安装vscode-server;
这是在服务器该目录下有一个目录
"~/.vscode-server/bin/$(commit-id)"的该目录，并赋值commit-id到以下网址中
```url
https://update.code.visualstudio.com/commit:$COMMIT_ID/server-linux-x64/stable
```
如果commit-id="2aae1f26c72891c399f860409176fe435a154b13",就可以直接使用服务器上已经下好的文件直接使用。
5. 下载后把该压缩包中的文件解压到当前目录中，重点是文件。
```shell
tar -xf vscode-server.tar.gz
mv vscode-server/* ./ 
touch 0
```
6. 这是在客户机上重新打开vscode即可连接，连接过程需要多次输入密码。

# 服务器上安装插件
命令行模式暂时无法使用，只能通过在EXTENSION选项卡中安装。

# 免密登录
由于使用密码会出现反复输入密码，很麻烦。
```shell
cat id_rsa.pub >> authorized_key
```
以避免反复输入密码的麻烦。


# 脚本配置

```json
{
    "version": "2.0.0",
    //每次执行都启动一个新的控制台
    "presentation": {
        "reveal": "always",
        "panel": "new",
        "echo": true
    },
    //设置环境变量
    "options": {
        "env": {
            "LINUX_SRC_HOME": "/home/user/system/packages/services/Car/evs",
            "LOCAL_SRC_HOME": "${workspaceRoot}"
        }
    },
    "type": "shell",
    "problemMatcher": {
        "owner": "vs_code",
        "fileLocation": [
            "relative",
            "${workspaceRoot}"
        ],
        "pattern": {
            "regexp": ".*(app/.*|project/.*):(\\d+):(\\d+):\\s+(warning|error):\\s+(.*)$",
            "file": 1,
            "line": 2,
            "column": 3,
            "severity": 4,
            "message": 5
        }
    },
    //任务列表
    "tasks": [
        {
            "label": "01.[同步代码]本地代码->Linux远程服务器",
            "command": "${workspaceRoot}\\.vscode\\sync_code.cmd",
            "args": [
                "native",
                "False"
            ],
            "identifier": "CodeSync",
            "taskClassify": "同步代码"
        },
		
        {
            "label": "02.[同步代码并获取修改文件列表]本地代码-->Linux远程服务器",
            "command": "${workspaceRoot}\\.vscode\\sync_code.cmd",
            "args": [
                "native",
                "True"
            ],
            "identifier": "CodeSyncDiff",
            "taskClassify": "同步代码"
        },	
		
        {
            "label": "03.[编译IT]在Linux远程服务器上编译IT工程",
            "dependsOn": "CodeSync",
            "command": "${workspaceRoot}\\.vscode\\build_obj.cmd",
            "args": [
                "test",
                "DTCenter.out",
                "it_cfg",
                "Debug",
                "-j8",
                "cache"
            ],
            "taskClassify": "编译IT工程"
        },
        {
            "label": "04.[同步+编译+IT]在Linux远程服务器上构建IT工程并运行",
            "dependsOn": "CodeSync",
            "command": "${workspaceRoot}\\.vscode\\build_and_run_IT.cmd ratmng.nrom.cfgslave",
            "taskClassify": "同步+编译+IT工程"
        },     
        {
            "label": "05.[静态检查]代码静态检查",
            "dependsOn": "CodeSyncDiff",
            "command": "${workspaceRoot}\\.vscode\\inc_build_flint.cmd",
            "taskClassify": "flint"
        },
        {
            "label": "06.[增量构建] 代码增量compile",
            "dependsOn": "CodeSyncDiff",
            "command": "${workspaceRoot}\\.vscode\\inc_build_compile.cmd",
            "taskClassify": "增量编译"
        }
    ]

```
