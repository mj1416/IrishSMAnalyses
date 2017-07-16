def mj_adj_err(data,C,d):
    from mj_hungariandvg1 import mj_AAold
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from munkres import Munkres
    "data is full data"
    x,f1,f,d,cust = mj_AAold(data,C,d)

    n = len(x)
    bigM=14
    matrix_aa = bigM*np.ones((n,n))
    matrix_mean = bigM*np.ones((n,n))


    for i in range(n):
        if i ==0:
            matrix_aa[i,:4]= abs(f[:4]-x[i])
            matrix_mean[i,:4]= abs(f1[:4] - x[i])
        elif i == 1:
            matrix_aa[i,:5] = abs(f[:5] - x[i])
            matrix_mean[i,:5] = abs(f1[:5] - x[i])
        elif i == 2:
            matrix_aa[i,:6] = abs(f[:6] - x[i])
            matrix_mean[i,:6] = abs(f1[:6] - x[i])
        elif i == 45:
            matrix_aa[i,i-3:] = abs(f[i-3:] - x[i])
            matrix_mean[i, i-3:] = abs(f1[i-3:] - x[i])
        elif i== 46:
            matrix_aa[i,i-3:] = abs(f[i-3:]-x[i])
            matrix_mean[i,i-3:] = abs(f1[i-3:]-x[i])
        elif i == 47:
            matrix_aa[i,i-3:] = abs(f[i-3:]-x[i])
            matrix_mean[i,i-3:] = abs(f1[i-3:]-x[i])
        else:
            matrix_aa[i,i-3:i+4] = abs(f[i-3:i+4] - x[i])
            matrix_mean[i,i-3:i+4] = abs(f[i-3:i+4] - x[i])

    m = Munkres()
    indexes_aa = m.compute(matrix_aa)
    indexes_mean = m.compute(matrix_mean)
    np.set_printoptions(precision=4)

    err_aa =np.zeros((n,1))
    err_mean = np.zeros((n,1))
    for i in range(n):
        err_aa[i] = abs(f[indexes_aa[i][1]]-x[i])
        err_mean[i] = abs(f1[indexes_mean[i][1]]-x[i])

    p_norm_err_aa = sum(err_aa**4)**0.25
    p_norm_err_mean = sum(err_mean**4)**0.25
    #print(p_norm_err_aa, p_norm_err_mean)
    return p_norm_err_aa, p_norm_err_mean

def main(data):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from munkres import Munkres
    #
    from mj_hungariandvg1 import mj_AA
    #
    AA_err_vec = np.zeros((7,503))
    mean_err_vec = np.zeros((7,503))
    for d in [1]:#,2,3,4,5,6,7]:
        for i in range(1,2):
            AA_err_vec[d-1,i-1],mean_err_vec[d-1,i-1]=mj_adj_err(data,i,d)
        print(d)
        #print(d-1, AA_err_vec[d-1,:], mean_err_vec[d-1,:])
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax1 = fig.add_subplot(711)
    ax2 = fig.add_subplot(712)
    ax3 = fig.add_subplot(713)
    ax4 = fig.add_subplot(714)
    ax5 = fig.add_subplot(715)
    ax6 = fig.add_subplot(716)
    ax7 = fig.add_subplot(717)


    ax1.plot(AA_err_vec[0,:]-mean_err_vec[0,:],'-k',label='AA')
    ax1.plot(mean_err_vec[0,:]-mean_err_vec[0,:],'-b', label="Mean")
    ax1.set_xticks([])


    ax2.plot(AA_err_vec[1,:]-mean_err_vec[1,:],'-k',label='AA')
    ax2.plot(mean_err_vec[1,:]-mean_err_vec[1,:],'-b',label="Mean")
    ax2.set_xticks([])

    ax3.plot(AA_err_vec[2,]-mean_err_vec[2,:],'-k',label='AA')
    ax3.plot(mean_err_vec[2,:]-mean_err_vec[2,:],'-b',label="Mean")
    ax3.set_xticks([])

    ax4.plot(AA_err_vec[3,:]-mean_err_vec[3,:],'-k',label='AA')
    ax4.plot(mean_err_vec[3,:]-mean_err_vec[3,:],'-b',label="Mean")
    ax4.set_xticks([])

    ax5.plot(AA_err_vec[4,:]-mean_err_vec[4,:],'-k',label='AA')
    ax5.plot(mean_err_vec[4,:]-mean_err_vec[4,:], '-b',label="Mean")
    ax5.set_xticks([])

    ax6.plot(AA_err_vec[5,:]-mean_err_vec[5,:],'-k',label='AA')
    ax6.plot(mean_err_vec[5,:]-mean_err_vec[5,:],'-b', label="Mean")
    ax6.set_xticks([])

    ax7.plot(AA_err_vec[6,:]-mean_err_vec[6,:],'-k',label='AA')
    ax7.plot(mean_err_vec[6,:]-mean_err_vec[6,:], '-b',label="Mean")

    ax.tick_params(labelcolor='w', top='off', bottom='on', left='on', right='off')
    ax.set_xlabel('Customers')
    ax.set_ylabel('Adjusted p-Norm Error (P=4)')
    #plt.legend(['-k','-b'],["AA","Mean"])
    plt.show()
    for i in range(0, 7):
        print(i, sum(AA_err_vec[i,:]-mean_err_vec[i,:]) )
