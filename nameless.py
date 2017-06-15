import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename1="~/Documents/MPECDT/MRes/Danica/Irish SM data/full_data.csv"
data = pd.read_csv(filename1)


data_mean = data.groupby("DayN").mean()
max_data_mean = data_mean[range(3,data_mean.shape[1])].max(axis=1)
t1 = max_data_mean[1:]
t0 = max_data_mean[:-1]
t0.index = t1.index
max_pos_diff_mean = t1-t0
max_pos_diff_mean[max_pos_diff_mean<0]=0

data_max = data.groupby("DayN").max()
max_data_max = data_max[range(3,data_max.shape[1])].max(axis=1)
t1 = max_data_max[1:]
t0 = max_data_max[:-1]
t0.index = t1.index
max_pos_diff_max = t1-t0
max_pos_diff_max[max_pos_diff_max<0]=0

data_sum = data.groupby("DayN").sum()
max_data_sum = data_sum[range(3,data_sum.shape[1])].max(axis=1)
t1 = max_data_sum[1:]
t0 = max_data_sum[:-1]
t0.index = t1.index
max_pos_diff_sum = t1-t0
max_pos_diff_sum[max_pos_diff_sum<0]=0

sum_data_sum = data_sum[range(3,data_sum.shape[1])].sum(axis=1)
t1 = sum_data_sum[1:]
t0 = sum_data_sum[:-1]
t0.index = t1.index
sum_pos_diff_sum = t1-t0
sum_pos_diff_sum[sum_pos_diff_sum<0]=0


pos_diff = pd.DataFrame()
pos_diff["Mm"] = max_pos_diff_mean
pos_diff["MM"] = max_pos_diff_max
pos_diff["MS"] = max_pos_diff_sum
pos_diff["SS"] = sum_pos_diff_sum
pos_diff.to_csv("22_pos_diff.csv")

t1 = data_max[1:]
t0 = data_max[:-1]
t0.index = t1.index

returns = abs(t1 - t0)/t0

returns = returns.drop(["Week","HH","Day"],axis=1)

returns.to_csv("max_returns_22.csv")
