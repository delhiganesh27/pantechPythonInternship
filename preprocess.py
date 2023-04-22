import pandas as pd
import numpy as np
df = pd.read_csv('train.csv')
df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
required_features = df[['Survived', 'Pclass', 'Sex',
                        'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
required_features.to_csv('titanic_required_features.csv', index=False)
print('CSV File Updated.')
print('\nSample output:')
print(required_features.head())
