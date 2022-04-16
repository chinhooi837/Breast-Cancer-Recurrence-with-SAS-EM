# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 21:27:18 2022

@author: chinh
"""

import numpy as np
import pandas as pd

df = pd.read_csv("breast-cancer2.csv")
df[['age_min', 'age_max']] = df['age'].str.split('-', expand=True)
df[['tumor-size_min', 'tumor-size_max']] = df['tumor-size'].str.split('-', expand=True)
df[['inv-nodes_min', 'inv-nodes_max']] = df['inv-nodes'].str.split('-', expand=True)

df=df.drop(['age','tumor-size','inv-nodes'],axis=1)
df.to_csv("breast-cancer_processed.csv")