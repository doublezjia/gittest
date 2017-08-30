# Git 安装和使用

参考[廖雪峰的Git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)


## Git安装
- linux
	以Ubuntu为例 运行 apt-get install git 进行安装,其他发行版同理.
- Mac os
	一是安装homebrew，然后通过homebrew安装Git，具体方法请参考homebrew的文档：[http://brew.sh/](http://brew.sh/)。

	第二种方法更简单，也是推荐的方法，就是直接从AppStore安装Xcode，Xcode集成了Git，不过默认没有安装，你需要运行Xcode，选择菜单“Xcode”->“Preferences”，在弹出窗口中找到“Downloads”，选择“Command Line Tools”，点“Install”就可以完成安装了。
- Windows
	从[https://git-for-windows.github.io](https://git-for-windows.github.io)下载，然后按默认选项安装即可。


安装完后，进行最后一步的设置，在命令行中运行一下命令：
```git	
git config --blobal user.name "用户名"
git config --global user.email "用户邮箱"
```


## Git使用
### 创建版本库
新建一个空的目录，然后进入目录执行命令`git init`初始化Git仓库
>注意：此时文件夹内会有一个`.git`的目录，这个目录是Git来跟踪管理版本库的，没事千万不要手动修改这个目录里面的文件，不然改乱了，就把Git仓库给破坏了。

### 把文件添加到版本库
第一步，用命令`git add <file> `把文件添加到仓库,这里可以一次添加多个文件
第二步，用命令`git commit`把文件提交到仓库

### 掌握仓库当前的状态
要随时掌握工作区的状态，使用`git status`命令。

如果git status告诉你有文件被修改过，用`git diff`可以查看修改内容。

>注意：如果文件修改过，记得要重新提交到版本库

### 版本回退
`git log`可以显示从最近到最远的提交日志，以便确定要回退到哪个版本。
>`commit 8692563b63ffdded98f0ed59ca9d2e5510d124ca`是`commit id` 
>用`HEAD`表示当前版本,上一个版本就是`HEAD^`，上上一个版本就是`HEAD^^`，当然往上100个版本写100个^比较容易数不过来，所以写成`HEAD~100`。

返回上一个版本用`git reset --hard HEAD^`

如果知道某个版本的`commit id`,也可以用`git reset --hard <commit id>`回到这个版本。
>这里的`commit id`可以不用写全，只写前面几位就可以的，Git会自动查找的。

`git reflog`可以查看历史命令，以便确定要回到未来的哪个版本。

### 工作区和暂存区 
- 工作区
	就是新建来存放文件的目录

- 版本库（Repository）
	工作区有一个隐藏目录`.git`，这个不算工作区，而是Git的版本库。
	Git的版本库里存了很多东西，其中最重要的就是称为`stage`（或者叫index）的**暂存区**，还有Git为我们自动创建的第一个分支`master`，以及指向master的一个指针叫`HEAD`。 

> 当提交到版本库时，一般会分两步执行：
> 第一步通过`git add`把文件添加到**暂存区**。
> 
> 第二步通过`git commit`把**暂存区**的所有文件提交到当前分支中。
> 
> 因为默认创建Git版本库时，创建了唯一的分支`master`,所以会从**暂存区**提交到`master`中。

### 撤销修改
当修改的文件还没运行`git add`命令把文件放到暂存区时，可以通过`git checkout -- <file>` 撤销会之前还没修改的版本。
>注意`git checkout -- <file>`中的`--`很重要，一定要有，要是没有`--`就会变成了切换到另一个分支的命令。

如果已经通过`git add`提交到暂存区且还没有运行`git commit`时，可以通过`git reset HEAD <file>`把暂存区的修改撤回，重新放回工作区。之后就可以用`git checkout -- <file>`进行撤销了。
>`git reset`命令既可以回退版本，也可以把暂存区的修改回退到工作区。当我们用`HEAD`时，表示最新的版本。

如果已经运行`git commit` 提交了，可以参照前面的`git reset --hard HEAD^`退回前面的版本，前提是没有推送到远程库中。

### 删除文件
如果不小心删除了本地文件，可以通过`git checkout -- <file>`进行恢复，`git checkout`可以从版本库中下载最新版本的文件。

如果不想要版本库中的某个文件，可以通过`git rm`进行删除，然后运行`git commit`，这样就可以把版本库中的文件删除。

## 远程仓库

### 创建ssh key
以Github为例
由于你的本地Git仓库和GitHub仓库之间的传输是通过SSH加密的，所以，需要一点设置：
第1步：创建`SSH Key`。在用户主目录下，看看有没有`.ssh`目录，如果有，再看看这个目录下有没有`id_rsa`和`id_rsa.pub`这两个文件，如果已经有了，可直接跳到下一步。如果没有，打开Shell（Windows下打开Git Bash），创建`SSH Key`：
```
ssh-keygen -t rsa -C "youremail@example.com"
```
>把邮件地址换成你自己的邮件地址，然后一路回车，使用默认值即可

第2步：登陆GitHub，打开`settings`，选择`ssh and gpg keys`页面,
然后点击`new ssh key`，填上任意Title，在Key文本框里粘贴`id_rsa.pub`文件的内容.

### 添加仓库并关联
登录Github，新建一个仓库。然后就可以把本地的仓库的关联到Github中的仓库，命令如下
```
#关联远程库
git remote add origin git@github.com:你的Github用户名/项目名称.git
```
>远程库的名称默认叫法为`origin`,命令在Github新建仓库中会有提示。

### 推送到远程库
推送到远程库用`git push`,把当前分支`master`推送到远程
>因为远程库是空的，所以第一次推送要加上`-u`,git在推送本地`master`的同时，会把本地的`master`和远程的`master`分支合并起来。

```
#第一次推送master分支
git push -u origin master

#每次提交到远程
git push origin master
```

### 从远程库克隆

可以通过 `git clone`加远程仓库地址，把远程库克隆到本地中。
git支持多种协议，包括https，但通过ssh支持的原生git协议速度最快。

>注意：第一次连接的时候ssh可能会有提示，输入yes就可以了。


## 分支管理

### 创建与合并分支
`git checkout -b 分支名`创建并切换到新的分支。
`git checkout`加上`-b`相当于
```
git branch 分支名
git checkout 分支名
```

`git branch`用来查看所有分支，当前分支前面会有一个`*`号的。
`git branch 分支名` 创建分支。
`git checkout 分支名`切换分支。
`git merge 分支名`合并指定分支到当前分支。
`git branch -d 分支名`删除分支。


### 解决冲突

当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。
Git用`<<<<<<<`，`=======`，`>>>>>>>`标记出不同分支的内容

用`git log --graph`命令可以看到分支合并图。

