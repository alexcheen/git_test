# 什么是GIT
简单说，分布式版本管理系统

//好像高大上，又好像什么也没说

分布式-版本管理

## 1. 版本管理


## 2. 分布式


# GIT 存储模型




·  git add -A  提交所有变化

·  git add -u  提交被修改(modified)和被删除(deleted)文件，不包括新文件(new)

·  git add .  提交新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件

git object  blob/tree/commit


git checkout master
git checkout -f
git checkout -- .
git checkout -b new_branch
git checkout master -- file.txt


git reset --soft、git reset、git reset --hard


git reflog


git reset --hard HEAD 或 git checkout -f
git clean -df
git stash push [-u | --include-untracked]

$ git commit --amend
$ git rebase -i origin/master
$ git show-branch
$ git blame
$ git bisect