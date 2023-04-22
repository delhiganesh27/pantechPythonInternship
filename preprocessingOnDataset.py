import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Loading the dataset
train_data = pd.read_csv("train.csv")

print('check for null values')
columns = train_data.columns
for i in columns:
    print(f"{i} have {train_data[i].isnull().sum()} null values")
print("_"*60)
# fill the null values
train_data['Age'] = train_data['Age'].fillna(int(train_data['Age'].mean()))

train_data['Embarked'] = train_data['Embarked'].fillna(
    train_data['Embarked'].mode()[0])

# drop unnecessary columns
train_data = train_data.drop(columns=['Name', 'Ticket', 'Cabin'], axis=1)

print('check for null values after removing unwanted columns and filling null values')
columns = train_data.columns
for i in columns:
    print(f"{i} have {train_data[i].isnull().sum()} null values")
cols = ['Sex', 'Embarked']
encode = LabelEncoder()

for col in cols:
    train_data[col] = encode.fit_transform(train_data[col])
print("_"*60, "\nAfter preprocessing:")
print(train_data.head(15))
train_data.to_csv('submission.csv', index=False)
