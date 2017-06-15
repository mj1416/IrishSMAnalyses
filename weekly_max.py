import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


filename = "~/Documents/MPECDT/MRes/Danica/Irish SM data/ControlDomesticDataComplete22Weeks.xlsx"
DATA=pd.read_excel(filename,sheetname=1,header=0,parse_cols="A:UA")
data=DATA.dropna(axis=1)


#extract weekly maxima

week_max = data.groupby("Week").max()

week_max[range(3,week_max.shape[1])].to_csv('weekly_max_22.csv')
