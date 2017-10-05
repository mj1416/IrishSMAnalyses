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


mymeplot <-function (data, omit = 3, labels = TRUE, plot=TRUE, ...) {
  data <- as.numeric(data)
  n <- length(data)
  myrank <- function(x, na.last = TRUE) {
    ranks <- sort.list(sort.list(x, na.last = na.last))
    if (is.na(na.last)) 
      x <- x[!is.na(x)]
    for (i in unique(x[duplicated(x)])) {
      which <- x == i & !is.na(x)
      ranks[which] <- max(ranks[which])
    }
    ranks
  }
  data <- sort(data)
  n.excess <- unique(floor(length(data) - myrank(data)))
  points <- unique(data)
  nl <- length(points)
  n.excess <- n.excess[-nl]
  points <- points[-nl]
  excess <- cumsum(rev(data))[n.excess] - n.excess * points
  y <- excess/n.excess
  xx <- points[1:(nl - omit)]
  yy <- y[1:(nl - omit)]
  if (plot) {
    plot(xx, yy, xlab = "", ylab = "", ...)
    if (labels) 
      title(xlab = "Threshold", ylab = "Mean Excess")
    invisible(list(x = xx, y = yy))
  }
  else c(xx,yy)
}

#########################       Data and ME plots     ##########################
AA_err1 <- read.csv(file = "AA_err.csv",dec='.',header = TRUE)
SD_err1 <- read.csv(file = "SD_err.csv",dec='.',header = TRUE)
LR_err1 <- read.csv(file = "LR_err.csv",dec='.',header = TRUE)

AA_err <- AA_err1[-c(1,2,3,4,5)]
SD_err <- SD_err1[-c(1,2,3,4,5)]
LR_err <- LR_err1[-c(1,2,3,4,5)]


qAA <- mymeplot(unlist(AA_err))#,plot=FALSE)
qSD <- mymeplot(unlist(SD_err))#,plot=FALSE)
qLR <- mymeplot(unlist(LR_err))#,plot=FALSE)

meAA <- data.frame(qAA$x,qAA$y)
meSD <- data.frame(qSD$x,qSD$y)
meLR <- data.frame(qLR$x,qLR$y)

require(ggplot2)
gmeAA <-ggplot(data=meAA,aes(x=qAA.x,y=qAA.y)) + geom_point(colour="indianred1") 
gmeAA + labs(x="Threshold",y="Mean Excess",title="AA")

gmeSD <-ggplot(data=meSD,aes(x=qSD.x,y=qSD.y)) + geom_point(colour="indianred1")
gmeSD + labs(y="Mean Excess",title="SD")
 
gmeLR <-ggplot(data=meLR,aes(x=qLR.x,y=qLR.y)) + geom_point(colour="indianred1")
gmeLR + labs(y="Mean Excess",title="WA")

require(gridExtra)
grid.arrange(gmeSD+ labs(x="",y="Mean Excess",title="SD")+theme(legend.position="none",panel.grid.minor=element_line(size = 0.5),panel.grid.major=element_line(size=0.5),plot.title = element_text(hjust=0.5)) ,gmeLR + labs(x="",y="Mean Excess",title="WA")+theme(legend.position="none",panel.grid.minor=element_line(size = 0.5),panel.grid.major=element_line(size=0.5),plot.title = element_text(hjust=0.5)),gmeAA+ labs(x="Threshold",y="Mean Excess",title="AA")+theme(legend.position="none",panel.grid.minor=element_line(size = 0.5),panel.grid.major=element_line(size=0.5),plot.title = element_text(hjust=0.5)),ncol=1,nrow=3)

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

qweAA = data.frame(n*ss,AAc_estG)
gAA <- ggplot(data = qweAA,mapping = aes(x=n*ss,y=AAc_estG)) +
  geom_hline(yintercept=1,colour="Dark Turquoise",linetype="dashed") +
  geom_line(color="Salmon") + theme(legend.position="none",panel.grid.minor=element_line(size = 1)) +
  theme(legend.position="none",panel.grid.minor=element_line(size = 0.5),panel.grid.major=element_line(size=0.5),plot.title = element_text(hjust=0.5)) +
  #geom_point(data=qwe[c(260,600,1295,1570,1980),],aes(x=n*ss[c(260,600,1295,1570,1980)],y=AAc_estG[c(1,2,3,4,5)]))+
  labs(x="Half Hour",y=expression(hat(c)),title="AA")
gAA

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

qweLR = data.frame(n*ss,LRc_estG)
gLR <- ggplot(data = qweLR,mapping = aes(x=n*ss,y=LRc_estG)) +
  geom_hline(yintercept=1,colour="Dark Turquoise",linetype="dashed") +
  geom_line(color="Salmon") + theme(legend.position="none",panel.grid.minor=element_line(size = 1)) +
  theme(legend.position="none",panel.grid.minor=element_line(size = 0.5),panel.grid.major=element_line(size=0.5),plot.title = element_text(hjust=0.5)) +
  #geom_point(data=qwe[c(260,600,1295,1570,1980),],aes(x=n*ss[c(260,600,1295,1570,1980)],y=AAc_estG[c(1,2,3,4,5)]))+
  labs(x="",y=expression(hat(c)),title="WA")
gLR

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

qweSD = data.frame(n*ss,SDc_estG)
gSD <- ggplot(data = qweSD,mapping = aes(x=n*ss,y=SDc_estG)) +
  geom_hline(yintercept=1,colour="Dark Turquoise",linetype="dashed") +
  geom_line(color="Salmon") + theme(legend.position="none",panel.grid.minor=element_line(size = 1)) +
  theme(legend.position="none",panel.grid.minor=element_line(size = 0.5),panel.grid.major=element_line(size=0.5),plot.title = element_text(hjust=0.5)) +
  #geom_point(data=qwe[c(260,600,1295,1570,1980),],aes(x=n*ss[c(260,600,1295,1570,1980)],y=AAc_estG[c(1,2,3,4,5)]))+
  labs(x="",y=expression(hat(c)))#,title="SD")
gSD

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


multiplot(gSD,gLR, gAA,rows=3)
