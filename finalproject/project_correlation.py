import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'dane.xlsx' 
df = pd.read_excel(file_path)

col1 = df.iloc[:, 0].tolist()
col2 = df.iloc[:, 1].tolist()
col3 = df.iloc[:, 2].tolist()
col4 = df.iloc[:, 3].tolist()
col5 = df.iloc[:, 4].tolist()
col6 = df.iloc[:, 5].tolist()
col7 = df.iloc[:, 6].tolist()


data = pd.DataFrame({
    'Maternal age': col1,
    'Maternal BMI': col2,
    'ChildBMI': col3,
    'CORTsal': col4,
    'CORTmilk': col5,
    'PRLmilk': col6,
    'PRLsal': col7
})


correlation_matrix = data.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation')
plt.xticks(rotation=0)
plt.show()