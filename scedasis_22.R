setwd("~/Documents/MPECDT/MRes/Danica/Irish SM data/")

G_kernel <- function(u){
  if (abs(u)<=1){
    G <- 15*((1-u**2)**2)/16
  }else {
    G <- 0.0
  }
  return(G)
}

#########################      Actual measurement (22 weeks)     ##########################
full <- read.csv(file = "full_data.csv",dec='.',header = TRUE)

simple <- full[-c(1,2,3,4)]

# define k
data_max <- apply(simple,1,max) 

n <- length(data_max)
k <- floor(n*0.08)
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

require(graphics)
filename <- "22_household_max_sced.pdf"
pdf(file=filename,width = 12,paper = "a4r")
plot(x = n*ss,y = c_est,type="l",col="blue",ylab=expression(hat(c)),xlab='Day',xaxt="n",yaxt="n")
axis(side = 1,at=seq(1,n,by=48*10),labels = seq(488,488+154,by=10))
axis(side=2,at=c(0.4,0.8,1.2,1.6),labels = c(0.4,0.8,1.2,1.6))
dev.off()

#########################       Postive differences        ##########################
#########################       Postive differences        ##########################
pos_diff <- read.csv(file = "22_pos_diff.csv",dec='.',header=TRUE)

pdf(file = "pos_diff_sced_22.pdf",paper="a4")
par(mfrow=c(2,2))
#########################       Postive differences Mm     ##########################

data_max <- data.matrix(frame = pos_diff["Mm"],rownames.force = NA)

n <- length(data_max)
k <- floor(n*0.08)
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

plot(x = n*ss,y = c_est,type="l",col="red",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day',main = "Max of Mean")
axis(side = 1,at=c(0,50,100,150),labels = c(488,438,588,638))
axis(side=2,at=c(0,1,2),labels = c(0,1,2))


#########################       Postive differences MM     ##########################

data_max <- data.matrix(frame = pos_diff["MM"],rownames.force = NA)

n <- length(data_max)
k <- floor(n*0.08)
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


plot(x = n*ss,y = c_est,type="l",col="dark green",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day',main = "Max of Max")
axis(side = 1,at=c(0,50,100,150),labels = c(488,438,588,638))
axis(side=2,at=c(0,1,2),labels = c(0,1,2))


#########################       Postive differences MS      ##########################

data_max <- data.matrix(frame = pos_diff["MS"],rownames.force = NA)

n <- length(data_max)
k <- floor(n*0.08)
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


plot(x = n*ss,y = c_est,type="l",col="cyan",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day',main = "Max of Total")
axis(side = 1,at=c(0,50,100,150),labels = c(488,438,588,638))
axis(side=2,at=c(0,1,2),labels = c(0,1,2))
#dev.off()

#########################       Postive differences SS      ##########################

data_max <- data.matrix(frame = pos_diff["SS"],rownames.force = NA)

n <- length(data_max)
k <- floor(n*0.08)
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


plot(x = n*ss,y = c_est,type="l",col="magenta",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day',main = "Total of Total")
axis(side = 1,at=c(0,50,100,150),labels = c(488,438,588,638))
axis(side=2,at=c(0,1,2),labels = c(0,1,2))
dev.off()

#########################       Maximum Returns (average)      ##########################
max_ret <- read.csv(file = "max_returns_22.csv",dec='.',header=TRUE,row.names = "DayN")

data_max <- apply(max_ret,1,mean)

n <- length(data_max)
k <- floor(n*0.08)
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

filename <- "avg_max_ret_sced.pdf"
pdf(file=filename,width = 12,paper = "a4r")
plot(x = n*ss,y = c_est,type="l",col="blue",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day',main = "Average of Maximum Returns")
axis(side = 1,at=c(0,50,100,150),labels = c(488,438,588,638))
axis(side=2,at=c(0,1,2),labels = c(0,1,2))
dev.off()

#########################       Maximum Returns (boxplot)      ##########################

n <- dim(max_ret)[1]
k <- floor(n*0.08)
c_est <- matrix(0,nrow=nrow(max_ret),ncol = ncol(max_ret))
for (j in 1:dim(max_ret)[2]){
  data_max <- max_ret[,j]
  data_ord <- sort(data_max)
  k_largest <- data_ord[(length(data_ord)-k+1)]#:length(data_ord)]
  
  #define time vectors
  ss <- seq(1/n,1,1/n)
  
  #define bandwidth
  h <- 0.1
  
  #scedasis estimator
  for (s in ss){
    i <- 1:n
    u <- (s-i/n)/h
    c_est[match(s,ss),j] <- (sum((data_max>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
  }
}

plot(x=n*ss,c_est[,4],type="l",col="blue",xaxt="n",ylab=expression(hat(c)),xlab='Day',main = "Maximum Returns (P4)")
axis(side = 1,at=c(0,50,100,150),labels = c(488,438,588,638))
#axis(side=2,at=c(0,1,2),labels = c(0,1,2))


matplot(c_est,type="l",col=1:503,xaxt="n",ylab=expression(hat(c)),xlab='Day',main = "Maximum Returns (4 Customers)")
#axis(side = 1,at=c(0,50,100,150),labels = c(488,438,588,638))
#axis(side=2,at=c(0,1,2),labels = c(0,1,2))

filename="box_plot_max_ret_sced.pdf"
pdf(file=filename,width = 12,paper = "a4r")
boxplot(t(c_est),ylab=expression(hat(c)),xlab="Day",xaxt="n")
axis(side = 1,at=c(0,50,100,150),labels = c(488,438,588,638))
dev.off()

perc50 <- apply(c_est,1,quantile,probs=0.5)
perc95 <- apply(c_est,1,quantile,probs=0.95)

filename="max_ret_95_median.pdf"
pdf(file=filename,width = 12,paper = "a4r")
matplot(cbind(perc50,perc95),type="l",col=c("black","red"),xlab="Day",ylab=expression(hat(c)),xaxt="n")
axis(side = 1,at=c(0,50,100,150),labels = c(488,438,588,638))
dev.off()