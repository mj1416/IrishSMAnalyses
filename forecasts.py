import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Same Day Method
def mySD(past):
    "produces a weekly forecasting"
    "input should be past data"
    #isolate by Day of the Weekday
    Day1 = past[past.Day==1]
    Day2 = past[past.Day==2]
    Day3 = past[past.Day==3]
    Day4 = past[past.Day==4]
    Day5 = past[past.Day==5]
    Day6 = past[past.Day==6]
    Day7 = past[past.Day==7]

    #mean by HH
    forecast1 = np.zeros((len(np.unique(past.HH)),Day1.shape[1]-1))
    forecast2 = np.zeros((len(np.unique(past.HH)),Day2.shape[1]-1))
    forecast3 = np.zeros((len(np.unique(past.HH)),Day3.shape[1]-1))
    forecast4 = np.zeros((len(np.unique(past.HH)),Day4.shape[1]-1))
    forecast5 = np.zeros((len(np.unique(past.HH)),Day5.shape[1]-1))
    forecast6 = np.zeros((len(np.unique(past.HH)),Day6.shape[1]-1))
    forecast7 = np.zeros((len(np.unique(past.HH)),Day7.shape[1]-1))

    #generate forecast
    forecast1 = Day1.groupby("HH").mean()
    forecast2 = Day2.groupby("HH").mean()
    forecast3 = Day3.groupby("HH").mean()
    forecast4 = Day4.groupby("HH").mean()
    forecast5 = Day5.groupby("HH").mean()
    forecast6 = Day6.groupby("HH").mean()
    forecast7 = Day7.groupby("HH").mean()

    SD_forecast = pd.concat([forecast1,forecast2,forecast3,forecast4,forecast5,forecast6,forecast7])
    SD = SD_forecast[range(3,SD_forecast.shape[1])]

    w20 = past[past.Week == past.Week.max()]
    blah = pd.DataFrame()
    blah['Week'] = w20.Week + 1
    blah.index = range(2016,2016+336)
    DayN = w20.DayN + 7
    DayN.index = blah.index
    hh = w20.HH
    hh.index = blah.index
    D = w20.Day
    D.index = blah.index
    blah['DayN'] = DayN
    blah['HH'] = hh
    blah['Day'] = D

    SD.index = blah.index
    forecast = pd.concat([blah,SD],axis=1)
    forecast.columns = past.columns
    return forecast

def myLW(past):
    "produces a weekly forecast."
    "Input should be past data"
    lw = past.Week.max()
    LW = past[past.Week==lw]

    forecast = LW.copy()
    forecast['Week'] = LW.Week + 1
    forecast['DayN'] = LW.DayN + 7
    forecast.index = range(past.tail(1).index[0]+1,past.tail(1).index[0]+1+336)
    forecast.columns = past.columns
    return forecast

def myRegWeek(data):
    "produces weekly forecast. want it to return pd.df"
    from forecasts import myOneDayRegression
    reg1 = myOneDayRegression(data,1)
    reg2 = myOneDayRegression(data,2)
    reg3 = myOneDayRegression(data,3)
    reg4 = myOneDayRegression(data,4)
    reg5 = myOneDayRegression(data,5)
    reg6 = myOneDayRegression(data,6)
    reg7 = myOneDayRegression(data,7)

    reg = np.hstack([reg1,reg2,reg3,reg4,reg5,reg6,reg7])
    reg_forecast = reg.transpose()
    reg_forecast = pd.DataFrame(reg_forecast)

    past = data[data.Week!=22]
    w20 = past[past.Week == past.Week.max()]
    blah = pd.DataFrame()
    blah['Week'] = w20.Week + 1
    blah.index = range(past.tail(1).index[0]+1,past.tail(1).index[0]+1+336)
    DayN = w20.DayN + 7
    DayN.index = blah.index
    hh = w20.HH
    hh.index = blah.index
    D = w20.Day
    D.index = blah.index
    blah['DayN'] = DayN
    blah['HH'] = hh
    blah['Day'] = D

    reg_forecast.index = blah.index

    forecast = pd.concat([blah,reg_forecast],axis=1)
    forecast.columns = data.columns

    return forecast

def myOneDayRegression(data,dd=1):
    #from sklearn.linear_model import LinearRegression
    "produces a one day forecast (for the dd'th day)"
    forecast = np.zeros((data.shape[1]-4,48))
    for H in range(1,49):
        forecast_hh_d = myRegression(data,hh=H,d=dd)
        forecast[:,H-1] = forecast_hh_d[:,0]
    return forecast

def myRegression(data,hh=1,d=1):
    "produces a forecast for HH=hh (the second input)"
    "on the d'th day of week (d=third input). Default"
    "is 1st HH and day 1 (mondays)"
    from sklearn.linear_model import LinearRegression
    data1 = data[data.Day==d]
    past1 = data1[data1.Week!=22]
    past = past1[past1.Week!=21]
    #obs = data1[data1.Week==22]

    #create XX = some subset of past transposed.
    if hh ==1:
        h = [1,2,3]
    elif hh == 2:
        h = [1,2,3,4]
    elif hh in range(3,47):
        h = [hh-2,hh-1,hh,hh+1,hh+2]
    elif hh == 47:
        h = [45,46,47,48]
    elif hh == 48:
        h = [46,47,48]

    XX = pd.DataFrame()
    YY = pd.DataFrame()
    for i in h:
        XX = XX.append(past[past.HH==i],ignore_index=True)
        YY = YY.append(past1[past1.HH==i],ignore_index=True)
    #X = XX[(XX.Week!=XX.Week.max()) | (XX.HH!=hh)].transpose()[4:]
    X = XX.transpose()[4:]

    #YY = past[past.Week==past.Week.max()]
    Y = YY[(YY.Week==YY.Week.max()) &(YY.HH==hh)].transpose()[4:]

    #do regression on this
    lm = LinearRegression()
    lm.fit(X,Y)
    XY = YY[YY.Week!=YY.Week.min()]
    #forecast_hh_d = 'forecast_%d_%d' % (hh,d)
    forecast_hh_d = lm.predict(XY.transpose()[4:])

    return forecast_hh_d

