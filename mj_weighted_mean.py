import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename1="~/Documents/MPECDT/MRes/Danica/Irish SM data/full_data.csv"
data = pd.read_csv(filename1,index_col=0)


p1 = data[[0,1,2,3,4]]

d1 = p1.loc[p1["Day"]==2]
OBS = d1.loc[d1.Week == 22]["P1"]

d2 = p1.loc[p1["Day"]==1]
G1 = d2.loc[d2.Week==22]["P1"]


G2 = d1.loc[d1.Week == 21]["P1"]
G3 = d1.loc[d1.Week == 20]["P1"]
G4 = d1.loc[d1.Week == 19]["P1"]
G5 = d1.loc[d1.Week == 18]["P1"]
G6 = d1.loc[d1.Week == 17]["P1"]
G7 = d1.loc[d1.Week == 16]["P1"]
