#!/usr/bin/python
# @Author: Chara
# @Description:
# @Time: 2020/2/28 16:07

import os

# rule = ['xls', 'xlsx']
rule = ['py']

# 获取当前路径
local = os.getcwd()

# 输出当前路径下符合过滤后缀名的文件
print([el for el in os.listdir(local) if el.split('.')[1] in rule])
