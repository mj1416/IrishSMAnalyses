import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import stat

def plot_autocorr():
    filename="~/Documents/MPECDT/MRes/Danica/Irish SM data/short_data.csv"
    data = pd.read_csv(filename,index_col=0)
    #
    #by day number
    DayN_sum = data.groupby('DayN').sum()
    dayn_sum = DayN_sum[range(4,DayN_sum.shape[1])].sum(axis=1)
    #
    #by day of the week
    #
    to plot t versus t-1
    today = DayN_sum[1:]
    yesterday = DayN_sum[:DayN_sum.shape[0]-1]
    #
    today_sum = today[range(4,today.shape[1])].sum(axis=1)
    yesterday_sum = yesterday[range(4,yesterday.shape[1])].sum(axis=1)
    #
    #do a subplot also about sums and means etc and each 503 etc.
    colors = cm.rainbow(np.linspace(0, 1, 504))
    for c in range(3,504):
        plt.figure(2)
        plt.scatter(yesterday[[c]],today[[c]],color=colors[c],marker ='.')
    plt.xlabel('Electricity usage on day d-1')
    plt.ylabel('Electricity usage on day d')
    plt.show()
    #
    plt.scatter(today[range(4,today.shape[1])],yesterday[range(4,yesterday.shape[1])])

def plot_sums():
    filename="~/Documents/MPECDT/MRes/Danica/Irish SM data/short_data.csv"
    data = pd.read_csv(filename)
    #
    #total usages
    #by half hour
    HH_sum = data.groupby('HH').sum()
    hh_sum = HH_sum[range(4,HH_sum.shape[1])].sum(axis=1)
    #
    #by day number
    DayN_sum = data.groupby('DayN').sum()
    dayn_sum = DayN_sum[range(4,DayN_sum.shape[1])].sum(axis=1)
    #
    #by the week number
    Week_sum = data.groupby('Week').sum()
    week_sum = Week_sum[range(4,Week_sum.shape[1])].sum(axis=1)
    #
    #by day of the week
    Day_sum = data.groupby('Day').sum()
    day_sum = Day_sum[range(4,Day_sum.shape[1])].sum(axis=1)
    #
    #plot various figures (sum)
    plt.figure(1)
    plt.subplot(2,2,1)
    #plt.suptitle('total usage for weeks 16-22')
    plt.plot(hh_sum,color='black',linestyle='-',marker='+')
    plt.xlabel('Time of day')
    plt.xticks((1,7,13,19,25,31,37,43,48),('00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00','23.30'))
    plt.ylabel('Smart meter \nreadings')
    #plt.title('Half-hourly total usage for weeks 16-22')
    #
    plt.subplot(2,2,2)
    plt.plot(week_sum,color='blue',linestyle='-',marker='+')
    plt.xlabel('Number of weeks')
    plt.ylabel('Smart meter \n readings')
    #plt.title('Weekly total usage for weeks 16-22')
    #
    plt.subplot(2,2,3)
    plt.plot(dayn_sum,color='magenta',linestyle='-',marker='+')
    plt.xlabel('Number of days')
    plt.ylabel('Smart meter \n readings')
    #plt.title('Daily total usage for weeks 16-22')
    #
    plt.subplot(2,2,4)
    plt.plot(day_sum,color='orange',linestyle='-',marker='+')
    plt.xlabel('Day of the Week')
    plt.xticks(range(1,8),('Mon','Tue','Wed','Thur','Fri','Sat','Sun'))
    plt.ylabel('Smart meter \n readings')
    #plt.title('total usage for weeks 16-22 by days of the week')
    #plt.tight_layout(pad=1,h_pad=1,w_pad=0.5)
    plt.show()
    # raw_input('press return to save file and continue')
    #print("Saving image")
    filename = "16_22_sum.png'
    plt.savefig(filename)

def plot_data_desc():

    filename="~/Documents/MPECDT/MRes/Danica/Irish SM data/short_data.csv"
    data = pd.read_csv(filename, index_col=0)
    #
    #by day number
    DayN_sum = data.groupby('DayN').mean()
    dayn_sum = DayN_sum[range(4,DayN_sum.shape[1])].mean(axis=1)
    #
    #
    #by day of the week
    Day_sum = data.groupby('Day').mean()
    day_sum = Day_sum[range(4,Day_sum.shape[1])].mean(axis=1)
    #
    Mon = data[data.Day==1].groupby("HH").mean()[range(3,data.shape[1]-1)].mean(1)
    Tues = data[data.Day==2].groupby("HH").mean()[range(3,data.shape[1]-1)].mean(1)
    Wed = data[data.Day==3].groupby("HH").mean()[range(3,data.shape[1]-1)].mean(1)
    Thur = data[data.Day==4].groupby("HH").mean()[range(3,data.shape[1]-1)].mean(1)
    Fri = data[data.Day==5].groupby("HH").mean()[range(3,data.shape[1]-1)].mean(1)
    Sat = data[data.Day==6].groupby("HH").mean()[range(3,data.shape[1]-1)].mean(1)
    Sun = data[data.Day==7].groupby("HH").mean()[range(3,data.shape[1]-1)].mean(1)
    #
    plt.figure(0)
    ax1 = plt.subplot2grid((4,2), (0,0), colspan=2,rowspan=1)
    ax1.plot(data.HH[:48],data.P1[:48])
    plt.xticks((1,7,13,19,25,31,37,43,48),('00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00','23.30'))
    plt.ylabel('kiloWatt hours')
    #

    ax2 = plt.subplot2grid((4,2), (1,0), colspan=2,rowspan=2)
    ax2.plot(Mon,color="blue",label="Monday")
    ax2.plot(Tues,color="red",label="Tuesday")
    ax2.plot(Wed,color="green",label="Wednesday")
    ax2.plot(Thur,color="magenta",label="Thursday")
    ax2.plot(Fri,color="cyan",label="Friday")
    ax2.plot(Sat,color="brown",label="Saturday")
    ax2.plot(Sun,color="orange",label="Sunday")
    plt.xticks((1,7,13,19,25,31,37,43,48),('00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00','23.30'))
    plt.ylabel('kiloWatt hours')
    ax2.legend()
    #

    ax3 = plt.subplot2grid((4,2), (3, 0), colspan=1,rowspan=1)
    ax3.plot(dayn_sum,color='magenta',linestyle='-',marker='+')
    plt.xlabel('Day Number')
    plt.ylabel('kiloWatt hours')
    #

    ax4 = plt.subplot2grid((4,2), (3, 1), colspan=1,rowspan=1)
    ax4.plot(day_sum,color='orange',linestyle='-',marker='+')
    plt.xticks(range(1,8),('Mon','Tue','Wed','Thur','Fri','Sat','Sun'))
    plt.ylabel('kiloWatt hours')
    plt.savefig("data_desc.pdf")
