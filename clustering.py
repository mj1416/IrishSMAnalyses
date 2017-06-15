def myKmeans(past,n):
    "returns a matrix X (N_households, N_features+6) with details of the cluster"
    from sklearn.decomposition import PCA
    from sklearn.cluster import KMeans
    #isolate data into 6 times
    #Breakfast
    breakfast = past[past["HH"].isin(range(17))]
    breakday = breakfast[breakfast["Day"]<6]
    breakend = breakfast[breakfast["Day"]>=6]
    tbreakday = breakday[range(4,breakday.shape[1])].transpose()
    tbreakend = breakend[range(4,breakend.shape[1])].transpose()

    #Daytime
    daytime = past[past["HH"].isin(range(17,35))]
    dayday = daytime[daytime["Day"]<6]
    dayend = daytime[daytime["Day"]>=6]
    tdayday = dayday[range(4,dayday.shape[1])].transpose()
    tdayend = dayend[range(4,dayend.shape[1])].transpose()

    #evening
    evening = past[past["HH"].isin(range(35,49))]
    eveday = evening[evening["Day"]<6]
    eveend = evening[evening["Day"]>=6]
    teveday = eveday[range(4,eveday.shape[1])].transpose()
    teveend = eveend[range(4,eveend.shape[1])].transpose()

    #KMeans
    kmeans_breakday = KMeans(n_clusters=n).fit(tbreakday)
    kmeans_breakend = KMeans(n_clusters=n).fit(tbreakend)
    kmeans_dayday = KMeans(n_clusters=n).fit(tdayday)
    kmeans_dayend = KMeans(n_clusters=n).fit(tdayend)
    kmeans_eveday = KMeans(n_clusters=n).fit(teveday)
    kmeans_eveend = KMeans(n_clusters=n).fit(teveend)

    #cluster
    clus_breakday = kmeans_breakday.fit_predict(tbreakday)
    clus_breakend = kmeans_breakend.fit_predict(tbreakend)
    clus_dayday = kmeans_dayday.fit_predict(tdayday)
    clus_dayend = kmeans_dayend.fit_predict(tdayend)
    clus_eveday = kmeans_eveday.fit_predict(teveday)
    clus_eveend = kmeans_eveend.fit_predict(teveend)

    X = past.transpose()

    clus_breakday = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],clus_breakday)))
    clus_breakend = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],clus_breakend)))
    clus_dayday = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],clus_dayday)))
    clus_dayend = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],clus_dayend)))
    clus_eveday = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],clus_eveday)))
    clus_eveend = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],clus_eveend)))

    pca = PCA(n_components=2)

    clus_breakday.index = X.index
    #x_bd = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],pca.fit_transform(tbreakday)[:,0])),index=X.index)
    y_bd = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],pca.fit_transform(tbreakday)[:,1])),index = X.index)
    X['BD'] = clus_breakday
    #X['x_bd'] = x_bd
    #X['y_bd'] = y_bd


    clus_breakend.index = X.index
    #x_be = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],pca.fit_transform(tbreakend)[:,0])),index = X.index)
    #y_be = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],pca.fit_transform(tbreaked)[:,1])),index = X.index)
    X['BE'] = clus_breakend
    #X['x_be'] = x_be
    #X['y_be'] = y_be

    clus_dayday.index = X.index
    #x_dd = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],pca.fit_transform(tdayday)[:,0])),index = X.index)
    #y_dd = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],pca.fit_transform(tdayday)[:,1])),index = X.index)
    X['DD'] = clus_dayday
    #X['x_dd'] = x_dd
    #X['y_dd'] = y_dd

    clus_dayend.index = X.index
    #x_de = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],pca.fit_transform(tdayend)[:,0])),index = X.index)
    #y_de = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],pca.fit_transform(tdayend)[:,1])),index = X.index)
    X['DE'] = clus_dayday
    #X['x_de'] = x_de
    #X['y_de'] = y_de

    clus_eveday.index = X.index
    #x_ed = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],pca.fit_transform(teveday)[:,0])),index = X.index)
    #y_ed = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],pca.fit_transform(teveday)[:,1])),index = X.index)
    X['ED'] = clus_eveday
    #X['x_ed'] = x_ed
    #X['y_ed'] = y_ed

    clus_eveend.index = X.index
    #x_ee = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],pca.fit_transform(teveend)[:,0])),index = X.index)
    #y_ee = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],pca.fit_transform(teveend)[:,1])),index = X.index)
    X['EE'] = clus_eveend
    #X['x_ee'] = x_ee
    #X['y_ee'] = y_ee

    ################    visualising clusters    ######################
    # pca = PCA(n_components=2)
    # tbreakday['x'] = pca.fit_transform(tbreakday)[:,0]
    # tbreakend['x'] = pca.fit_transform(tbreakend)[:,0]
    # tbreakday['y'] = pca.fit_transform(tbreakday)[:,1]
    # tbreakend['y'] = pca.fit_transform(tbreakend)[:,1]
    # tbreakday['cluster'] = clus_breakday
    # tbreakend['cluster'] = clus_breakend
    #
    # tdayday['x'] = pca.fit_transform(tdayday)[:,0]
    # tdayend['x'] = pca.fit_transform(tdayend)[:,0]
    # tdayday['y'] = pca.fit_transform(tdayday)[:,1]
    # tdayend['y'] = pca.fit_transform(tdayend)[:,1]
    # tdayday['cluster'] = clus_dayday
    # tdayend['cluster'] = clus_dayend
    #
    # teveday['x'] = pca.fit_transform(teveday)[:,0]
    # teveend['x'] = pca.fit_transform(teveend)[:,0]
    # teveday['y'] = pca.fit_transform(teveday)[:,1]
    # teveend['y'] = pca.fit_transform(teveend)[:,1]
    # teveday['cluster'] = clus_eveday
    # teveend['cluster'] = clus_eveend
    #
    # new_breakday = tbreakday[["x","y","cluster"]]
    # new_breakend = tbreakend[["x","y","cluster"]]
    # new_dayday = tdayday[["x","y","cluster"]]
    # new_dayend = tdayend[["x","y","cluster"]]
    # new_eveday = teveday[["x","y","cluster"]]
    # new_eveend = teveend[["x","y","cluster"]]
    #
    # plt.subplot(1,2,1)
    # plt.plot(new_breakday[new_breakday.cluster ==0]['x'],new_breakday[new_breakday.cluster ==0]['y'],'g.',label="Cluster 1")
    # plt.plot(new_breakday[new_breakday.cluster ==1]['x'],new_breakday[new_breakday.cluster ==1]['y'],'b.',label="Cluster 2")
    # plt.plot(new_breakday[new_breakday.cluster ==2]['x'],new_breakday[new_breakday.cluster ==2]['y'],'r.', label="Cluster 3")
    # plt.title("Breakfast Weekday")
    # plt.subplot(1,2,2)
    # plt.plot(new_breakend[new_breakend.cluster ==0]['x'],new_breakend[new_breakend.cluster ==0]['y'],'g.',label="Cluster 1")
    # plt.plot(new_breakend[new_breakend.cluster ==1]['x'],new_breakend[new_breakend.cluster ==1]['y'],'b.',label="Cluster 2")
    # plt.plot(new_breakend[new_breakend.cluster ==2]['x'],new_breakend[new_breakend.cluster ==2]['y'],'r.', label="Cluster 3")
    # plt.title('Breakfast Weekend')
    # plt.legend()
    # plt.savefig('kmeans_s_breakfast_cluster.pdf')
    # plt.close()
    #
    # plt.subplot(1,2,1)
    # plt.plot(new_dayday[new_dayday.cluster ==0]['x'],new_dayday[new_dayday.cluster ==0]['y'],'g.',label="Cluster 1")
    # plt.plot(new_dayday[new_dayday.cluster ==1]['x'],new_dayday[new_dayday.cluster ==1]['y'],'b.',label="Cluster 2")
    # plt.plot(new_dayday[new_dayday.cluster ==2]['x'],new_dayday[new_dayday.cluster ==2]['y'],'r.',label="Cluster 3")
    # plt.title('Daytime Weekday')
    # plt.subplot(1,2,2)
    # plt.plot(new_dayend[new_dayend.cluster ==0]['x'],new_dayend[new_dayend.cluster ==0]['y'],'g.',label="Cluster 1")
    # plt.plot(new_dayend[new_dayend.cluster ==1]['x'],new_dayend[new_dayend.cluster ==1]['y'],'b.',label="Cluster 2")
    # plt.plot(new_dayend[new_dayend.cluster ==2]['x'],new_dayend[new_dayend.cluster ==2]['y'],'r.',label="Cluster 3")
    # plt.title('Daytime Weekend')
    # plt.legend()
    # plt.savefig('kmeans_s_daytime_cluster.pdf')
    # plt.close()
    #
    # plt.subplot(1,2,1)
    # plt.plot(new_eveday[new_eveday.cluster ==0]['x'],new_eveday[new_eveday.cluster ==0]['y'],'g.', label="Cluster 1")
    # plt.plot(new_eveday[new_eveday.cluster ==1]['x'],new_eveday[new_eveday.cluster ==1]['y'],'b.', label="Cluster 2")
    # plt.plot(new_eveday[new_eveday.cluster ==2]['x'],new_eveday[new_eveday.cluster ==2]['y'],'r.',label="Cluster 3")
    # plt.title('Evening Weekday')
    # plt.subplot(1,2,2)
    # plt.plot(new_eveend[new_eveend.cluster ==0]['x'],new_eveend[new_eveend.cluster ==0]['y'],'g.', label="Cluster 1")
    # plt.plot(new_eveend[new_eveend.cluster ==1]['x'],new_eveend[new_eveend.cluster ==1]['y'],'b.', label="Cluster 2")
    # plt.plot(new_eveend[new_eveend.cluster ==2]['x'],new_eveend[new_eveend.cluster ==2]['y'],'r.',label="Cluster 3")
    # plt.title('Evening Weekend')
    # plt.legend()
    # plt.savefig('kmeans_s_evening_cluster.pdf')
    # plt.close()
    #
    # #plotting mean against sd
    # new_breakday['mean'] = np.mean(tbreakday[tbreakday.columns[:560]],axis=1)
    # new_breakday['sd'] = np.std(tbreakday[tbreakday.columns[:560]],axis=1)
    #
    # new_breakend['mean'] = np.mean(tbreakend[tbreakend.columns[:224]],axis=1)
    # new_breakend['sd'] = np.std(tbreakend[tbreakend.columns[:224]],axis=1)
    #
    # new_dayday['mean'] = np.mean(tdayday[tdayday.columns[:630]],axis=1)
    # new_dayday['sd'] = np.std(tdayday[tdayday.columns[:630]],axis=1)
    #
    # new_dayend['mean'] = np.mean(tdayend[tdayend.columns[:252]],axis=1)
    # new_dayend['sd'] = np.std(tdayend[tdayend.columns[:252]],axis=1)
    #
    # new_eveday['mean'] = np.mean(teveday[teveday.columns[:490]],axis=1)
    # new_eveday['sd'] = np.std(teveday[teveday.columns[:490]],axis=1)
    #
    # new_eveend['mean'] = np.mean(teveend[teveend.columns[:196]],axis=1)
    # new_eveend['sd'] = np.std(teveend[teveend.columns[:196]],axis=1)
    #
    #
    # plt.subplot(1,2,1)
    # plt.plot(new_breakday[new_breakday.cluster ==0]['mean'],new_breakday[new_breakday.cluster ==0]['sd'],'g.',label="Cluster 1")
    # plt.plot(new_breakday[new_breakday.cluster ==1]['mean'],new_breakday[new_breakday.cluster ==1]['sd'],'b.',label="Cluster 2")
    # plt.plot(new_breakday[new_breakday.cluster ==2]['mean'],new_breakday[new_breakday.cluster ==2]['sd'],'r.', label="Cluster 3")
    # plt.xlabel('mean')
    # plt.ylabel('sd')
    # plt.title("Breakfast Weekday")
    # plt.subplot(1,2,2)
    # plt.plot(new_breakend[new_breakend.cluster ==0]['mean'],new_breakend[new_breakend.cluster ==0]['sd'],'g.',label="Cluster 1")
    # plt.plot(new_breakend[new_breakend.cluster ==1]['mean'],new_breakend[new_breakend.cluster ==1]['sd'],'b.',label="Cluster 2")
    # plt.plot(new_breakend[new_breakend.cluster ==2]['mean'],new_breakend[new_breakend.cluster ==2]['sd'],'r.', label="Cluster 3")
    # plt.title('Breakfast Weekend')
    # plt.xlabel('mean')
    # plt.legend()
    # plt.savefig('kmeans_s_breakfast_sd_mean.pdf')
    # plt.close()
    #
    # plt.subplot(1,2,1)
    # plt.plot(new_dayday[new_dayday.cluster ==0]['mean'],new_dayday[new_dayday.cluster ==0]['sd'],'g.',label="Cluster 1")
    # plt.plot(new_dayday[new_dayday.cluster ==1]['mean'],new_dayday[new_dayday.cluster ==1]['sd'],'b.',label="Cluster 2")
    # plt.plot(new_dayday[new_dayday.cluster ==2]['mean'],new_dayday[new_dayday.cluster ==2]['sd'],'r.',label="Cluster 3")
    # plt.title('Daytime Weekday')
    # plt.xlabel('mean')
    # plt.ylabel('sd')
    # plt.subplot(1,2,2)
    # plt.plot(new_dayend[new_dayend.cluster ==0]['mean'],new_dayend[new_dayend.cluster ==0]['sd'],'g.',label="Cluster 1")
    # plt.plot(new_dayend[new_dayend.cluster ==1]['mean'],new_dayend[new_dayend.cluster ==1]['sd'],'b.',label="Cluster 2")
    # plt.plot(new_dayend[new_dayend.cluster ==2]['mean'],new_dayend[new_dayend.cluster ==2]['sd'],'r.',label="Cluster 3")
    # plt.title('Daytime Weekend')
    # plt.xlabel('mean')
    # plt.legend()
    # plt.savefig('kmeans_s_daytime_sd_mean.pdf')
    # plt.close()
    #
    # plt.subplot(1,2,1)
    # plt.plot(new_eveday[new_eveday.cluster ==0]['mean'],new_eveday[new_eveday.cluster ==0]['sd'],'g.', label="Cluster 1")
    # plt.plot(new_eveday[new_eveday.cluster ==1]['mean'],new_eveday[new_eveday.cluster ==1]['sd'],'b.', label="Cluster 2")
    # plt.plot(new_eveday[new_eveday.cluster ==2]['mean'],new_eveday[new_eveday.cluster ==2]['sd'],'r.',label="Cluster 3")
    # plt.title('Evening Weekday')
    # plt.xlabel('mean')
    # plt.ylabel('sd')
    # plt.subplot(1,2,2)
    # plt.plot(new_eveend[new_eveend.cluster ==0]['mean'],new_eveend[new_eveend.cluster ==0]['sd'],'g.', label="Cluster 1")
    # plt.plot(new_eveend[new_eveend.cluster ==1]['mean'],new_eveend[new_eveend.cluster ==1]['sd'],'b.', label="Cluster 2")
    # plt.plot(new_eveend[new_eveend.cluster ==2]['mean'],new_eveend[new_eveend.cluster ==2]['sd'],'r.',label="Cluster 3")
    # plt.title('Evening Weekend')
    # plt.xlabel('mean')
    # plt.legend()
    # plt.savefig('kmeans_s_evening_sd_mean.pdf')
    # plt.close()

    return X

