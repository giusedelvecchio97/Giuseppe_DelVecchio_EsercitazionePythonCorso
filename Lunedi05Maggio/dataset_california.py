from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.datasets import load_boston

california = fetch_california_housing(as_frame=True)
housing = california.frame
housing.head()
boston = load_boston()
print(boston.DESCR)
