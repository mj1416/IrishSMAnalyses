setwd("~/Documents/MPECDT/MRes/Danica/Irish SM data/")

full <- read.csv(file = "short_data.csv",dec='.',header = TRUE)

full <- full[-c(which(is.na(full[1,])))]

simple <- full[-c(1,2,3,4)]

qwe <- sort(unlist(simple,use.names = FALSE))

n = dim(simple)[1]
m = dim(simple)[2]

N = n*m
k = floor(N*0.08)

threshold = qwe[N-k+1]

c_est <- rowSums(simple>threshold)/k

require(graphics)
filename <- "hh_sced_prop.pdf"
pdf(file=filename,width = 12,paper = "a4r")
plot(c_est,type="l",ylab="",xlab="Day",yaxt="n",xaxt="n")
title(ylab=expression(hat(c)(10^-3)),mgp=c(2.65,1,0))
axis(side=1,at=seq(1,n,by=48*10),labels=seq(593,593+49,by=10))
axis(side=2,at=c(0,0.0004,0.0008,0.0012),labels = c(0,0.4,0.8,1.2))
dev.off()