def myaffprop(past,num=None):
    "X should be in the shape of (N_households,N_features)"
    "returns number of clusters"
    from sklearn.cluster import AffinityPropagation

    breakfast = past[past.HH.isin(range(17))]
    daytime = past[past.HH.isin(range(17,35))]
    evening = past[past.HH.isin(range(35,49))]

    breakday = breakfast[breakfast.Day<6]
    breakend = breakfast[breakfast.Day>=6]
    dayday = daytime[daytime.Day<6]
    dayend = daytime[daytime.Day>=6]
    eveday = evening[evening.Day<6]
    eveend = evening[evening.Day>=6]

    af = AffinityPropagation(preference=num)

    X = past.transpose()

    clus_breakday = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],af.fit_predict(breakday.transpose()[4:]))),index=X.index)
    clus_breakend = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],af.fit_predict(breakend.transpose()[4:]))),index=X.index)
    clus_dayday = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],af.fit_predict(dayday.transpose()[4:]))),index=X.index)
    clus_dayend = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],af.fit_predict(dayend.transpose()[4:]))),index=X.index)
    clus_eveday = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],af.fit_predict(eveday.transpose()[4:]))),index=X.index)
    clus_eveend = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],af.fit_predict(eveend.transpose()[4:]))),index=X.index)

    X['BD'] = clus_breakday
    X['BE'] = clus_breakend
    X['DD'] = clus_dayday
    X['DE'] = clus_dayend
    X['ED'] = clus_eveday
    X['EE'] = clus_eveend

    return X

