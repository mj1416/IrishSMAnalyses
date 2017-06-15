def myclus1(data,C=3):
    import numpy as np
    import pandas as pd
    from sklearn.cluster import KMeans
    from forecasts import mySD

    past = data[data.Week!=22]
    obs = data[data.Week==22]

    breakfast = past[past["HH"].isin(range(17))]
    breakday = breakfast[breakfast["Day"]<6]
    #breakend = breakfast[breakfast["Day"]>=6]
    tbreakday = breakday.transpose()

    kmeans_breakday = KMeans(n_clusters=C).fit(tbreakday[4:])
    clus_breakday = kmeans_breakday.fit_predict(tbreakday[4:])
    clus_breakday = np.append([np.nan,np.nan,np.nan,np.nan],clus_breakday)

    tpast = past.transpose()
    tpast['breakday'] = clus_breakday

    tobs = obs.transpose()
    tobs['breakday'] = clus_breakday

    mse = np.zeros(len(range(C)))

    for i in range(C):
        breakday0 = tpast[tpast.breakday==i]
        breakday0 = pd.concat([tpast[0:4],breakday0])

        p_bd0 = breakday0.transpose()[0:-1]
        forecast = mySD(p_bd0)
        mean_forecast = forecast[range(4,forecast.shape[1])].mean(axis=1)

        tobs0 = tobs[tobs.breakday==i]
        obs0 = tobs0.transpose()[0:-1]
        obs0_mean = obs0.mean(axis=1)
        obs0_mean.index = mean_forecast.index
        mse[i] = np.nanmean(np.sqrt((obs0_mean - mean_forecast)**2))

    return mse,np.nanmean(mse)

def myclus2(data,C=3,t=0):
    import numpy as np
    import pandas as pd
    from sklearn.mixture import GaussianMixture
    from forecasts import mySD
    from clustering import mygaussianmix

    #come up with X
    if t==0:
        #breakfast weekday
        breakfast = data[data["HH"].isin(range(17))]
        breakday = breakfast[breakfast["Day"]<6]
        past = breakday[breakday.Week!=22]
        obs = breakday[breakday.Week==22]
        tpast = past.transpose()
        tobs = obs.transpose()
        X = tpast[4:]
    elif t==1:
        #breakfast weekend
        breakfast = data[data["HH"].isin(range(17))]
        breakend = breakfast[breakfast["Day"]>=6]
        past = breakend[breakend.Week!=22]
        obs = breakend[breakend.Week==22]
        tpast = past.transpose()
        tobs = obs.transpose()
        X = tpast[4:]
    elif t==2:
        #daytime Weekday
        daytime = data[data["HH"].isin(range(17,35))]
        dayday = daytime[daytime["Day"]<6]
        past = dayday[dayday.Week!=22]
        obs = dayday[dayday.Week==22]
        tpast = past.transpose()
        tobs = obs.transpose()
        X = tpast[4:]
    elif t==3:
        #daytime weekend
        daytime = data[data["HH"].isin(range(17,35))]
        dayend = daytime[daytime["Day"]>=6]
        past = dayend[dayend.Week!=22]
        obs = dayend[dayend.Week==22]
        tpast = past.transpose()
        tobs = obs.transpose()
        X = tpast[4:]
    elif t==4:
        #evening weekday
        evening = data[data["HH"].isin(range(35,49))]
        eveday = evening[evening["Day"]<6]
        past = eveday[eveday.Week!=22]
        obs = eveday[eveday.Week==22]
        tpast = past.transpose()
        tobs = obs.transpose()
        X = tpast[4:]
    elif t==5:
        #evening weekend
        evening = data[data["HH"].isin(range(35,49))]
        eveend = evening[evening["Day"]>=6]
        past = eveend[eveend.Week!=22]
        obs = eveend[eveend.Week==22]
        tpast = past.transpose()
        tobs = obs.transpose()
        X = tpast[4:]

    #run gaussianmix with C
    vec = mygaussianmix(X,C)
    cluster = np.append([np.nan,np.nan,np.nan,np.nan],vec[:,0])
    tpast['cluster'] = cluster
    tobs['cluster'] = cluster

    #do mySD forecast & calc errors
    mse = np.zeros(len(range(C)))
    for i in range(C):
        time_i = tpast[tpast.cluster==i]
        time_i = pd.concat([tpast[0:4],time_i])
        forecast = mySD(time_i.transpose()[0:-1])
        mean_forecast = forecast[range(4,forecast.shape[1])].mean(axis=1)

        tobs_i = tobs[tobs.cluster==i]
        obs_i = tobs_i.transpose()[0:-1]
        obs_i_mean = obs_i.mean(axis=1)
        obs_i_mean.index = mean_forecast.index
        mse[i] = np.nanmean(np.sqrt((obs_i_mean - mean_forecast)**2))

    return mse, np.nanmean(mse)

def mygm(it,clus=[3,4,5,6,7,8,9,10]):
    from clustering import myclus2
    import numpy as np
    for C in clus:
        for t in range(6):
            rec = np.zeros((it))
            for pp in range(it):
                vec,mjmean = myclus2(data,C,t)
                rec[pp] = np.nanmean(vec)
            print(C,t,np.nanmean(rec),np.std(rec))
    #return rec#,np.nanmean(rec),np.std(rec)

def myOldAffProp(X,num=None):
    "X should be in the shape of (N_households,N_features)"
    "returns number of clusters"
    from sklearn.cluster import AffinityPropagation
    af = AffinityPropagation(preference=num).fit(X)
    n_clusters = len(af.cluster_centers_indices_)
    return n_clusters

def myMeanShift(X):
    from sklearn.cluster import MeanShift, estimate_bandwidth
    ms = MeanShift(bin_seeding=True, cluster_all=False)
    ms.fit(X)
    labels = ms.labels_
    n_clusters = len(np.unique(labels))
    return n_clusters