def myForecastCompare(data):
    import time
    past = data[data.Week!=data.Week.max()]
    data_new = data[data.Week<=19]

    t0 = time.time()
    SD_forecast = mySD(past).drop(['Week','DayN','HH','Day'],1)
    t1 = time.time()
    LW_forecast = myLW(past).drop(['Week','DayN','HH','Day'],1)
    t2 = time.time()
    LR_forecast = myRegWeek(data_new).drop(['Week','DayN','HH','Day'],1)
    t3 = time.time()
    BR_forecast = myWeekRidge(data_new).drop(['Week','DayN','HH','Day'],1)
    t4 = time.time()

    oobs = data[data.Week==22].drop(['Week','DayN','HH','Day'],1)

    reg_err = abs(oobs - LR_forecast)**4
    SD_err = abs(oobs - SD_forecast)**4
    LW_err = abs(oobs - LW_forecast)**4
    BR_err = abs(oobs - BR_forecast)**4

    reg_err_sum = reg_err.sum(axis=0)
    SD_err_sum = SD_err.sum(axis=0)
    LW_err_sum = LW_err.sum(axis=0)
    BR_err_sum = BR_err.sum(axis=0)

    err_reg = reg_err_sum**0.25
    err_SD = SD_err_sum**0.25
    err_LW = LW_err_sum**0.25
    err_BR = BR_err_sum**0.25

    #print("time: SD = %.5f, LW = %.5f, Lin Reg = %.5f, Bay= %.5f" %(t1-t0,t2-t1,t3-t2,t4-t3))
    print("mean error: SD = %.5f, LW = %.5f, Lin Reg= %.5f, Bay= %.5f" %(np.mean(err_SD),np.mean(err_LW),np.mean(err_reg),np.mean(err_BR)))
    return err_reg, err_SD, err_LW, err_BR



    return reg_err, SD_err, LW_err

def myRidgeHH(data,hh=1,dd=1):
    "produces a forecast for half hour hh on day dd"
    "format is numpy array of shape (n_households,)"
    from sklearn.linear_model import BayesianRidge

    data1 = data[data.Day==dd]
    past1 = data1[data1.Week!=22]
    past = past1[past1.Week!=21]

    if hh ==1:
        h = [1,2,3]
    elif hh == 2:
        h = [1,2,3,4]
    elif hh in range(3,47):
        h = [hh-2,hh-1,hh,hh+1,hh+2]
    elif hh == 47:
        h = [45,46,47,48]
    elif hh == 48:
        h = [46,47,48]

    XX = pd.DataFrame()
    YY = pd.DataFrame()
    for i in h:
        XX = XX.append(past[past.HH==i],ignore_index=True)
        YY = YY.append(past1[past1.HH==i],ignore_index=True)
    X = XX.transpose()[4:]


    Y = YY[(YY.Week==YY.Week.max()) &(YY.HH==hh)].transpose()[4:]

    BR = BayesianRidge()
    BR.fit(X,Y)

    XX_new = YY[YY.Week!=YY.Week.min()]
    X_new = XX_new.transpose()[4:]
    forecast_hh_dd = BR.predict(X_new)
    return forecast_hh_dd

def myDayRidge(data,d=1):
    "produces a day foreast for day dd"
    "format is numpy array of shape (n_households,48)"
    from forecasts import myRidgeHH
    forecast_dd = np.zeros((data.shape[1]-4,48))
    for H in range(1,49):
        forecast_hh_dd = myRidgeHH(data,hh=H,dd=d)
        forecast_dd[:,H-1] = forecast_hh_dd
    return forecast_dd

def myWeekRidge(data):
    "produces a weekly forecast. format"
    "is pandas dataframe with the same"
    "indices and column names as obs"
    from forecasts import myDayRidge

    reg1 = myDayRidge(data,1)
    reg2 = myDayRidge(data,2)
    reg3 = myDayRidge(data,3)
    reg4 = myDayRidge(data,4)
    reg5 = myDayRidge(data,5)
    reg6 = myDayRidge(data,6)
    reg7 = myDayRidge(data,7)

    reg = np.hstack([reg1,reg2,reg3,reg4,reg5,reg6,reg7])
    reg_forecast = reg.transpose()
    reg_forecast = pd.DataFrame(reg_forecast)

    past = data[data.Week!=22]
    w20 = past[past.Week == past.Week.max()]
    blah = pd.DataFrame()
    blah['Week'] = w20.Week + 1
    blah.index = range(past.tail(1).index[0]+1,past.tail(1).index[0]+1+336)
    DayN = w20.DayN + 7
    DayN.index = blah.index
    hh = w20.HH
    hh.index = blah.index
    D = w20.Day
    D.index = blah.index
    blah['DayN'] = DayN
    blah['HH'] = hh
    blah['Day'] = D

    reg_forecast.index = blah.index

    forecast = pd.concat([blah,reg_forecast],axis=1)
    forecast.columns = data.columns

    return forecast