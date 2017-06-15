setwd("~/Documents/MPECDT/MRes/Danica/Irish SM data/")

#Define Kernel
G_kernel <- function(u){
  if (abs(u)<=1){
    G <- 15*((1-u**2)**2)/16
  }else {
    G <- 0.0
  }
  return(G)
}

#Read in file and ensure date time understood
SP500 <- read.csv(file = "SP500.csv",dec = '.',header = TRUE)
SP500$Date <- as.Date(SP500$Date,format="%m/%d/%Y")
SP500$Day <- weekdays(SP500$Date)

qwe <-subset(x = SP500,SP500$Date<as.Date("2008-01-01"))
qwe1 <- subset(x=qwe, qwe$Date>as.Date("1987-12-31"))
qwe2 <- qwe1[order(qwe1$Date),]

#Wed <-subset(x = qwe2,qwe2$Day=="Friday")
n <- dim(qwe2)[1]
print(paste("number of obs: ",dim(qwe2)[1]))
print(paste("number of losses:",sum( (qwe2$Adj.Close[2:n] - qwe2$Adj.Close[1:n-1])<0 )))
neg_returns <- abs(qwe2$Adj.Close[2:n] - qwe2$Adj.Close[1:n-1])/qwe2$Adj.Close[1:n-1]
n <- length(neg_returns)

k <- 130
h <- 0.1
data_ord <- sort(neg_returns)
k_largest <- data_ord[(length(neg_returns)-k+1)]#:length(data_ord)]

ss <- seq(1/n,1, 1/n)

c_est <- numeric(n)
for (s in ss){
  i <- 1:(n)
  u <- (s-i/(n))/h
  c_est[match(s,ss)] <- (sum((neg_returns>k_largest)*sapply(u,FUN=G_kernel)))/(k*h)
}

require(graphics)
pdf(file="SP500_sced_qwe.pdf",width = 12,paper = "a4r")
plot(x = n*ss,y = c_est,type="l",col="blue",xaxt="n",yaxt="n",ylab=expression(hat(c)),xlab='Year',main="1988 - 2007")
axis(side=2,at=c(0,0.5,1,1.5,2,2.5,3),labels = c(0,0.5,1,1.5,2,2.5,3))
axis(side = 1,at=c(200,1200,2200,3200,4200),labels = c(format(qwe2[200,1],"%Y"),format(qwe2[1200,1],"%Y"),format(qwe2[2200,1],"%Y"),format(qwe2[3200,1],"%Y"),format(qwe2[4200,1],"%Y")))
dev.off()

