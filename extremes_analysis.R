setwd("~/Documents/MPECDT/MRes/Danica/Irish SM data/")
library(ggplot2)
library(nutshell)
library(gridExtra)

library(evir)
library(fExtremes)

data <- read.csv(file = "short_data.csv",dec='.',header = TRUE)
acf(data[,5], plot=TRUE, main= "Title")

#data[,1] #first column
#data[1,] #first row
#data[1,2] #specific element


conf.level <- 0.95
ciline <- qnorm((1 - conf.level)/2)/sqrt(length(MEAN))

#Removing na
MEAN<-rowMeans(data[,5:507], na.rm = FALSE, dims = 1)
bacf <- acf(MEAN,lag.max = 48, plot=TRUE,main="Mean Electric Usage (Day)")
bacfdf <- with(bacf, data.frame(lag,acf))
q <- ggplot(data = bacfdf, mapping = aes(x = lag, y = acf)) +
  geom_hline(aes(yintercept = 0)) +
  geom_segment(mapping = aes(xend = lag, yend = 0),color="#FF6666")
conf.level <- 0.95
ciline <- qnorm((1 - conf.level)/2)/sqrt(length(MEAN))
q <- q + geom_hline(yintercept = ciline, color = "blue",size = 0.2,linetype="dashed") + 
  geom_hline(yintercept = -ciline, color = "blue",size = 0.2,linetype="dashed")
q
acf(MEAN,lag.max = 336, plot=TRUE,main="Mean Electric Usage (Week)")
acf(MEAN,lag.max = 672, plot=TRUE,main="Mean Electric Usage (2 Weeks)")
acf(MEAN,lag.max = 2352, plot=TRUE,main="Mean Electric Usage (Full")

#preparing for ggplot2
A <- data.frame(data, check.names= TRUE)

#to remove time series data, don't have to do this
simple <- data[ -c(1,2,3,4)]

#vectorise
data_vec <- unlist(simple,use.names=FALSE)

plot(density(data_vec),main="Energy Usage")

#mean excess plots
meplot(data_vec, omit=3)


#msratio plots at various values of p
msratioPlot(data_vec,p=1)
text(x=600000,y=0.5,"p=1")

#hill plot
hill(data_vec,option='xi', end=1000)
hill(data_vec,option='xi', end=100000)
hill(data_vec,option='xi')


#weekly max
WM <- read.csv(file = "weekly_max.csv",dec='.',header = TRUE)
wm_vec <- unlist(WM,use.names = FALSE)
msratioPlot(wm_vec,p = c(1,2,5,10))
text(x=2500,y=1.0,"p= 1",col="red")
text(x=2500,y=0.94,"p= 2",col="green")
text(x=2500,y=0.88,"p= 5",col="blue")
text(x=2500,y=0.82,"p=10",col="cyan")


