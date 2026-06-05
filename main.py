"""
修改文件后,文件处于工作区,需要先到暂存区,再commit到仓库

红色：新文件，还没被 Git 跟踪
蓝色：已跟踪文件被修改了
绿色：已加入暂存区的新文件
黑色/白色：没有改动
灰色：被 .gitignore 忽略了

加入暂存区:git add .

提交暂存区到仓库:git commit -m "注释内容"

查看修改的状态:git status

查看提交日志:git log
配置.bashrc文件后:git-log

版本回退:git reset --hard commitID
查看已经删除的记录:git reflog

Git忽略列表:gitignore

-----------------------------------------分支-----------------------------------------
HEAD指向哪个分支名,当前就在哪个分支

查看分支:git branch

创建本地分支:git branck 分支名

切换分支(切换前需要先提交):git checkout 分支名
创建并切换:git checkoput -b 分支名

合并分支(在主线上合并):git merge 分支名称

删除分支
git branch -d 分支名称
git branch -D 分支名称 ---> 强制删除

解决冲突:
1.处理文件中冲突的地方
2.将解决完冲突的文件加入暂存区
3.提交到仓库
"""