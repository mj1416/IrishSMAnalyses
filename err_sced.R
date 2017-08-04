setwd("~/Documents/MPECDT/MRes/Danica/Irish SM data/")

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

#########################       Data and ME plots     ##########################
AA_err1 <- read.csv(file = "AA_err.csv",dec='.',header = TRUE)
SD_err1 <- read.csv(file = "SD_err.csv",dec='.',header = TRUE)
LR_err1 <- read.csv(file = "LR_err.csv",dec='.',header = TRUE)

AA_err <- AA_err1[-c(1,2,3,4,5)]
SD_err <- SD_err1[-c(1,2,3,4,5)]
LR_err <- LR_err1[-c(1,2,3,4,5)]

require(evir)
require(graphics)
filename <- 'AA_err_meplot.pdf'
pdf(file=filename,width=12,paper="a4r")
meplot(unlist(AA_err,use.names = FALSE),main="AA_err")
dev.off()
filename <- 'SD_err_meplot.pdf'
pdf(file=filename,width=12,paper="a4r")
meplot(unlist(SD_err,use.names = FALSE),main="SD_err")
dev.off()
filename <- 'LR_err_meplot.pdf'
pdf(file=filename,width=12,paper="a4r")
meplot(unlist(LR_err,use.names = FALSE),main="WA_err")
dev.off()
#########################       AA scedasis     ##########################

data_max <- apply(AA_err,1,max)

n <- length(data_max)
k <- 100
data_ord <- sort(data_max)
k_largest <- data_ord[(length(data_ord)-k)]#:length(data_ord)]

#define time vectors
ss <- seq(1/n,1,1/n)

#define bandwidth
h <- 0.1

#scedasis estimator
AAc_estG <- vector(mode = "numeric",length = length(ss))
for (s in ss){
  i <- 1:n
  u <- (s-i/n)/h
  AAc_estG[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
}

#c_estK <- vector(mode = "numeric",length = length(ss))
#for (s in ss){
#  i <- 1:n
#  u <- (s-i/n)/h
#  c_estK[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=K_kernel)))/(k*h)
#}

filename <- "AA_err_sced.pdf"
pdf(file=filename,width = 12,paper = "a4r")
plot(x = n*ss,y =AAc_estG,type="l",col="blue",xaxt="n",ylab=expression(hat(c)),xlab='Day')
#legend("bottomright", inset=.05, legend=c("Biweight Kernel", "Epanechnikov Kernel"), lty=c(1,2), col=c("blue","black"), horiz=FALSE)
axis(side = 1,at=seq(24,n,by=48),labels = seq(635,641))
axis(side=2,at=c(0.4,0.8,1.2,1.6),labels = c(0.4,0.8,1.2,1.6))
dev.off()

#########################       LR scedasis     ##########################

data_max <- apply(LR_err,1,max)

n <- length(data_max)
k <- 100
data_ord <- sort(data_max)
k_largest <- data_ord[(length(data_ord)-k)]#:length(data_ord)]

#define time vectors
ss <- seq(1/n,1,1/n)

#define bandwidth
h <- 0.1

#scedasis estimator
LRc_estG <- vector(mode = "numeric",length = length(ss))
for (s in ss){
  i <- 1:n
  u <- (s-i/n)/h
  LRc_estG[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
}

#c_estK <- vector(mode = "numeric",length = length(ss))
#for (s in ss){
#  i <- 1:n
#  u <- (s-i/n)/h
#  c_estK[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=K_kernel)))/(k*h)
#}

require(graphics)
filename <- "LR_err_sced.pdf"
pdf(file=filename,width = 12,paper = "a4r")
plot(x = n*ss,y =LRc_estG,type="l",col="blue",xaxt="n",ylab=expression(hat(c)),xlab='Day')
#legend("bottomright", inset=.05, legend=c("Biweight Kernel", "Epanechnikov Kernel"), lty=c(1,2), col=c("blue","black"), horiz=FALSE)
axis(side = 1,at=seq(24,n,by=48),labels = seq(635,641))
axis(side=2,at=c(0.4,0.8,1.2,1.6),labels = c(0.4,0.8,1.2,1.6))
dev.off()

#########################       SD scedasis     ##########################

data_max <- apply(SD_err,1,max)

n <- length(data_max)
k <- 100
data_ord <- sort(data_max)
k_largest <- data_ord[(length(data_ord)-k)]#:length(data_ord)]

#define time vectors
ss <- seq(1/n,1,1/n)

#define bandwidth
h <- 0.1

#scedasis estimator
SDc_estG <- vector(mode = "numeric",length = length(ss))
for (s in ss){
  i <- 1:n
  u <- (s-i/n)/h
  SDc_estG[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
}

#c_estK <- vector(mode = "numeric",length = length(ss))
#for (s in ss){
#  i <- 1:n
#  u <- (s-i/n)/h
#  c_estK[match(s,ss)] <- (sum((data_max>k_largest)*sapply(u,FUN=K_kernel)))/(k*h)
#}

require(graphics)
filename <- "SD_err_sced.pdf"
pdf(file=filename,width = 12,paper = "a4r")
plot(x = n*ss,y =SDc_estG,type="l",col="blue",xaxt="n",ylab=expression(hat(c)),xlab='Day')
#legend("bottomright", inset=.05, legend=c("Biweight Kernel", "Epanechnikov Kernel"), lty=c(1,2), col=c("blue","black"), horiz=FALSE)
axis(side = 1,at=seq(24,n,by=48),labels = seq(635,641))
axis(side=2,at=c(0.4,0.8,1.2,1.6),labels = c(0.4,0.8,1.2,1.6))
dev.off()


filename <- "err_sced_together.pdf"
pdf(file=filename,width = 12,paper = "a4r")
par(mfrow=c(3,1),mai=c(0.6,1,0.1,0.5))
plot(x = n*ss,y =AAc_estG,type="l",col="blue",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day')
legend("bottom", inset=0.5, legend=c("AA"), lty=c(1), col=c("blue"), horiz=FALSE)
axis(side = 1,at=seq(24,n,by=48),labels = seq(635,641))
axis(side=2,at=c(0.4,1.0,1.5),labels = c(0.4,1.0,1.5))
plot(x = n*ss,y =LRc_estG,type="l",col="blue",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day')
legend("bottom", inset=0.5, legend=c("LR"), lty=c(1), col=c("blue"), horiz=FALSE)
axis(side = 1,at=seq(24,n,by=48),labels = seq(635,641))
axis(side=2,at=c(0.4,1.0,1.6),labels = c(0.4,1.0,1.6))
plot(x = n*ss,y =SDc_estG,type="l",col="blue",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Day')
legend("bottom", inset=0.5, legend=c("SD"), lty=c(1), col=c("blue"), horiz=FALSE)
axis(side = 1,at=seq(24,n,by=48),labels = seq(635,641))
axis(side=2,at=c(0.4,1.0,1.6),labels = c(0.4,1.0,1.6))
dev.off()

