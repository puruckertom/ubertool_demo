library(sensitivity) 
library(boot)

# You can also set your own working directory
# setwd('your/own/path')

n <- 1000
X1 <- data.frame(matrix(runif(8 * n), nrow = n))
X2 <- data.frame(matrix(runif(8 * n), nrow = n))

# sensitivity analysis
x <- sobol2002(model = sobol.fun, X1, X2, nboot = 100)

pdf("Fig1.pdf")
  plot(x)
dev.off()






















