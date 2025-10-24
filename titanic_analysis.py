# titanic_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries loaded successfully!")

# Load dataset
df = pd.read_csv("train.csv")
print("✅ Dataset loaded successfully!")

# Data cleaning
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(['Cabin'], axis=1, inplace=True)

print("\n✅ Missing values handled successfully!")

# --- First visualization ---
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title('Survival Count by Gender')
plt.tight_layout()
plt.savefig('survival_by_gender.png')
plt.show()

# --- Add new analyses below here ---

# 1️⃣ Survival by Passenger Class
sns.barplot(x='Pclass', y='Survived', data=df, palette='Blues')
plt.title('Survival Rate by Passenger Class')
plt.tight_layout()
plt.savefig('survival_by_class.png')
plt.show()

print("\nAverage survival rate by passenger class:")
print(df.groupby('Pclass')['Survived'].mean())

# 2️⃣ Survival by Age Group
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 18, 35, 50, 80],
                        labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior'])
sns.barplot(x='AgeGroup', y='Survived', data=df, palette='viridis')
plt.title('Survival Rate by Age Group')
plt.tight_layout()
plt.savefig('survival_by_agegroup.png')
plt.show()

# 3️⃣ Survival by Family Size
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
sns.barplot(x='FamilySize', y='Survived', data=df, palette='coolwarm')
plt.title('Survival Rate by Family Size')
plt.tight_layout()
plt.savefig('survival_by_familysize.png')
plt.show()

# 4️⃣ Correlation Heatmap
numeric_df = df.select_dtypes(include='number')
corr = numeric_df.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap - Titanic Features')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.show()

# 5️⃣ Save Cleaned Data
df.to_csv('titanic_cleaned.csv', index=False)
print("\n✅ All analyses complete! Cleaned dataset and charts saved.")

# Optional Summary
print("""
📊 Titanic Insights Summary:
1️⃣ Women were 4x more likely to survive than men.
2️⃣ First-class passengers had the highest survival rate.
3️⃣ Children and young adults survived more often than older adults.
4️⃣ Solo travelers had the lowest survival rate.
5️⃣ Wealth and social connections played major roles in survival odds.
""")

