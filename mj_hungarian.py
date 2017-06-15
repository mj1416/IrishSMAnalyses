import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from munkres import Munkres

def mj_AA(data,C=1,d=1):

    #test for one person
    p1 = data[[0,1,2,3,C+3]]
    cust = C
    P = str(data.columns[C+3])
    #pick a day of the week
    d1 = p1.loc[p1["Day"]==d]


    #set up past observations
    G1 = d1.loc[d1.Week == 21][P]
    G2 = d1.loc[d1.Week == 20][P]
    G3 = d1.loc[d1.Week == 19][P]
    G4 = d1.loc[d1.Week == 18][P]
    G5 = d1.loc[d1.Week == 17][P]
    G6 = d1.loc[d1.Week == 16][P]

    G= np.zeros((48,6))
    G[:,0]=G1
    G[:,1]=G2
    G[:,2]=G3
    G[:,3]=G4
    G[:,4]=G5
    G[:,5]=G6
    M,N = G.shape

    GG = np.zeros((M,N))

    #initialise baseline
    F = np.zeros((M,N+1))
    for i in range(M):
        F[i,0] = np.median((G[i,0],G[i,1],G[i,2],G[i,3],G[i,4],G[i,5]))


    #apply appendix A algorithm from Danica 2014 paper
    for k in range(N):
        matrix = np.ones((M,M))
        for i in range(M):
            if i ==0:
                matrix[i,:3] = abs(G[:3,k]-F[i,k])
            elif i == 1:
                matrix[i,:4] = abs(G[:4,k]-F[i,k])
            elif i == 46:
                matrix[i,i-2:] = abs(G[i-2:,k] - F[i,k])
            elif i == 47:
                matrix[i,i-2:] = abs(G[i-2:,k]-F[i,k])
            else:
                matrix[i,i-2:i+3] = abs(G[i-2:i+3,k]-F[i,k])
        m = Munkres()
        indexes = m.compute(matrix)
        np.set_printoptions(precision=3)
        for i in range(M):
            GG[i,k] = G[indexes[i][1],k]
        F[:,k+1] = (1.0/(k+1))*(GG[:,k] + k*F[:,k])
        #F[:,k+1] = (1.0/2)*(GG[:,k] + F[:,k])

    #adjusted average forecast
    AA = F[:,6]

    #normal mean forecast
    MEAN = np.mean(G,axis=1)
    #actual observation
    ACT = d1.loc[d1.Week == 22][P]
    OBS = np.array(ACT)

    return OBS, MEAN, AA, d, cust

# def main():
#     filename = "~/Documents/MPECDT/MRes/Danica/Irish SM data/16_22_weeks.xlsx"
#     DATA=pd.read_excel(filename,sheetname=1,header=0,parse_cols="A:UA")
#
#     #clean data
#     data=DATA.dropna(axis=1)
#
#     OBS,MEAN,AA, d, cust = mj_AA(data)
#     plt.figure()
#     plt.plot(OBS,'-k', label="Observations")
#     plt.plot(MEAN, '--k', label= "mean")
#     plt.plot(AA,'--b', label= "Adjusted Average")
#     plt.xlabel('Half hours')
#     plt.ylabel('Energy demand (kWh)')
#     plt.title('Forecasting techniques on day %s of Customer %s' %(d,cust))
#     plt.legend()
#     plt.show()
#
#
# main()
