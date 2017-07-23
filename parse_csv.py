# -*- coding: utf-8 -*-
import pandas as pd
filename = 'first.csv'
encoding = "GB2312"
col_name = "A项数量"
f_csv = pd.read_csv(filename, encoding=encoding,usecols=[col_name])
max = 0
total = 0
size = 0
error_size = 0
for i in f_csv[col_name]:
    size = size + 1
    num = int(i)
    total = total + num
    if max < num:
        max = num
    if num <= 0:
        error_size = error_size + 1

print("max", max, "total",total, "size",size, "error_size", error_size)