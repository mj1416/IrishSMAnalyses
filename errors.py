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
