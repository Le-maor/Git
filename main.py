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
"""