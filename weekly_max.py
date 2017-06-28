import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


filename1="~/Documents/MPECDT/MRes/Danica/Irish SM data/short_data.csv"
data = pd.read_csv(filename1,index_col=0)

#extract weekly maxima

week_max = data.groupby("Week").max()

week_max[range(3,week_max.shape[1])].to_csv('weekly_max_22.csv')
