import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


filename = "~/Documents/MPECDT/MRes/Danica/Irish SM data/16_22_weeks.xlsx"
DATA=pd.read_excel(filename,sheetname=1,header=0,parse_cols="A:UA")
data=DATA.dropna(axis=1)


data_max = data.groupby("DayN").max()
today = data_max[range(3,data_max.shape[1])][1:]
yesterday = data_max[range(3,data_max.shape[1])][:-1]
yesterday.index = today.index
ret = abs(today - yesterday)/yesterday
ret.to_csv("max_ret_6.csv")


day_mean = data.groupby("DayN").mean()
day_mean = day_mean.drop(["Week","HH","Day"],axis=1)
# mean_day_mean = day_mean.mean(axis=1)
# t1 = mean_day_mean[1:]
# t0 = mean_day_mean[:-1]
# t0.index = t1.index
# mean_pos_diff_mean = t1-t0
# mean_pos_diff_mean[mean_pos_diff_mean<0]=0

max_day_mean = day_mean.max(axis=1)
t1 = max_day_mean[1:]
t0 = max_day_mean[:-1]
t0.index = t1.index
max_pos_diff_mean = t1-t0
max_pos_diff_mean[max_pos_diff_mean<0]=0

day_max = data.groupby("DayN").max()
day_max = day_max.drop(["Week","HH","Day"],axis=1)
mean_day_max = day_max.mean(axis=1)
t1 = mean_day_max[1:]
t0 = mean_day_max[:-1]
t0.index = t1.index
mean_pos_diff_max = t1-t0
mean_pos_diff_max[mean_pos_diff_max<0]=0

max_day_max = day_max.max(axis=1)
t1 = max_day_max[1:]
t0 = max_day_max[:-1]
t0.index = t1.index
max_pos_diff_max = t1-t0
max_pos_diff_max[max_pos_diff_max<0]=0

day_sum = data.groupby("DayN").sum()
day_sum = day_sum.drop(["Week","HH","Day"],axis=1)
sum_day_sum = day_sum.sum(axis=1)
t1 = sum_day_sum[1:]
t0 = sum_day_sum[:-1]
t0.index = t1.index
sum_pos_diff_sum = t1-t0
sum_pos_diff_sum[sum_pos_diff_sum<0]=0

max_day_sum = day_sum.max(axis=1)
t1 = max_day_sum[1:]
t0 = max_day_sum[:-1]
t0.index = t1.index
max_pos_diff_sum = t1-t0
max_pos_diff_sum[max_pos_diff_sum<0]=0

#save image
f, axarr = plt.subplots(2, 2)
axarr[0, 0].plot(max_pos_diff_mean.index,max_pos_diff_mean,'r')
axarr[0, 0].set_title('Max of Mean')
axarr[0, 1].plot(max_pos_diff_max.index,max_pos_diff_max,'g')
axarr[0, 1].set_title('Max of Max')
axarr[1, 0].plot(max_pos_diff_sum.index, max_pos_diff_sum,'c')
axarr[1, 0].set_title('Max of Total')
axarr[1, 0].set_xlabel("Day")
axarr[1, 1].plot(sum_pos_diff_sum.index, sum_pos_diff_sum,'m')
axarr[1, 1].set_title('Total of Total')
axarr[1, 1].set_xlabel("Day")
plt.tight_layout()
plt.savefig('pos_diffs.pdf')
plt.close()

#save as an excel file
pos_diff = pd.DataFrame()
#pos_diff["mm"] = mean_pos_diff_mean
pos_diff["Mm"] = max_pos_diff_mean
#pos_diff["mM"] = mean_pos_diff_max
pos_diff["MM"] = max_pos_diff_max
pos_diff["mS"] = mean_pos_diff_sum
pos_diff["MS"] = max_pos_diff_sum
pos_diff["SS"] = sum_pos_diff_sum
pos_diff.to_csv("pos_diff.csv")
