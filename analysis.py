import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("mess_data.csv")

# Set style
sns.set()

print("\n===== BASIC INFO =====\n")
print(df.head())

# ===== TEXT INSIGHTS =====

# Average ratings
print("\n===== OVERALL RATINGS =====\n")
print(df[["Taste", "Hygiene", "Variety", "Overall"]].mean())

# Meal-wise
print("\n===== MEAL-WISE RATINGS =====\n")
print(df.groupby("Meal")[["Taste", "Overall"]].mean())

# Day-wise
print("\n===== DAY-WISE RATINGS =====\n")
print(df.groupby("Day")["Overall"].mean())

# Food-wise
print("\n===== FOOD-WISE RATINGS =====\n")
print(df.groupby("Food")["Overall"].mean().sort_values())

# Category-wise
print("\n===== CATEGORY ANALYSIS =====\n")
print(df.groupby("Category")["Overall"].mean())

# Best & Worst food
worst_food = df.groupby("Food")["Overall"].mean().idxmin()
best_food = df.groupby("Food")["Overall"].mean().idxmax()

print("\nWorst Food Item:", worst_food)
print("Best Food Item:", best_food)

# ===== VISUALIZATION =====

# 1. Average Ratings
plt.figure(figsize=(8,5))
avg = df[["Taste", "Hygiene", "Variety", "Overall"]].mean()

avg.plot(kind='bar', color=['#4CAF50', '#F44336', '#2196F3', '#FF9800'])

plt.title("Average Ratings of Mess Food", fontsize=14)
plt.ylabel("Rating (out of 5)")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 2. Meal-wise Ratings
plt.figure(figsize=(8,5))
df.groupby("Meal")["Overall"].mean().plot(kind='bar', color='skyblue')

plt.title("Meal-wise Satisfaction")
plt.ylabel("Rating")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 3. Food-wise Ratings (BEST GRAPH 🔥)
plt.figure(figsize=(10,6))
food_avg = df.groupby("Food")["Overall"].mean().sort_values()

food_avg.plot(kind='barh', color='purple')

plt.title("Food-wise Overall Ratings")
plt.xlabel("Rating")
plt.ylabel("Food Items")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# 4. Veg vs Non-Veg
plt.figure(figsize=(6,4))
df.groupby("Category")["Overall"].mean().plot(kind='bar', color=['green','red'])

plt.title("Veg vs Non-Veg Ratings")
plt.ylabel("Rating")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()