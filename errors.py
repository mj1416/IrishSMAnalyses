def myMAPE(forecast, obs):
    m,n = forecast.shape
    MAPE = 100*abs((forecast-obs)/obs)[range(4,n)].sum()/n
    return MAPE

def myErrorP(forecast,obs,p):
    m,n = forecast.shape
    qwe = abs(forecast-obs)**p
    qwe1 = qwe[range(4,n)].sum()
    error = qwe1**(1.0/p)
    return error

def plot_mj_pnormerr(data,p):
    AA = pd.read_csv("AA_forecast.csv",index_col=0)
    from forecasts import *
    past = data[data.Week!=22]
    obs = data[data.Week==22]
    SD = mySD(past)
    LW = myLW(past)
    LR = myRegWeek(data)
    BR = myWeekRidge(data)
    #
    AA_err = myErrorP(AA,obs,p)
    SD_err = myErrorP(SD,obs,p)
    LW_err = myErrorP(LW,obs,p)
    LR_err = myErrorP(LR,obs,p)
    BR_err = myErrorP(BR,obs,p)
    #plot subplots
    #
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_ylabel("$4^{th}-$norm Errors (kWh)")
    ax.set_xlabel("Customers")
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')
    #
    fig.add_subplot(4,1,1)
    plt.plot(range(1,504),LW_err-SD_err,"g",label="LW")
    plt.plot(range(1,504),SD_err-SD_err,"black")#,label="0")
    #plt.ylabel("$E_4$ (kWh)")
    plt.xlim((0,505))
    plt.legend()
    #
    fig.add_subplot(4,1,2)
    plt.plot(range(1,504),AA_err-SD_err,"red",label="AA")
    plt.plot(range(1,504),SD_err-SD_err,"black")#,label="0")
    #plt.ylabel("$E_4$ (kWh)")
    plt.xlim((0,505))
    plt.legend()
    #
    fig.add_subplot(4,1,3)
    plt.plot(range(1,504),LR_err-SD_err,"gold",label="LR")
    plt.plot(range(1,504),SD_err-SD_err,"black")#,label="0")
    #plt.ylabel("$E_4$ (kWh)")
    plt.xlim((0,505))
    plt.legend()
    #
    fig.add_subplot(4,1,4)
    plt.plot(range(1,504),BR_err-SD_err,"blue",label="BR")
    plt.plot(range(1,504),SD_err-SD_err,"black")#,label="0")
    #plt.ylabel("$E_4$ (kWh)")
    #plt.xlabel("Customers")
    plt.xlim((0,505))
    plt.legend()
    plt.show()
    #plt.savefig("rel_4_norm_err.pdf")

def plot_mj_MAPE(data):
    AA = pd.read_csv("AA_forecast.csv",index_col=0)
    from forecasts import *
    past = data[data.Week!=22]
    obs = data[data.Week==22]
    SD = mySD(past)
    LW = myLW(past)
    LR = myRegWeek(data)
    BR = myWeekRidge(data)
    #
    AA_err = myMAPE(AA,obs)
    SD_err = myMAPE(SD,obs)
    LW_err = myMAPE(LW,obs)
    LR_err = myMAPE(LR,obs)
    BR_err = myMAPE(BR,obs)
    #plot subplots
    #
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_ylabel("MAPE (%)")
    ax.set_xlabel("Customers")
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')
    #
    fig.add_subplot(4,1,1)
    plt.plot(range(1,504),LW_err-SD_err,"g",label="LW")
    plt.plot(range(1,504),SD_err-SD_err,"black")#,label="0")
    #plt.ylabel("$E_4$ (kWh)")
    plt.xlim((0,505))
    plt.legend()
    #
    fig.add_subplot(4,1,2)
    plt.plot(range(1,504),AA_err-SD_err,"red",label="AA")
    plt.plot(range(1,504),SD_err-SD_err,"black")#,label="0")
    #plt.ylabel("$E_4$ (kWh)")
    plt.xlim((0,505))
    plt.legend()
    #
    fig.add_subplot(4,1,3)
    plt.plot(range(1,504),LR_err-SD_err,"gold",label="LR")
    plt.plot(range(1,504),SD_err-SD_err,"black")#,label="0")
    #plt.ylabel("$E_4$ (kWh)")
    plt.xlim((0,505))
    plt.legend()
    #
    fig.add_subplot(4,1,4)
    plt.plot(range(1,504),BR_err-SD_err,"blue",label="BR")
    plt.plot(range(1,504),SD_err-SD_err,"black")#,label="0")
    #plt.ylabel("$E_4$ (kWh)")
    #plt.xlabel("Customers")
    plt.xlim((0,505))
    plt.legend()
    plt.show()
    #plt.savefig("rel_MAPE.pdf")

def myAdjError(forecast,obs):
    from munkres import Munkres
    n,m = forecast.shape
    blah = forecast.copy()
    #
    for j in range(4,m):
        print j
        qwe = forecast[forecast.columns[j]]
        qwe1 = obs[obs.columns[j]]
        #
        bigM = 14
        matrix_f = bigM*np.ones((n,n))
        #
        for i in range(n):
            if i ==0:
                matrix_f[i,:4]= abs(qwe[:4]-qwe1[qwe1.index[i]])
            elif i == 1:
                matrix_f[i,:5] = abs(qwe[:5] - qwe1[qwe1.index[i]])
            elif i == 2:
                matrix_f[i,:6] = abs(qwe[:6] - qwe1[qwe1.index[i]])
            elif i == 45:
                matrix_f[i,i-3:] = abs(qwe[i-3:] - qwe1[qwe1.index[i]])
            elif i== 46:
                matrix_f[i,i-3:] = abs(qwe[i-3:]-qwe1[qwe1.index[i]])
            elif i == 47:
                matrix_f[i,i-3:] = abs(qwe[i-3:]-qwe1[qwe1.index[i]])
            else:
                matrix_f[i,i-3:i+4] = abs(qwe[i-3:i+4] - qwe1[qwe1.index[i]])
        MM = Munkres()
        index_f = MM.compute(matrix_f)
        err_f = np.zeros((n,1))
        for i in range(n):
            err_f[i] = abs(qwe[qwe.index[index_f[i][1]]]-qwe1[qwe1.index[i]])
        blah[blah.columns[j]]=err_f
    return blah
