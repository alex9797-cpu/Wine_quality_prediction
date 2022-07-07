import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

wine_data=pd.read_csv(filepath_or_buffer="winequalityN.csv")

n_row=wine_data.shape[0]
n_col=wine_data.shape[1]

print(f"The Dataset contains {n_row} Observations and {n_col} Variables")

' Split up into red and white wine'
wine_red = wine_data[wine_data['type']=='red']
wine_white = wine_data[wine_data['type']=='white']

' Creates histogramms for the wine quality variable'

plt.hist(wine_red['quality'])
plt.xlabel("Data")
plt.ylabel("Frequency")
plt.title("Histogram wine quality red")
plt.show()

plt.hist(wine_white['quality'])
plt.xlabel("Data")
plt.ylabel("Frequency")
plt.title("Histogram wine quality white")
plt.show()



# PLot correlation matrices for both wines:
corr_mat_red=wine_red.iloc[:,1:11].corr()

sns.heatmap(corr_mat_red, xticklabels=corr_mat_red.columns,yticklabels=corr_mat_red.columns)
plt.show()

corr_mat_white=wine_white.iloc[:,1:11].corr()

sns.heatmap(corr_mat_white, xticklabels=corr_mat_red.columns,yticklabels=corr_mat_red.columns)
plt.show()











































