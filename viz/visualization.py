# visualization redesign

import pandas as pd
import altair as alt

url_path = 'https://raw.githubusercontent.com/yuwangy/uk_spending_viz/main/Government%20spending%202010-11%20-%20TOTALS.csv'
data = pd.read_csv(url_path)
data.head(8)

data.shape
data.info()

# data filtering and cleaning
data = data.rename(columns = {'Unnamed: 1': '09_10_spending',
'Unnamed: 2': '10_11_spending'})
data.head(5)


bar_plot = alt.Chart(data).mark_bar().encode(
    alt.X('UK SPENDING 2010-11'),
    alt.Y('10_11_spending')
)

bar_plot


install.packages("ggplot2")
install.packages("readr")
install.packages("dplyr")
library(ggplot2)
library(readr)
library(dplyr)






