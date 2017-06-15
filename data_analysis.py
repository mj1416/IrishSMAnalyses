import numpy as np
import pandas as pd
import stat
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def main():

    filename = "~/Documents/MPECDT/MRes/Danica/Irish SM data/16_22_weeks.xlsx"
    DATA=pd.read_excel(filename,sheetname=1,header=0,parse_cols="A:UA")


    #remove empty columns
    data=DATA.dropna(axis=1) #this is the data set where we have all the readings

    #total usages
    #by half hour
    HH_sum = data.groupby('HH').sum()
    hh_sum = HH_sum[range(4,HH_sum.shape[1])].sum(axis=1)

    #by day number
    DayN_sum = data.groupby('DayN').sum()
    dayn_sum = DayN_sum[range(4,DayN_sum.shape[1])].sum(axis=1)

    #to plot t versus t-1
    today = DayN_sum[1:]
    yesterday = DayN_sum[:DayN_sum.shape[0]-1]

    today_sum = today[range(4,today.shape[1])].sum(axis=1)
    yesterday_sum = yesterday[range(4,yesterday.shape[1])].sum(axis=1)

    #do a subplot also about sums and means etc and each 503 etc.
    colors = cm.rainbow(np.linspace(0, 1, 504))
    for c in range(3,504):
        plt.figure(2)
        plt.scatter(yesterday[[c]],today[[c]],color=colors[c],marker ='.')
    plt.xlabel('Electricity usage at time t on day d-1')
    plt.ylabel('Electricity usage at time t on day d')
    plt.show()

    # plt.scatter(today[range(4,today.shape[1])],yesterday[range(4,yesterday.shape[1])])

    #by the week number
    # Week_sum = data.groupby('Week').sum()
    # week_sum = Week_sum[range(4,Week_sum.shape[1])].sum(axis=1)
    #
    # #by day of the week
    # Day_sum = data.groupby('Day').sum()
    # day_sum = Day_sum[range(4,Day_sum.shape[1])].sum(axis=1)

    #plot various figures (sum)
    # plt.figure(1)
    # plt.subplot(2,2,1)
    # plt.suptitle('total usage for weeks 16-22')
    # plt.plot(hh_sum,color='black',linestyle='-',marker='+')
    # plt.xlabel('Time of day')
    # plt.xticks((1,7,13,19,25,31,37,43,48),('00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00','23.30'))
    # plt.ylabel('Smart meter \nreadings')
    # plt.title('Half-hourly total usage for weeks 16-22')
    #
    # plt.subplot(2,2,2)
    # plt.plot(week_sum,color='blue',linestyle='-',marker='+')
    # plt.xlabel('Number of weeks')
    # plt.ylabel('Smart meter \n readings')
    # plt.title('Weekly total usage for weeks 16-22')
    #
    # plt.subplot(2,2,3)
    # plt.plot(dayn_sum,color='magenta',linestyle='-',marker='+')
    # plt.xlabel('Number of days')
    # plt.ylabel('Smart meter \n readings')
    # plt.title('Daily total usage for weeks 16-22')
    #
    # plt.subplot(2,2,4)
    # plt.plot(day_sum,color='orange',linestyle='-',marker='+')
    # plt.xlabel('Day of the Week')
    # plt.xticks(range(1,8),('Mon','Tue','Wed','Thur','Fri','Sat','Sun'))
    # plt.ylabel('Smart meter \n readings')
    # plt.title('total usage for weeks 16-22 by days of the week')
    # plt.show()
    # raw_input('press return to save file and continue')
    #print("Saving image")
    #filename = "16_22_sum.png'
    #plt.savefig(filename)


main()
