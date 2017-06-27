import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


filename1="~/Documents/MPECDT/MRes/Danica/Irish SM data/full_data.csv"
data = pd.read_csv(filename1)
#
# #data = data.drop("P357",1) #removing the one extreme outlier
#
past = data[data.Week!=22]
obs = data[data.Week==22]

from forecasts import *
LW = myLW(past)
SD = mySD(past)
LR = myRegWeek(data)
BR = myWeekRidge(data)


plt.subplot(7,1,1)
plt.plot(LW[LW.Day==1].HH,LW[LW.Day==1].P3,'g', label='LW')
plt.plot(SD[SD.Day==1].HH,SD[SD.Day==1].P3,'m', label='SD')
plt.plot(LR[LR.Day==1].HH,LR[LR.Day==1].P3,'r', label='LR')
plt.plot(BR[BR.Day==1].HH,BR[BR.Day==1].P3,'b', label='BR')
#plt.plot(BR_2[BR_2.Day==1].HH,BR_2[BR_2.Day==1].P3,'r', label='Ridge (2 weeks)')
plt.plot(obs[obs.Day==1].HH,obs[obs.Day==1].P3,'orange', label='Obs')
plt.ylabel('Mon')
plt.xticks([],[])
plt.legend(bbox_to_anchor=(1,1))

plt.subplot(7,1,2)

plt.plot(LW[LW.Day==2].HH,LW[LW.Day==2].P3,'g', label='LW')
plt.plot(SD[SD.Day==2].HH,SD[SD.Day==2].P3,'m', label='SD')
plt.plot(LR[LR.Day==2].HH,LR[LR.Day==2].P3,'r', label='LR')
plt.plot(BR[BR.Day==2].HH,BR[BR.Day==2].P3,'b', label='BR')
#plt.plot(BR_2[BR_2.Day==1].HH,BR_2[BR_2.Day==1].P3,'r', label='Ridge (2 weeks)')
plt.plot(obs[obs.Day==2].HH,obs[obs.Day==2].P3,'orange', label='Observations')
plt.ylabel('Tue')
plt.xticks([],[])

plt.subplot(7,1,3)

plt.plot(LW[LW.Day==3].HH,LW[LW.Day==3].P3,'g', label='LW')
plt.plot(SD[SD.Day==3].HH,SD[SD.Day==3].P3,'m', label='SD')
plt.plot(LR[LR.Day==3].HH,LR[LR.Day==3].P3,'r', label='LR')
plt.plot(BR[BR.Day==3].HH,BR[BR.Day==3].P3,'b', label='BR')
#plt.plot(BR_2[BR_2.Day==1].HH,BR_2[BR_2.Day==1].P3,'r', label='Ridge (2 weeks)')
plt.plot(obs[obs.Day==3].HH,obs[obs.Day==3].P3,'orange', label='Observations')
plt.ylabel('Wed')
plt.xticks([],[])

plt.subplot(7,1,4)
plt.plot(LW[LW.Day==4].HH,LW[LW.Day==4].P3,'g', label='LW')
plt.plot(SD[SD.Day==4].HH,SD[SD.Day==4].P3,'m', label='SD')
plt.plot(LR[LR.Day==4].HH,LR[LR.Day==4].P3,'r', label='LR')
plt.plot(BR[BR.Day==4].HH,BR[BR.Day==4].P3,'b', label='BR')
#plt.plot(BR_2[BR_2.Day==1].HH,BR_2[BR_2.Day==1].P3,'r', label='Ridge (2 weeks)')
plt.plot(obs[obs.Day==4].HH,obs[obs.Day==4].P3,'orange', label='Observations')
plt.ylabel('Thur')
plt.xticks([],[])

plt.subplot(7,1,5)
plt.plot(LW[LW.Day==5].HH,LW[LW.Day==5].P3,'g', label='LW')
plt.plot(SD[SD.Day==5].HH,SD[SD.Day==5].P3,'m', label='SD')
plt.plot(LR[LR.Day==5].HH,LR[LR.Day==5].P3,'r', label='LR')
plt.plot(BR[BR.Day==5].HH,BR[BR.Day==5].P3,'b', label='BR')
#plt.plot(BR_2[BR_2.Day==1].HH,BR_2[BR_2.Day==1].P3,'r', label='Ridge (2 weeks)')
plt.plot(obs[obs.Day==5].HH,obs[obs.Day==5].P3,'orange', label='Observations')
plt.ylabel('Fri')
plt.xticks([],[])

plt.subplot(7,1,6)
plt.plot(LW[LW.Day==6].HH,LW[LW.Day==6].P3,'g', label='LW')
plt.plot(SD[SD.Day==6].HH,SD[SD.Day==6].P3,'m', label='SD')
plt.plot(LR[LR.Day==6].HH,LR[LR.Day==6].P3,'r', label='LR')
plt.plot(BR[BR.Day==6].HH,BR[BR.Day==6].P3,'b', label='BR')
#plt.plot(BR_2[BR_2.Day==1].HH,BR_2[BR_2.Day==1].P3,'r', label='Ridge (2 weeks)')
plt.plot(obs[obs.Day==6].HH,obs[obs.Day==6].P3,'orange', label='Observations')
plt.ylabel('Sat')
plt.xticks([],[])

plt.subplot(7,1,7)
l1 = plt.plot(LW[LW.Day==7].HH,LW[LW.Day==7].P3,'g', label='LW')
l2 = plt.plot(SD[SD.Day==7].HH,SD[SD.Day==7].P3,'m', label='SD')
l3 = plt.plot(LR[LR.Day==7].HH,LR[LR.Day==7].P3,'r', label='LR')
l4 = plt.plot(BR[BR.Day==7].HH,BR[BR.Day==7].P3,'b', label='BR')
#plt.plot(BR_2[BR_2.Day==1].HH,BR_2[BR_2.Day==1].P3,'r', label='Ridge (2 weeks)')
l5 = plt.plot(obs[obs.Day==7].HH,obs[obs.Day==7].P3,'orange', label='Observations')
plt.ylabel('Sun')
plt.xticks([1,7,13,19,25,31,37,43,48],['00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00','23:30'])

#plt.figlegend((l1,l2,l3,l4,l5),("LW","SD","LR","BR","Observations"),loc="best")
plt.show()
