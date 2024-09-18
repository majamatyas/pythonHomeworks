import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

file_path = 'dane.xlsx' 
df = pd.read_excel(file_path)

array_1 = df.iloc[:, 0].to_numpy()  
array_2 = df.iloc[:, 1].to_numpy()  
array_3 = df.iloc[:, 2].to_numpy()  
array_4 = df.iloc[:, 3].to_numpy()  
array_5 = df.iloc[:, 4].to_numpy()  
array_6 = df.iloc[:, 5].to_numpy()  
array_7 = df.iloc[:, 6].to_numpy()  

df_arrays = pd.DataFrame({
    'Maternal age': array_1,
    'Maternal BMI': array_2,
    'ChildBMI': array_3,
    'CORTsal': array_4,
    'CORTmilk': array_5,
    'PRLmilk': array_6,
    'PRLsal': array_7
})

X = df_arrays[['CORTmilk', 'PRLmilk', 'PRLsal', 'ChildBMI', 'Maternal BMI']]
y = df_arrays['CORTsal']

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)

plt.figure(figsize=(12, 6))
sns.scatterplot(x=y, y=predictions, color='blue', label='Predictions', alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='darkblue', linestyle='--', label='Perfect Fit')
plt.title('Dependency ')
plt.xlabel('CORTsal')
plt.ylabel('Predicted Values')
plt.legend()
plt.grid(True)
plt.show()
