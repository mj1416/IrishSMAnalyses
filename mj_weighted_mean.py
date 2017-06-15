import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = "~/Documents/MPECDT/MRes/Danica/Irish SM data/16_22_weeks.xlsx"
DATA=pd.read_excel(filename,sheetname=1,header=0,parse_cols="A:UA")

#clean data
data=DATA.dropna(axis=1)


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
