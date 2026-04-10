import pandas as pd
import random

data = [
    ["Monday", "Breakfast", "Idli", "Veg"],
    ["Monday", "Lunch", "Aloo Mutter", "Veg"],
    ["Monday", "Dinner", "Kadhai Mix Veg", "Veg"],

    ["Tuesday", "Breakfast", "Poha", "Veg"],
    ["Tuesday", "Lunch", "White Chana", "Veg"],
    ["Tuesday", "Dinner", "Paneer Masala", "Veg"],

    ["Wednesday", "Breakfast", "Upma", "Veg"],
    ["Wednesday", "Lunch", "Dal Tadka", "Veg"],
    ["Wednesday", "Dinner", "Egg Curry", "Non-Veg"],

    ["Thursday", "Breakfast", "Paratha", "Veg"],
    ["Thursday", "Lunch", "Rajma Rice", "Veg"],
    ["Thursday", "Dinner", "Chicken Curry", "Non-Veg"],

    ["Friday", "Breakfast", "Dalia", "Veg"],
    ["Friday", "Lunch", "Dal Fry", "Veg"],
    ["Friday", "Dinner", "Mix Veg", "Veg"],

    ["Saturday", "Breakfast", "Upma", "Veg"],
    ["Saturday", "Lunch", "Ghee Rice", "Veg"],
    ["Saturday", "Dinner", "Veg Pulao", "Veg"],

    ["Sunday", "Breakfast", "Uttapam", "Veg"],
    ["Sunday", "Lunch", "Veg Biryani", "Veg"],
    ["Sunday", "Dinner", "Aloo Masala", "Veg"]
]

final_data = []

for row in data:
    day, meal, food, category = row

    # Simulate multiple student responses
    for _ in range(15):  # 15 students per meal
        if meal == "Dinner":
            taste = random.choice([2, 3, 3, 4])
        else:
            taste = random.choice([3, 4, 4, 5])

        hygiene = random.choice([2, 3, 4, 5])
        variety = random.choice([2, 3, 4, 5])
        overall = round((taste + hygiene + variety) / 3)

        final_data.append([day, meal, food, category, taste, hygiene, variety, overall])

df = pd.DataFrame(final_data, columns=[
    "Day", "Meal", "Food", "Category",
    "Taste", "Hygiene", "Variety", "Overall"
])

df.to_csv("mess_data.csv", index=False)

print("Realistic mess dataset created!")