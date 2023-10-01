# visualization redesign

import pandas as pd
import altair as alt

url_path = 'https://raw.githubusercontent.com/kemiolamudzengi/dsci-320-datasets/main/tinder.csv'
data = pd.read_csv(url_path)
data.head(10)
