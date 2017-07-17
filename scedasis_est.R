#########################       Biweight Kernel     ##########################
G_kernel <- function(u){
  if (abs(u)<=1){
    G <- 15*((1-u**2)**2)/16
  }else {
    G <- 0.0
  }
  return(G)
}

#########################       Epanechnikov Kernel     ##########################
K_kernel <- function(u){
  if (abs(u)<=1){
    K <- 3*(1-u**2)/4
  }else {
    K <- 0.0
  }
  return(K)
}

#########################       Set Directory    ##########################
setwd("~/Documents/MPECDT/MRes/Danica/Irish SM data/")

#########################       Load & Correct Data     ##########################

data <- read.csv(file = "short_data.csv",dec='.',header = TRUE)

simple <- data[-c(1,2,3,4,5)]

#########################       for actual measurements     ##########################
# define k
data_max <- apply(simple,1,max)
library(evir)
require(graphics)

#filename <- "hh_max_meplot.pdf"
#pdf(file=filename,width = 12,paper = "a4r")
#meplot(data_max,type="l")
#dev.off()

n <- length(data_max)
k <- 400
data_ord <- sort(data_max)
k_largest <- data_ord[(length(data_ord)-k)]#:length(data_ord)]

#define time vectors
ss <- seq(1/n,1,1/n)

#define bandwidth
h <- 0.1

#scedasis estimator with Biweight Kernel
c_estG <- vector(mode = "numeric",length = length(ss))
for (s in ss){
  i <- 1:n
  u <- (s-i/n)/h
  c_estG[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
}

#scedasis estimator with Epanechnikov Kernel
c_estK <- vector(mode = "numeric",length = length(ss))
for (s in ss){
  i <- 1:n
  u <- (s-i/n)/h
  c_estK[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=K_kernel)))/(k*h)
}

#generate and save an image in landscape pdf
filename <- "hh_max_sced_pres.pdf"
pdf(file=filename,width = 12,paper = "a4r")
plot(x=n*ss,y=c_estG,type="l",col="blue",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab="Day")
#matplot(x = cbind(n*ss,n*ss),y = cbind(c_estG,c_estK),type="l",col=c("blue","black"),xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day')
#legend("bottom", inset=.05, legend=c("Biweight Kernel", "Epanechnikov Kernel"), lty=c(1,2), col=c("blue","black"), horiz=FALSE)
axis(side = 1,at=seq(1,n,by=48*4),labels = seq(593,593+49,by=4))
axis(side=2,at=c(0.4,0.8,1.2),labels = c(0.4,0.8,1.2))
dev.off()


#########################           Positive Differences          ##########################

pdf(file = "pos_diff_sced.pdf",width=12,paper="a4r")
par(mfrow=c(2,2))
#########################       Postive differences Mm     ##########################

pos_diff <- read.csv(file = "pos_diff.csv",dec='.',header=TRUE)
data_max <- data.matrix(frame = pos_diff["SM"],rownames.force = NA)

n <- length(data_max)
k <- 20#floor(n*0.08)
data_ord <- sort(data_max)
k_largest <- data_ord[(length(data_ord)-k+1)]#:length(data_ord)]

#define time vectors
ss <- seq(1/n,1,1/n)

#define bandwidth
h <- 0.1

