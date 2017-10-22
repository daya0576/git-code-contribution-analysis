# Git Repo代码贡献量分析的小脚本


### 声明:
此项目只用来分析项目**代码**贡献量, 而不是项目贡献量.

### Demo:
![loading](http://opetwnn9x.bkt.clouddn.com/git_contribution/Jietu20171022-210926.jpg)

###  Features:

1. 快 (2500个commits的项目用时, 用时1.1s, 和gitinspector相比快了20倍.) 
2. 统计一个用户所有的commits, insertion, deletion, 改动总比重.
3. 合并多个用户(不同用户名)到一个用户名.
4. 支持按列排序.

###  Installation 

1. **安装python依赖:**   
```
git clone git@github.com:daya0576/git-code-contribution-analysis.git; cd git-code-contribution-analysis
pip3 install -r requirements.txt 
```
2. **配置:**   
在`env.py`中配置 待分析的git项目路径
```
python3 main.py
```

### TODO

1. 导出其他格式: html, cvs, excel, json
2. 多个repo, 合并分析
3. 兼容Python2
4. **其他指标, 算法, 更好地分析项目贡献, 而不仅仅是代码量的贡献.** 
5. 程序的进度条
6. 将配置(env.py)

---
(割)
---

# A Script for **Code Contribution** Analysis   

###  Installation
`tested in python3.6`
``` sh
pip install -r requirements.txt 
```

###  Usage

1. config repo path, [order column, ] in `env.py `
2. `python `

