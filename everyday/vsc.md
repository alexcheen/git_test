# vs code 插件的离线安装
现在微软插件库下载所需插件：
```url
https://marketplace.visualstudio.com/vscode
```
然后在使用安装目录下的code工具进行安装：
```cmd
($installdir)\bin\code --install-extension extension-name.vsix
```
# remote-ssh
在安装好remote-ssh插件后，ssh连接服务器，这是由于内网服务器是没有外网连接，所以在服务器该目录下
"~/.vscode-server/bin/$(commit-id)"的该目录，并赋值commit-id到以下网址中
```url
2aae1f26c72891c399f860409176fe435a154b13
https://update.code.visualstudio.com/commit:$COMMIT_ID/server-linux-x64/insider
https://update.code.visualstudio.com/commit:2aae1f26c72891c399f860409176fe435a154b13/server-linux-x64/vscode-server
https://update.code.visualstudio.com/commit:2aae1f26c72891c399f860409176fe435a154b13/server-linux-x64/stable
```
下载后把该压缩包中的文件解压到当前目录中，重点是文件。
```shell
tar -xf vscode-server.tar.gz
mv vscode-server/* ./ 
touch 0
```
这是在客户机上重新打开vscode即可连接，连接过程需要多次输入密码。
