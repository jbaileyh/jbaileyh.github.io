# R packages used by the posts. Run once with:  Rscript install.R
pkgs <- c("rmarkdown", "knitr", "ggplot2", "downlit", "xml2")
missing <- setdiff(pkgs, rownames(installed.packages()))
if (length(missing)) install.packages(missing, repos = "https://cloud.r-project.org")
