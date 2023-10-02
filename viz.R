# install.packages("ggplot2")
# install.packages("readr")
# install.packages("dplyr")
library(ggplot2)
library(readr)
library(dplyr)
library(tidyverse)

data = read_csv("https://raw.githubusercontent.com/yuwangy/uk_spending_viz/main/Government%20spending%202010-11%20-%20TOTALS.csv")
head(data)

new_data <- data[-c(1,2),] |>
  rename(
   spending = ...2
  )

head(new_data)

bar_plot <- ggplot(data = new_data, aes(x = `UK SPENDING 2010-11`, 
                                        y = spending)) +
  geom_bar(stat="identity", fill = "blue") +
  ggtitle("Plot of Department Spending 2010-11") +
  xlab("Department section") +
  ylab("Spending") +
  theme(axis.text.x = element_text(hjust = 15)) +
  scale_fill_gradient(low="lightblue", high="blue")

bar_plot





