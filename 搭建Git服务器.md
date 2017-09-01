## 搭建Git服务器
>环境：centos 6.8


1. 安装`git`
```
 yum install git -y
```
2. 创建`git`用户
```
useradd git
```
3. 收集所有需要登录到git服务器的用户的公钥，把所有公钥导入到`/home/git/.ssh/authorized_keys`文件里，一行一个。
>这里要注意把目录和文件夹的拥有者改为git
>出于安全考虑，还把目录权限改为700，文件名称改为600
	
	
	把etc/ssh/sshd_conf中的这三个注释去掉
	RSAAuthentication yes
	PubkeyAuthentication yes
	AuthorizedKeysFile      .ssh/authorized_keys
	

4. 初始化Git仓库
选定一个目录作为Git仓库，假如仓库是`/home/gitrepo/test.git`,进入`/home/gitrepo/`目录运行以下命令：
```
git init --bare test.git 
```
>初始化Git仓库一定要加上`--bare`,因为默认git是拒绝push操作的，如果不加上，客户端会提交不了到服务器中。

Git就会创建一个裸仓库，裸仓库没有工作区，因为服务器上的Git仓库纯粹是为了共享，所以不让用户直接登录到服务器上去改工作区，并且服务器上的Git仓库通常都以.git结尾。然后，把`owner`改为`git`
```
chown -R git:git test.git
```
>注意文件夹拥有者权限

5. 禁用git的shell登录
出于安全考虑，第二步创建的git用户不允许登录shell，这可以通过编辑`/etc/passwd`文件完成。
```
git:x:503:507::/home/git:/bin/bash
```
改为
```
git:x:503:507::/home/git:/usr/bin/git-shell
```

6. 克隆远程仓库
 通过`git clone`命令克隆远程仓库了，在各自的电脑上运行
```
git clone git@192.168.106.142:/home/gitrepo/test.git
```
>这里的ip改为服务的ip

这样Git服务器就完成了，之后只要把本地的分支推送到服务器就可以了。