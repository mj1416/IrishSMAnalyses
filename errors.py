def myMAPE(forecast, obs):
    import numpy as np
    import pandas as pd
    m,n = forecast.shape
    MAPE = 100*abs((forecast-obs)/obs)[range(4,n)].sum()/n
    return MAPE

def myErrorP(forecast,obs,p):
    import numpy as np
    import pandas as pd
    m,n = forecast.shape
    qwe = abs(forecast-obs)**p
    qwe1 = qwe[range(4,n)].sum()
    error = qwe1**(1.0/p)
    return error

def plot_mj_pnormerr(data,p):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
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
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
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
        import numpy as np
        import pandas as pd
        from munkres import Munkres
        #
        m = forecast.shape[1]
        for k in range(1,8):
            forecast1 = forecast[forecast.Day==k]
            obs1 = obs[obs.Day==k]
            for j in range(4,m):
                #print j
                qwe = forecast1[forecast1.columns[j]]
                qwe1 = obs1[obs1.columns[j]]
                #
                bigM = 14
                n = len(qwe)
                matrix_f = bigM*np.ones((n,n))
                #
                for i in range(n):
                    #print i
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
                if j==4:
                    qw = err_f
                else:
                    qw = np.hstack((qw,err_f))
            if k ==1:
                qwe2 = qw
            else:
                qwe2 = np.vstack((qwe2,qw))
        qwe2 = pd.DataFrame(qwe2,index = range(2016,2016+336))
        qwe3 = pd.concat([obs[range(4)],qwe2],1)
        qwe3.columns = obs.columns
        return qwe3

def plot_err():
    import pandas as pd
    import matplotlib.pyplot as plt
    #
    SD = pd.read_csv("SD_forecast.csv",index_col=0)
    LW = pd.read_csv("LW_forecast.csv",index_col=0)
    AA = pd.read_csv("AA_forecast.csv",index_col=0)
    LR = pd.read_csv("LR_forecast.csv",index_col=0)
    BR = pd.read_csv("BR_forecast.csv",index_col=0)
    data = pd.read_csv("short_data.csv",index_col=0)
    obs = data[data.Week==22]
    #
    SD_4err = myErrorP(SD,obs,4)
    LW_4err = myErrorP(LW,obs,4)
    AA_4err = myErrorP(AA,obs,4)
    LR_4err = myErrorP(LR,obs,4)
    BR_4err = myErrorP(BR,obs,4)
    #
    SD_Adj_err = pd.read_csv("SD_Adj_err.csv",index_col=0)
    SD_AAdj_err = ((SD_Adj_err[range(4,507)]**4).sum())**0.25
    LW_Adj_err = pd.read_csv("LW_Adj_err.csv",index_col=0)
    LW_AAdj_err = ((LW_Adj_err[range(4,507)]**4).sum())**0.25
    AA_Adj_err = pd.read_csv("AA_Adj_err.csv",index_col=0)
    AA_AAdj_err = ((AA_Adj_err[range(4,507)]**4).sum())**0.25
    LR_Adj_err = pd.read_csv("LR_Adj_err.csv",index_col=0)
    LR_AAdj_err = ((LR_Adj_err[range(4,507)]**4).sum())**0.25
    BR_Adj_err = pd.read_csv("BR_Adj_err.csv",index_col=0)
    BR_AAdj_err = ((BR_Adj_err[range(4,507)]**4).sum())**0.25
    #
    plt.subplot(5,1,1)
    plt.plot(range(1,504),SD_4err,"k",label="$E_4$")
    plt.plot(range(1,504),SD_AAdj_err,"r",label="$\hat{E}$")
    plt.xlim((1,504))
    plt.xticks([])
    plt.ylabel("SD")
    plt.legend()

    plt.subplot(5,1,2)
    plt.plot(range(1,504),LW_4err,"k",label="$E_4$")
    plt.plot(range(1,504),LW_AAdj_err,"r",label="$\hat{E}$")
    plt.xlim((1,504))
    plt.xticks([])
    plt.ylabel("LW")
    plt.legend()

    plt.subplot(5,1,3)
    plt.plot(range(1,504),AA_4err,"k",label="AA, $E_4$")
    plt.plot(range(1,504),AA_AAdj_err,"r",label="$\hat{E}$")
    plt.xlim((1,504))
    plt.xticks([])
    plt.ylabel("AA")
    plt.legend()

    plt.subplot(5,1,4)
    plt.plot(range(1,504),LR_4err,"k",label="LR, $E_4$")
    plt.plot(range(1,504),LR_AAdj_err,"r",label="$\hat{E}$")
    plt.xlim((1,504))
    plt.xticks([])
    plt.ylabel("LR")
    plt.legend()

    plt.subplot(5,1,5)
    plt.plot(range(1,504),BR_4err,"k",label="BR, $E_4$")
    plt.plot(range(1,504),BR_AAdj_err,"r",label="$\hat{E}$")
    plt.xlim((1,504))
    plt.xlabel("Customers")
    plt.ylabel("BR")
    plt.legend()
    plt.show()
    #plt.savefig("Errors.pdf")

