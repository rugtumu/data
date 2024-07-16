import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as sty
import plotly.express as px
import seaborn as sns

df = pd.read_csv('product_sales.csv')
df.info()
print(df)