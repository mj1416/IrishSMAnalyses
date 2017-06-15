import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from munkres import Munkres

def mj_AA(data,C,d):

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
#
    GG = np.zeros((M,N))

    #initialise baseline
    F = np.zeros((M,N+1))
    BigM=np.max(G)
    BigM=14
    for i in range(M):
        F[i,0] = np.median((G[i,0],G[i,1],G[i,2],G[i,3],G[i,4],G[i,5]))


    #apply appendix A algorithm from Danica 2014 paper
    for k in range(N):
        matrix = BigM*np.ones((M,M))
        for i in range(M):
            if i ==0:
                matrix[i,:4] = abs(G[:4,k]-F[i,k])
            elif i == 1:
                matrix[i,:5] = abs(G[:5,k]-F[i,k])
            elif i == 2:
                matrix[i,:6] = abs(G[:6, k] - F[i, k])
            elif i == 45:
                matrix[i, i-3:] = abs(G[i-3:, k] - F[i, k])
            elif i == 46:
                matrix[i,i-3:] = abs(G[i-3:,k] - F[i,k])
            elif i == 47:
                matrix[i,i-3:] =abs(G[i-3:,k]-F[i,k])
            else:
                matrix[i,i-3:i+4] = abs(G[i-3:i+4,k]-F[i,k])

        m = Munkres()
        np.set_printoptions(precision=4)
        #matrixa=matrix.copy()
        indexes = m.compute(matrix)

#        plt.figure()
#        plt.plot(np.array(G[:, k]),'-b', label="Gk")
#        plt.plot(np.array(F[:, k]),'-r', label="Fk")
#
#        plt.xlabel('Half hours')
#        plt.ylabel('Energy demand (kWh)')
#        plt.title('Weakly observations of Customer %s' %(cust))
#        plt.legend()
#        plt.show()


#        total=0
##
#
#        for row, column in indexes:
#             total +=  matrix[row, column]
##
##            #print('(%d, %d) -> %d' % (row, column,matrix[row, column] ))
#        print('total cost: %d' % total)

        for i in range(M):
            GG[i,k] = G[indexes[i][1],k]
        F[:,k+1] = (1.0/(k+1))*(GG[:,k] + k*F[:,k])

    #adjusted average forecast
    AA = F[:,6]

    #normal mean forecast
    MEAN = np.mean(G,axis=1)
    #actual observation
    ACT = d1.loc[d1.Week == 22][P]
    OBS = np.array(ACT)

    return OBS, MEAN, AA, d, cust

def mj_AA_plot():
    filename = 'short_data.csv'
    data=pd.read_csv(filename,index_col=0)
    #OBS,MEAN,AA, d, cust = mj_AA(data, C=1, d=5)
    OBS1,MEAN1,AA1, d1, cust1 = mj_AA(data, C=1, d=1)
    OBS2,MEAN2,AA2, d2, cust1 = mj_AA(data, C=1, d=2)
    OBS3,MEAN3,AA3, d3, cust1 = mj_AA(data, C=1, d=3)
    OBS4,MEAN4,AA4, d4, cust1 = mj_AA(data, C=1, d=4)
    OBS5,MEAN5,AA5, d5, cust1 = mj_AA(data, C=1, d=5)
    OBS6,MEAN6,AA6, d6, cust1 = mj_AA(data, C=1, d=6)
    OBS7,MEAN7,AA7, d7, cust1 = mj_AA(data, C=1, d=7)


    plt.subplot(7,1,1)
    plt.plot(OBS1,'-k', label="Observations")
    plt.plot(MEAN1, '--k', label= "SD")
    plt.plot(AA1,'--b', label= "Adjusted Average")
    plt.ylabel('Mon')
    plt.xticks([],[])
    #plt.legend()#bbox_to_anchor=(1,1))

    plt.subplot(7,1,2)
    plt.plot(OBS2,'-k', label="Observations")
    plt.plot(MEAN2, '--k', label= "SD")
    plt.plot(AA2,'--b', label= "Adjusted Average")
    plt.ylabel('Tue')
    plt.xticks([],[])

    plt.subplot(7,1,3)
    plt.plot(OBS3,'-k', label="Observations")
    plt.plot(MEAN3, '--k', label= "SD")
    plt.plot(AA3,'--b', label= "Adjusted Average")
    plt.ylabel('Wed')
    plt.xticks([],[])

    plt.subplot(7,1,4)
    plt.plot(OBS4,'-k', label="Observations")
    plt.plot(MEAN4, '--k', label= "SD")
    plt.plot(AA4,'--b', label= "Adjusted Average")
    plt.ylabel('Thur')
    plt.xticks([],[])

    plt.subplot(7,1,5)
    plt.plot(OBS5,'-k', label="Observations")
    plt.plot(MEAN5, '--k', label= "SD")
    plt.plot(AA5,'--b', label= "Adjusted Average")
    plt.ylabel('Fri')
    plt.xticks([],[])

    plt.subplot(7,1,6)
    plt.plot(OBS6,'-k', label="Observations")
    plt.plot(MEAN6, '--k', label= "SD")
    plt.plot(AA6,'--b', label= "Adjusted Average")
    plt.ylabel('Sat')
    plt.xticks([],[])

    plt.subplot(7,1,7)
    plt.plot(OBS7,'-k', label="Observations")
    plt.plot(MEAN7, '--k', label= "SD")
    plt.plot(AA7,'--b', label= "Adjusted Average")
    plt.ylabel('Sun')
    plt.xticks([1,7,13,19,25,31,37,43,48],['00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00','23:30'])

    # plt.figure()
    # plt.plot(OBS,'-k', label="Observations")
    # plt.plot(MEAN, '--k', label= "mean")
    # plt.plot(AA,'--b', label= "Adjusted Average")
    # plt.xlabel('Half hours')
    # plt.ylabel('Energy demand (kWh)')
    # plt.title('Forecasting techniques on day %s of Customer %s' %(d,cust))
    # plt.legend()
    plt.savefig("AA_forecast_P1.pdf")

mj_AA_plot()
