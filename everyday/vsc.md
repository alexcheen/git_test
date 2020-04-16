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