#scedasis estimator
c_est <- vector(mode = "numeric",length = length(ss))
for (s in ss){
  i <- 1:n
  u <- (s-i/n)/h
  c_est[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
}

plot(x = n*ss,y = c_est,type="l",col="red",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day',main = "Total of Daily Max")
axis(side = 1,at=c(0,10,20,30,40,48),labels = c(593,603,613,623,633,641))
axis(side=2,at=c(0,1,2,3),labels = c(0,1,2,3))


#########################       Postive differences MM     ##########################

data_max <- data.matrix(frame = pos_diff["MM"],rownames.force = NA)

n <- length(data_max)
k <- 20#floor(n*0.08)
data_ord <- sort(data_max)
k_largest <- data_ord[(length(data_ord)-k+1)]#:length(data_ord)]

#define time vectors
ss <- seq(1/n,1,1/n)

#define bandwidth
h <- 0.1

#scedasis estimator
c_est <- vector(mode = "numeric",length = length(ss))
for (s in ss){
  i <- 1:n
  u <- (s-i/n)/h
  c_est[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
}


plot(x = n*ss,y = c_est,type="l",col="dark green",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day',main = "Max of Daily Max")
axis(side = 1,at=c(0,10,20,30,40,48),labels = c(593,603,613,623,633,641))
axis(side=2,at=c(0,1,2,3),labels = c(0,1,2,3))


#########################       Postive differences MS      ##########################

data_max <- data.matrix(frame = pos_diff["MS"],rownames.force = NA)

n <- length(data_max)
k <- 20#floor(n*0.08)
data_ord <- sort(data_max)
k_largest <- data_ord[(length(data_ord)-k+1)]#:length(data_ord)]

#define time vectors
ss <- seq(1/n,1,1/n)

#define bandwidth
h <- 0.1

#scedasis estimator
c_est <- vector(mode = "numeric",length = length(ss))
for (s in ss){
  i <- 1:n
  u <- (s-i/n)/h
  c_est[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
}


plot(x = n*ss,y = c_est,type="l",col="cyan",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day',main = "Max of Daily Total")
axis(side = 1,at=c(0,10,20,30,40,48),labels = c(593,603,613,623,633,641))
axis(side=2,at=c(0,1,2,3),labels = c(0,1,2,3))
#dev.off()

#########################       Postive differences SS      ##########################

data_max <- data.matrix(frame = pos_diff["SS"],rownames.force = NA)

n <- length(data_max)
k <- 20#lofloor(n*0.08)
data_ord <- sort(data_max)
k_largest <- data_ord[(length(data_ord)-k+1)]#:length(data_ord)]

#define time vectors
ss <- seq(1/n,1,1/n)

#define bandwidth
h <- 0.1

#scedasis estimator
c_est <- vector(mode = "numeric",length = length(ss))
for (s in ss){
  i <- 1:n
  u <- (s-i/n)/h
  c_est[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
}


plot(x = n*ss,y = c_est,type="l",col="magenta",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day',main = "Total of Daily Total")
axis(side = 1,at=c(0,10,20,30,40,48),labels = c(593,603,613,623,633,641))
axis(side=2,at=c(0,1,2,3),labels = c(0,1,2,3))
dev.off()

#######################     checking with financial data      ########################

#Read in file and ensure date time understood
SP500 <- read.csv(file = "SP500.csv",dec = '.',header = TRUE)
SP500$Date <- as.Date(SP500$Date,format="%m/%d/%Y")

qwe <-subset(x = SP500,SP500$Date<=as.Date("2007-12-31"))
qwe1 <- subset(x=qwe, qwe$Date>=as.Date("1988-01-01"))
qwe2 <- qwe1[order(qwe1$Date),]


n <- dim(qwe2)[1]
print(paste("number of obs: ",dim(qwe2)[1]))
print(paste("number of losses:",sum( (qwe2$Adj.Close[1:n-1] - qwe2$Adj.Close[2:n])<0 )))
neg_returns <- abs(qwe2$Adj.Close[1:n-1] - qwe2$Adj.Close[2:n])/qwe2$Adj.Close[1:n-1]

k <- 130
h <- 0.1
data_ord <- sort(neg_returns)
k_largest <- data_ord[(length(neg_returns)-k+1)]#:length(data_ord)]

ss <- seq(0,1,length=n-1)

c_est <- vector(mode = "numeric",length = length(ss))
for (s in ss){
  i <- 1:(n-1)
  u <- (s-i/(n-1))/h
  c_est[match(s,ss)] <- (sum((neg_returns>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
}

plot(x = n*ss,y = c_est,type="l",col="blue",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Year')
axis(side = 1,at=c(1,1012,2023,3034,4038),labels = c(1988,1992,1996,2000,2004))
axis(side=2,at=c(0,0.5,1,1.5,2,2.5,3),labels = c(0,0.5,1,1.5,2,2.5,3))
#dev.off()