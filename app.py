import streamlit as st
import pandas as pd
import plotly.express as px

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Smart Mess Analytics", layout="wide")

# ================= LOAD DATA =================
df = pd.read_csv("mess_data.csv")

# ================= DAY ORDER FIX =================
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df["Day"] = pd.Categorical(df["Day"], categories=day_order, ordered=True)

# ================= TITLE =================
st.title("🍽️ Smart Mess Analytics System")
st.caption("Data-driven insights for improving food quality")

st.markdown("""
### 📌 Problem Statement  
Mess food quality varies across days and meals, and feedback is often unstructured.  
This system analyzes food ratings to identify patterns and support better decision-making.
""")

# ================= SIDEBAR FILTERS =================
st.sidebar.title("🔍 Filters")

selected_day = st.sidebar.selectbox("Select Day", ["All"] + day_order)
selected_meal = st.sidebar.selectbox("Select Meal", ["All"] + sorted(df["Meal"].unique()))
selected_category = st.sidebar.selectbox("Category", ["All"] + sorted(df["Category"].unique()))

# Apply filters
filtered_df = df.copy()

if selected_day != "All":
    filtered_df = filtered_df[filtered_df["Day"] == selected_day]

if selected_meal != "All":
    filtered_df = filtered_df[filtered_df["Meal"] == selected_meal]

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]

# ================= KEY METRICS =================
st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

avg_rating = round(filtered_df["Overall"].mean(), 2)

try:
    best_food = filtered_df.groupby("Food")["Overall"].mean().idxmax()
    worst_food = filtered_df.groupby("Food")["Overall"].mean().idxmin()
except:
    best_food = "N/A"
    worst_food = "N/A"

col1.metric("⭐ Avg Rating", avg_rating)
col2.metric("🏆 Best Food", best_food)
col3.metric("⚠️ Worst Food", worst_food)
col4.metric("📦 Total Reviews", len(filtered_df))

# ================= QUALITY SCORE =================
st.subheader("📊 Food Quality Score")

filtered_df["Quality Score"] = (
    filtered_df["Taste"] * 0.4 +
    filtered_df["Hygiene"] * 0.4 +
    filtered_df["Variety"] * 0.2
)

avg_score = round(filtered_df["Quality Score"].mean(), 2)
st.metric("Overall Quality Score", avg_score)

# ================= DISTRIBUTION =================
st.subheader("📈 Rating Distribution")

fig1 = px.histogram(filtered_df, x="Overall", nbins=5,
                    color_discrete_sequence=["#636EFA"])
st.plotly_chart(fig1, use_container_width=True)

# ================= MEAL ANALYSIS =================
st.subheader("🍛 Meal-wise Performance")

meal_avg = filtered_df.groupby("Meal")["Overall"].mean().reset_index()
fig2 = px.bar(meal_avg, x="Meal", y="Overall", color="Meal",
              text=meal_avg["Overall"].round(2),
              color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig2, use_container_width=True)

# ================= FOOD ANALYSIS =================
st.subheader("🍽️ Food-wise Ratings")

food_avg = filtered_df.groupby("Food")["Overall"].mean().sort_values().reset_index()

fig3 = px.bar(food_avg, x="Overall", y="Food", orientation="h",
              color="Overall",
              color_continuous_scale="RdYlGn")
st.plotly_chart(fig3, use_container_width=True)

# ================= CATEGORY =================
st.subheader("🥦 Veg vs Non-Veg")

cat_avg = filtered_df.groupby("Category")["Overall"].mean().reset_index()
fig4 = px.pie(cat_avg, names="Category", values="Overall",
              color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig4, use_container_width=True)

# ================= DAY TREND =================
st.subheader("📅 Day-wise Trend")

day_avg = filtered_df.groupby("Day")["Overall"].mean().reset_index()
day_avg = day_avg.sort_values("Day")

fig5 = px.line(day_avg, x="Day", y="Overall", markers=True)
st.plotly_chart(fig5, use_container_width=True)

# ================= RECOMMENDATION =================
st.subheader("🤖 Recommended Foods")

recommended = filtered_df.groupby("Food")["Overall"].mean().sort_values(ascending=False).head(3)

for i, food in enumerate(recommended.index):
    st.success(f"{i+1}. {food}")

# ================= CONSISTENCY =================
st.subheader("📊 Food Consistency Analysis")

consistency = filtered_df.groupby("Food")["Overall"].std().sort_values()

st.write("🟢 Most Consistent Foods:")
st.write(consistency.head(3))

st.write("🔴 Most Inconsistent Foods:")
st.write(consistency.tail(3))

# ================= ALERT SYSTEM =================
st.subheader("🚨 Alerts")

low_food = filtered_df.groupby("Food")["Overall"].mean()

for food, rating in low_food.items():
    if rating < 3:
        st.error(f"{food} is performing poorly!")

# ================= SMART INSIGHTS =================
st.subheader("🧠 Smart Insights")

if filtered_df["Hygiene"].mean() < 3.5:
    st.warning("⚠️ Hygiene ratings are below average. Improvement needed.")

if not filtered_df.empty:
    st.info(f"📉 Lowest performing meal: {filtered_df.groupby('Meal')['Overall'].mean().idxmin()}")

if not filtered_df.empty:
    st.success(f"📈 Best performing meal: {filtered_df.groupby('Meal')['Overall'].mean().idxmax()}")

# ================= PREDICTION =================
st.subheader("🔮 Predict Food Rating")

taste = st.slider("Taste", 1, 5, 3)
hygiene = st.slider("Hygiene", 1, 5, 3)
variety = st.slider("Variety", 1, 5, 3)

predicted = round((taste + hygiene + variety) / 3, 2)
st.success(f"Predicted Rating: {predicted}")

# ================= USER FEEDBACK =================
st.subheader("📝 Give Your Feedback")

user_rating = st.slider("Rate today's food", 1, 5, 3, key="feedback")

if st.button("Submit Feedback"):
    st.success(f"✅ Thanks! You rated it {user_rating}/5")

# ================= DATA PIPELINE =================
st.markdown("""
### 🔄 Data Pipeline

1. Data Collection → Mess menu + simulated feedback  
2. Data Processing → Cleaning & structuring using Pandas  
3. Analysis → Pattern detection & aggregation  
4. Visualization → Interactive dashboard  
5. Insights → Recommendations & alerts  

👉 This mimics real-world AI/LLM data pipelines.
""")

# ================= CONCLUSION =================
st.markdown("""
### ✅ Conclusion

- Hygiene is the most critical area for improvement  
- Dinner meals tend to underperform  
- Certain dishes consistently receive lower ratings  
- Data-driven decisions can significantly improve food quality  
""")