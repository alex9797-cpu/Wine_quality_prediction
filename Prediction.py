import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


# Import data
wine_data=pd.read_csv(filepath_or_buffer="winequalityN.csv")


# Start with prediction only for the red wines:
wine_red=wine_data[wine_data['type']=='red']

# Omit type Varaible:

wine_red=wine_red.drop(columns='type',axis=1)


' Change Labels and  train test split'

wine_red=wine_red.dropna()

X=wine_red.drop(columns='quality',axis=1)
y=wine_red['quality']
# Changt to binary categorical output:
y_bin=[1 if val >=7 else 0 for val in y]

X_train, X_test, y_train, y_test = train_test_split(X, y_bin, test_size=0.33, random_state=42)

' Data Prepocessing steps'


scaler=StandardScaler()

# Scale Training set
X_train=scaler.fit_transform(X_train)
# Scale Test set
X_test=scaler.fit_transform(X_test)


' Fit Model and evaluate model'

# Fit Naive Bayes and Test it
gnb = GaussianNB()
gnb.fit(X_train,y_train)

# Compute predictions
y_pred=gnb.predict(X_test)
# Print accuracy:
print(f' Naive Bayes Accuarcy Scoee: {accuracy_score(y_test,y_pred)}')


































