def plot_4_err():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    #
    SD = pd.read_csv("SD_forecast.csv",index_col=0)
    LW = pd.read_csv("LW_forecast.csv",index_col=0)
    AA = pd.read_csv("AA_forecast.csv",index_col=0)
    LR = pd.read_csv("LR_forecast.csv",index_col=0)
    BR = pd.read_csv("BR_forecast.csv",index_col=0)
    data = pd.read_csv("short_data.csv",index_col=0)
    obs = data[data.Week==22]
    #
    SD_4err = myErrorP(SD,obs,4)
    LW_4err = myErrorP(LW,obs,4)
    AA_4err = myErrorP(AA,obs,4)
    LR_4err = myErrorP(LR,obs,4)
    BR_4err = myErrorP(BR,obs,4)

    plt.subplot(5,1,2)
    plt.plot(range(1,504),LW_4err, 'k',label="LW")
    plt.plot(range(1,504),np.ones(len(LW_4err))*LW_4err.mean(),'b')
    plt.xlim((1,504))
    plt.ylim((0,14))
    plt.xticks([])
    plt.ylabel("LW")

    plt.subplot(5,1,3)
    plt.plot(range(1,504),AA_4err, 'k',label="AA")
    plt.plot(range(1,504),np.ones(len(AA_4err))*AA_4err.mean(),'b')
    plt.xlim((1,504))
    plt.ylim((0,14))
    plt.xticks([])
    plt.ylabel("AA")

    plt.subplot(5,1,4)
    plt.plot(range(1,504),LR_4err, 'k',label="LR")
    plt.plot(range(1,504),np.ones(len(LR_4err))*LR_4err.mean(),'b')
    plt.xlim((1,504))
    plt.ylim((0,14))
    plt.xticks([])
    plt.ylabel("LR")

    plt.subplot(5,1,1)
    plt.plot(range(1,504),SD_4err, 'k',label="SD")
    plt.plot(range(1,504),np.ones(len(SD_4err))*SD_4err.mean(),'b')
    plt.xlim((1,504))
    plt.ylim((0,14))
    plt.xticks([])
    plt.ylabel("SD")

    plt.subplot(5,1,5)
    plt.plot(range(1,504),BR_4err, 'k',label="BR")
    plt.plot(range(1,504),np.ones(len(BR_4err))*BR_4err.mean(),'b')
    plt.xlim((1,504))
    plt.ylim((0,14))
    plt.ylabel("BR")
    plt.xlabel("Customers")
    plt.show()
    #plt.savefig("Errors_E_4.pdf")

def plot_AdjErr():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    #
    SD_Adj_err = pd.read_csv("SD_Adj_err.csv",index_col=0)
    SD_AAdj_err = ((SD_Adj_err[range(4,507)]**4).sum())**0.25
    LW_Adj_err = pd.read_csv("LW_Adj_err.csv",index_col=0)
    LW_AAdj_err = ((LW_Adj_err[range(4,507)]**4).sum())**0.25
    AA_Adj_err = pd.read_csv("AA_Adj_err.csv",index_col=0)
    AA_AAdj_err = ((AA_Adj_err[range(4,507)]**4).sum())**0.25
    LR_Adj_err = pd.read_csv("LR_Adj_err.csv",index_col=0)
    LR_AAdj_err = ((LR_Adj_err[range(4,507)]**4).sum())**0.25
    BR_Adj_err = pd.read_csv("BR_Adj_err.csv",index_col=0)
    BR_AAdj_err = ((BR_Adj_err[range(4,507)]**4).sum())**0.25
    #
    plt.subplot(5,1,2)
    plt.plot(range(1,504),LW_AAdj_err, 'k',label="LW")
    plt.plot(range(1,504),np.ones(len(LW_AAdj_err))*LW_AAdj_err.mean(),'b')
    plt.xlim((1,504))
    plt.ylim((0,10))
    plt.xticks([])
    plt.ylabel("LW")

    plt.subplot(5,1,3)
    plt.plot(range(1,504),AA_AAdj_err, 'k',label="AA")
    plt.plot(range(1,504),np.ones(len(AA_AAdj_err))*AA_AAdj_err.mean(),'b')
    plt.xlim((1,504))
    plt.ylim((0,10))
    plt.xticks([])
    plt.ylabel("AA")

    plt.subplot(5,1,4)
    plt.plot(range(1,504),LR_AAdj_err, 'k',label="LR")
    plt.plot(range(1,504),np.ones(len(LR_AAdj_err))*LR_AAdj_err.mean(),'b')
    plt.xlim((1,504))
    plt.ylim((0,10))
    plt.xticks([])
    plt.ylabel("LR")

    plt.subplot(5,1,1)
    plt.plot(range(1,504),SD_AAdj_err, 'k',label="SD")
    plt.plot(range(1,504),np.ones(len(SD_AAdj_err))*SD_AAdj_err.mean(),'b')
    plt.xlim((1,504))
    plt.ylim((0,10))
    plt.xticks([])
    plt.ylabel("SD")

    plt.subplot(5,1,5)
    plt.plot(range(1,504),BR_AAdj_err, 'k',label="BR")
    plt.plot(range(1,504),np.ones(len(BR_AAdj_err))*BR_AAdj_err.mean(),'b')
    plt.xlim((1,504))
    plt.ylim((0,10))
    plt.ylabel("BR")
    plt.xlabel("Customers")
    plt.show()
    #plt.savefig("Errors_Adj.pdf")
