import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

wine_data=pd.read_csv(filepath_or_buffer="winequalityN.csv")

n_row=wine_data.shape[0]
n_col=wine_data.shape[1]


print(f"The Dataset contains {n_row} Observations and {n_col} Variables")








