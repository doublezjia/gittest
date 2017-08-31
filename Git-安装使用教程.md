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
>删除关联用`git remote rm origin`
>如果要关联多个远程库的,把`origin`这里改成不同的名称就可以了

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

### 分支管理策略
合并分支时，加上`--no-ff`参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而`fast forward`合并就看不出来曾经做过合并。
>当使用`--no-ff`合并时要创建一个新的commit，所以要加上`-m`,然后写上commit的描述。
>如```git merge --no-ff -m "merge with no-ff" dev```

>可以通过`git log`查看分支历史

### 储藏当前还没提交的工作区内容

当在自己的分支中的修改还没有改好又不想提交时，又要急着处理bug时，可以通过`git stash`把当前工作现场储藏起来，然后切换到其他分支修复bug。完成后再切换回来，通过`git stash apply`进行恢复，然后继续工作。

`git stash` 保存当前工作现场
`git stash list` 查看保存的名称
`git stash apply <name>` 恢复当前工作现场
`git stash drop <name>` 删除stash保存的内容
`git stash pop <name>` 恢复的同时把stash保存的内容删掉

>这个可以应用在自己的内容还没修改好不想提交，又急着处理其他分支的事情时可以用到。
>当手头工作没有完成时，先把工作现场`git stash`一下，然后去修复bug，修复后，再`git stash pop`，回到工作现场。
>修复bug时，我们会通过创建新的bug分支进行修复，然后合并，最后删除

### 强制删除还没合并的分支
有时候当我们新建一个分支进行开发，最后发现不需要这个分支要把它删除时，因为这个分支不需要，所以不能合并到主分支上。要是直接运行`git branch -d <name>`发现不能删除，这是因为这个分支还没有合并的原因。这是可以使用`git branch -D <name>`强制删除。

### 多人协助
多人协作的工作模式通常是这样：

1. 首先，可以试图用`git push origin branch-name`推送自己的修改；
2. 如果推送失败，则因为远程分支比你的本地更新，需要先用`git pull`试图合并；
3. 如果合并有冲突，则解决冲突，并在本地提交；
4. 没有冲突或者解决掉冲突后，再用`git push origin branch-name`推送就能成功！

5. 如果`git pull`提示`no tracking information`，则说明本地分支和远程分支的链接关系没有创建，用命令~~~git branch --set-upstream branch-name origin/branch-name~~~。
`git branch --set-upstream-to=origin/<branch> <branch>`

这就是多人协作的工作模式，一旦熟悉了，就非常简单。


- 查看远程库信息，使用`git remote -v`；

- 本地新建的分支如果不推送到远程，对其他人就是不可见的；

- 从本地推送分支，使用`git push origin branch-name`，如果推送失败，先用`git pull`抓取远程的新提交；

- 在本地创建和远程分支对应的分支，使用`git checkout -b branch-name origin/branch-name`，本地和远程分支的名称最好一致；

- 建立本地分支和远程分支的关联，使用~~~git branch --set-upstream branch-name origin/branch-name~~~；
`git branch --set-upstream-to=origin/<branch> <branch>`
- 从远程抓取分支，使用`git pull`，如果有冲突，要先处理冲突。

- ` git push origin :<branch>` 可以删除远程分支

## 标签
为了更好的查找版本，所以需要打上一个TAG

### 创建标签

`git tag <tagname>`用于新建一个标签，默认为`HEAD`，也可以指定一个`commit id`,用`git tag <tagname> <commit id>`打上标签

`git tag -a <tagname> -m "blablabla..."`可以指定标签信息

`git tag -s <tagname> -m "blablabla..."`可以用PGP签名标签，签名采用PGP签名，因此，必须首先安装gpg（GnuPG），如果没有找到gpg，或者没有gpg密钥对，就会报错，用PGP签名的标签是不可伪造的，因为可以验证PGP签名。

`git tag`可以查看所有标签,顺序是按照字母排序的。
`git show <tagname>` 查看标签信息。

### 操作标签
- `git push origin <tagname>`可以推送一个本地标签；

- `git push origin --tags`可以推送全部未推送过的本地标签；

- `git tag -d <tagname>`可以删除一个本地标签；

- `git push origin :refs/tags/<tagname>`可以删除一个远程标签。
>要删除远程标签，要先删除本地标签

## 自定义Git

### 忽略特殊文件
有些不需要提交的文件可以通过新建一个`.gitignore`的文件，然后把不需要提交的文件名输入到`.gitignore`中，并把`.gitignore`提交了。这样就可以忽略不需要提交的文件了。
>如果要强制提交的，可以用`git add -f <name>`进行提交
>如果发现`.gitignore`写的有问题，可以通过`git check-ignore`进行检查。
>`.gitignore`文件本身要放到版本库里，并且可以对`.gitignore`做版本管理！

### 配置别名
`git config --global alias.<别名> <命令>`进行别名配置
如`git config --global alias.st status`就是把`status`设置成`st`

>配置Git的时候，加上`--global`是针对当前用户起作用的，如果不加，那只针对当前的仓库起作用。
>每个仓库的Git配置文件都放在`.git/config`文件中.
>当前用户的Git配置文件放在用户主目录下的一个隐藏文件`.gitconfig`中.
>可以打开配置文件，对里面的`[alias]`进行别名的添加、修改和删除。


