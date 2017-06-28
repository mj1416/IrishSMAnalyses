import numpy as np
import pandas as pd

from forecasts import *
#
data=pd.read_csv("short_data.csv",index_col=0)
past = data[data.Week!=22]
#
obs = data[data.Week==22]
SD = mySD(past)
LR = myRegWeek(data)
AA = pd.read_csv("AA_forecast.csv",index_col=0)
#
# from errors import myErrorP
# AA_err = myErrorP(AA,obs,4)
# SD_err = myErrorP(SD,obs,4)
# LR_err = myErrorP(LR,obs,4)
#
AA_err = abs(AA-obs)#.drop(["Week","DayN","HH","Day"],1)
SD_err = abs(SD-obs)#.drop(["Week","DayN","HH","Day"],1)
LR_err = abs(LR-obs)#.drop(["Week","DayN","HH","Day"],1)

AA_err.to_csv("AA_err.csv")
SD_err.to_csv("SD_err.csv")
LR_err.to_csv("LR_err.csv")
