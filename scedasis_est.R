setwd("~/Documents/MPECDT/MRes/Danica/Irish SM data/")

data <- read.csv(file = "short_data.csv",dec='.',header = TRUE)
pos_diff <- read.csv(file = "pos_diff.csv",dec='.',header=TRUE)

data <- data[-c(which(is.na(data[1,])))]

simple <- data[-c(1,2,3,4)]

#data_vec <- unlist(simple,use.names = FALSE)
#data_ord <- sort(x=data_vec)

#define kernel
G_kernel <- function(u){
  if (abs(u)<=1){
    G <- 15*((1-u**2)**2)/16
  }else {
    G <- 0.0
  }
  return(G)
}

#########################       for actual measurements     ##########################
# define k
data_max <- apply(simple,1,max) 

n <- length(data_max)
k <- floor(n*0.08)
data_ord <- sort(data_max)
k_largest <- data_ord[(length(data_ord)-k+1)]#:length(data_ord)]

#define time vectors
ss <- seq(0,1,length=n)

#define bandwidth
h <- 0.1

#scedasis estimator
c_est <- vector(mode = "numeric",length = length(ss))
for (s in ss){
  i <- 1:n
  u <- (s-i/n)/h
  c_est[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
}

#generate and save an image in landscape pdf
require(graphics)
filename <- "hh_max_sced.pdf"
pdf(file=filename,width = 12,paper = "a4r")
plot(x = n*ss,y = c_est,type="l",col="blue",xaxt="n",ylab=expression(hat(c)),xlab='Day')
axis(side = 1,at=seq(1,n,by=48*4),labels = seq(593,593+49,by=4))
axis(side=2,at=c(0.4,0.8,1.2),labels = c(0.4,0.8,1.2))
dev.off()


#########################           Daily returns          ##########################




pdf(file = "pos_diff_sced.pdf",paper="a4")
par(mfrow=c(3,2))
#########################       Postive differences Mm     ##########################

data_max <- data.matrix(frame = pos_diff["Mm"],rownames.force = NA)

n <- length(data_max)
k <- floor(n*0.08)
data_ord <- sort(data_max)
k_largest <- data_ord[(length(data_ord)-k+1)]#:length(data_ord)]

#define time vectors
ss <- seq(0,1,length=n)

#define bandwidth
h <- 0.1

#scedasis estimator
c_est <- vector(mode = "numeric",length = length(ss))
for (s in ss){
  i <- 1:n
  u <- (s-i/n)/h
  c_est[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
}

plot(x = n*ss,y = c_est,type="l",col="red",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day',main = "Max of Mean")
axis(side = 1,at=c(0,10,20,30,40,48),labels = c(593,603,613,623,633,641))
axis(side=2,at=c(0,1,2,3),labels = c(0,1,2,3))


#########################       Postive differences MM     ##########################

data_max <- data.matrix(frame = pos_diff["MM"],rownames.force = NA)

n <- length(data_max)
k <- floor(n*0.08)
data_ord <- sort(data_max)
k_largest <- data_ord[(length(data_ord)-k+1)]#:length(data_ord)]

#define time vectors
ss <- seq(0,1,length=n)

#define bandwidth
h <- 0.1

#scedasis estimator
c_est <- vector(mode = "numeric",length = length(ss))
for (s in ss){
  i <- 1:n
  u <- (s-i/n)/h
  c_est[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
}


plot(x = n*ss,y = c_est,type="l",col="dark green",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day',main = "Max of Max")
axis(side = 1,at=c(0,10,20,30,40,48),labels = c(593,603,613,623,633,641))
axis(side=2,at=c(0,1,2,3),labels = c(0,1,2,3))


#########################       Postive differences MS      ##########################

data_max <- data.matrix(frame = pos_diff["MS"],rownames.force = NA)

n <- length(data_max)
k <- floor(n*0.08)
data_ord <- sort(data_max)
k_largest <- data_ord[(length(data_ord)-k+1)]#:length(data_ord)]

#define time vectors
ss <- seq(0,1,length=n)

#define bandwidth
h <- 0.1

#scedasis estimator
c_est <- vector(mode = "numeric",length = length(ss))
for (s in ss){
  i <- 1:n
  u <- (s-i/n)/h
  c_est[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
}


plot(x = n*ss,y = c_est,type="l",col="cyan",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day',main = "Max of Total")
axis(side = 1,at=c(0,10,20,30,40,48),labels = c(593,603,613,623,633,641))
axis(side=2,at=c(0,1,2,3),labels = c(0,1,2,3))
#dev.off()

#########################       Postive differences SS      ##########################

data_max <- data.matrix(frame = pos_diff["SS"],rownames.force = NA)

n <- length(data_max)
k <- floor(n*0.08)
data_ord <- sort(data_max)
k_largest <- data_ord[(length(data_ord)-k+1)]#:length(data_ord)]

#define time vectors
ss <- seq(0,1,length=n)

#define bandwidth
h <- 0.1

#scedasis estimator
c_est <- vector(mode = "numeric",length = length(ss))
for (s in ss){
  i <- 1:n
  u <- (s-i/n)/h
  c_est[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
}


plot(x = n*ss,y = c_est,type="l",col="magenta",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day',main = "Total of Total")
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