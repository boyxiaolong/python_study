# -*- coding: utf-8 -*-
import pandas as pd

filename = 'first.csv'
encoding = "GB2312"
col_name = "A项数量"
f_csv = pd.read_csv(filename, encoding=encoding,usecols=[col_name])
for i in f_csv[col_name]:
    num = int(i)
    if num < 0:
        print("error")