## calculates temporal scedasis
rm(list=ls())
data1<- read.csv("SP500ret_88to07.csv", header=FALSE)

h=0.1
k=130
n= as.integer(nrow(data1))
ind <- data1[1:k,3]

s <- seq(1 / n, 1, 1 / n)	#seq(0.1, 0.9, lag)
hatc <- numeric(n)
arg <- outer(s, s, "-")
arg[(arg < -h) | (arg > h)] <- h #sets all values of arg that are greater or less than h or -h to be h.
arg <- 15 * (1 - (arg / h)^2)^2 / 16 # epanechnikov

hatc <- data.frame(s, colSums(arg[ind, ], na.rm=TRUE) / (k * h)) # evaluates G(arg) at the exceedances
names(hatc)<- c("t", "ct")



