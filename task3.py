import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"D:\Movies\Downloads\cleaned_student_dataset.csv")

print(data.head())

print(data.info())
print(data.describe())

print(data.isnull().sum())

sns.histplot(data['Marks'], kde=True)
plt.title("Marks Distribution")
plt.show()

sns.countplot(x='Course', data=data)
plt.title("Students per Course")
plt.show()

sns.scatterplot(x='Attendance (%)', y='Marks', data=data)
plt.title("Attendance vs Marks")
plt.show()

corr = data.corr(numeric_only=True)

sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()

sns.boxplot(x=data['Marks'])
plt.title("Outliers in Marks")
plt.show()