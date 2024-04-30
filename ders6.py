import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#veri yükleme
veriler = pd.read_csv("eksikveriler.csv")

#eksik veri
from sklearn.impute import SimpleImputer
imputer= SimpleImputer(missing_values=np.nan,strategy="mean")
