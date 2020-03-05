#!/usr/bin/python
# @Author: Chara
# @Description:
# @Time: 2020/2/28 15:50
import os
import pandas as pd

# 过滤出 excel 文件
rule = ['xls', 'xlsx']

# 获取当前路径
local = os.getcwd()

# test-1
# local = os.path.join(os.getcwd(),'test-1')

# 输出路径
outUrl = os.path.join(local, "output.xlsx")

# 如果有之前合并完的输出文件，那就先删除
if os.path.exists(outUrl):
    os.remove(outUrl)

# 获取当前路径下的 excel 文件列表
excelArr = [os.path.join(local, el) for el in os.listdir(local) if el.split('.')[1] in rule]

if len(excelArr) == 0:
    print('无 excel 文件')
else:
    # 通过文件名读入数据
    # header 的值即为设置标题所在的行数，默认为 0
    wbArr = [pd.read_excel(i, header=1) for i in excelArr]
    writer = pd.ExcelWriter(outUrl)
    pd.concat(wbArr).to_excel(writer, 'Sheet1', index=False)
    writer.save()
