import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename1="~/Documents/MPECDT/MRes/Danica/Irish SM data/full_data.csv"
data = pd.read_csv(filename1)#,index_col=0)

returns = abs(t1 - t0)/t0

returns = returns.drop(["Week","HH","Day"],axis=1)

returns.to_csv("max_returns_22.csv")
