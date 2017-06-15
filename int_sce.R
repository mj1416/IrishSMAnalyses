setwd("~/Documents/MPECDT/MRes/Danica/Irish SM data/")

data <- read.csv(file = "short_data.csv",dec='.',header = TRUE)

data <- data[-c(which(is.na(data[1,])))]

simple <- data[-c(1,2,3,4)]

# define k
data_max <- apply(simple,1,max)
k <- 30
data_ord <- sort(data_max)
k_largest <- data_ord[(length(data_ord)-k+1)]#:length(data_ord)]

#define time vectors
n <- dim(data)[1]
ss <- seq(0,1,length=n)
C_est <- vector(mode = "numeric",length = length(ss))

for (s in ss){
  up <- floor(n*s)
  C_est[match(s,ss)] <- sum(data_max[1:up]>k_largest)/k
  #print(paste(s,sum(data_max[1:up]>k_largest)/k))
  #print(s.index)
}

require(graphics)
plot(x = n*ss,y = C_est,type="l",xaxt="n",yaxt="n",col="blue",ylab=expression(hat(C)),xlab='Day')
axis(side = 1,at=seq(1,n,by=48*4),labels = seq(1,49,by=4))
axis(side=2,at=c(0,0.5,1),labels = c(0,0.5,1))