def mygaussianmix(past,n=3):
    "input is past data"
    from sklearn.mixture import GaussianMixture
    from sklearn.decomposition import PCA

    breakfast = past[past.HH.isin(range(17))]
    daytime = past[past.HH.isin(range(17,35))]
    evening = past[past.HH.isin(range(35,49))]

    breakday = breakfast[breakfast.Day<6]
    breakend = breakfast[breakfast.Day>=6]
    dayday = daytime[daytime.Day<6]
    dayend = daytime[daytime.Day>=6]
    eveday = evening[evening.Day<6]
    eveend = evening[evening.Day>=6]

    gm = GaussianMixture(n_components=n)

    XBD = breakday.transpose()[4:]
    gm.fit(XBD)
    cluster_XBD = gm.predict(XBD)
    cluster_XBD = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],cluster_XBD)))

    XBE = breakend.transpose()[4:]
    gm.fit(XBE)
    cluster_XBE = gm.predict(XBE)
    cluster_XBE = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],cluster_XBE)))

    XDD = dayday.transpose()[4:]
    gm.fit(XDD)
    cluster_XDD = gm.predict(XDD)
    cluster_XDD = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],cluster_XDD)))

    XDE = dayend.transpose()[4:]
    gm.fit(XDE)
    cluster_XDE = gm.predict(XDE)
    cluster_XDE = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],cluster_XDE)))

    XED = eveday.transpose()[4:]
    gm.fit(XED)
    cluster_XED = gm.predict(XED)
    cluster_XED = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],cluster_XED)))

    XEE = eveend.transpose()[4:]
    gm.fit(XEE)
    cluster_XEE = gm.predict(XEE)
    cluster_XEE = pd.DataFrame(np.hstack(([np.nan,np.nan,np.nan,np.nan],cluster_XEE)))

    X = past.transpose()
    cluster_XBD.index = X.index
    X['BD'] = cluster_XBD

    cluster_XBE.index = X.index
    X['BE'] = cluster_XBE

    cluster_XDD.index = X.index
    X['DD'] = cluster_XDD

    cluster_XDE.index = X.index
    X['DE'] = cluster_XDE

    cluster_XED.index = X.index
    X['ED'] = cluster_XED

    cluster_XEE.index = X.index
    X['EE'] = cluster_XEE

    #gm.fit(X)
    #cluster = gm.predict(X)
    #vec = np.zeros((len(cluster),3))
    #vec[:,0] = cluster
    #pca = PCA(n_components=2)
    #vec[:,1] = pca.fit_transform(X)[:,0]
    #vec[:,2] = pca.fit_transform(X)[:,1]
    return X

def myClusCompare(data,n=3):
    from clustering import myKmeans, mygaussianmix
    from sklearn.decomposition import PCA

    past = data[data.Week!=22]
    obs = data[data.Week==22]

    KK = myKmeans(past,n)
    GM = mygaussianmix(past,n)
