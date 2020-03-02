#!/usr/bin/python
# @Author: Chara
# @Description:
# @Time: 2020/2/28 15:50
import os
import pandas as pd
from openpyxl import load_workbook as ld

# 过滤出 excel 文件
rule = ['xls', 'xlsx']

# 获取当前路径
local = os.getcwd()

# 获取当前路径下的 excel 文件列表
excelArr = [el for el in os.listdir(local) if el.split('.')[1] in rule]

# 通过文件名读入数据
wbArr = [ld(i) for i in excelArr]

