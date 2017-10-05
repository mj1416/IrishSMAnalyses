setwd("~/Documents/MPECDT/MRes/Danica/Irish SM data/")

full <- read.csv(file = "short_data.csv",dec='.',header = TRUE)

#full <- full[-c(which(is.na(full[1,])))]

simple <- full[-c(1,2,3,4,5)]

qwe <- sort(unlist(simple,use.names = FALSE))

n = dim(simple)[1]
m = dim(simple)[2]

N = n*m
k = 400#sum(qwe>6)#24000#floor(N*0.08)

threshold = qwe[N-k+1]

p_est <- rowSums(simple>threshold)/k

require(graphics)
filename <- "hh_sced_prop_full.pdf"
pdf(file=filename,width = 12,paper = "a4r")
plot(p_est,type ="p",pch="*",ylab=expression(hat(p)),xaxt="n" ,mgp=c(2.65,1,0),xlab="Day")
#title(ylab=expression(hat(p)),mgp=c(2.65,1,0))
axis(side=1,at=c(1,481,961,1441,1921,n-24),labels=c(593,603,613,623,633,641))
#axis(side=2,at=c(0,0.0004,0.0008,0.0012),labels = c(0,0.4,0.8,1.2))
dev.off()

plot(density(p_est),main="",xlab = expression(hat(p)))


hist(p_est,main = "",xlab=expression(hat(p)))
ggplot(qwe,aes(qwe$p_est)) + geom_histogram(fill="salmon") + labs(x=expression(hat(p)),y="Frequency")
