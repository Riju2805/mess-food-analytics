import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Mess Food Analytics", layout="wide")

# 🔥 FULL UI FIX
st.markdown("""
<style>

/* Remove top black bar */
header {visibility: hidden;}
footer {visibility: hidden;}

/* Main background */
[data-testid="stAppViewContainer"] {
    background-color: #F5F1E8;
    color: #4E342E;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #EADFD3;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: #5D4037 !important;
}
            
/* Selected tags (Mon, Tue, etc.) */
span[data-baseweb="tag"] {
    background-color: #D7CCC8 !important;  /* soft brown */
    color: #4E342E !important;            /* dark brown text */
    border-radius: 8px !important;
    padding: 4px 8px !important;
}

/* Remove red cross icon color */
span[data-baseweb="tag"] svg {
    color: #4E342E !important;
}

/* Titles */
h1, h2, h3 {
    color: #5D4037;
}

/* Center content spacing */
.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center;'>🍽️ Mess Food Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#6D4C41;'>🤎 Cute insights into food, mood & vibes</p>", unsafe_allow_html=True)

st.markdown("---")

# Load data
conn = sqlite3.connect("mess.db")
df = pd.read_sql_query("SELECT * FROM meals", conn)
conn.close()

# Sidebar
st.sidebar.markdown("## 🎛️ Controls")

selected_day = st.sidebar.multiselect(
    "Select Day",
    df['day'].unique(),
    default=df['day'].unique()
)

selected_meal = st.sidebar.multiselect(
    "Select Meal",
    df['meal'].unique(),
    default=df['meal'].unique()
)

filtered_df = df[
    (df['day'].isin(selected_day)) &
    (df['meal'].isin(selected_meal))
]

# KPIs
col1, col2, col3 = st.columns(3)

col1.markdown(f"<h3 style='text-align:center;'>🍽️ Meals</h3><h2 style='text-align:center;'>{len(filtered_df)}</h2>", unsafe_allow_html=True)

col2.markdown(f"<h3 style='text-align:center;'>⭐ Avg Rating</h3><h2 style='text-align:center;'>{round(filtered_df['rating'].mean(),2)}</h2>", unsafe_allow_html=True)

col3.markdown(f"<h3 style='text-align:center;'>🍛 Variety</h3><h2 style='text-align:center;'>{filtered_df['food_item'].nunique()}</h2>", unsafe_allow_html=True)

st.markdown("---")

# 🎨 CUSTOM BEIGE CHARTS (NO BLACK, NO BLUE)

# Food Popularity
col1, col2 = st.columns(2)

with col1:
    st.subheader("🍛 Food Popularity")

    fig, ax = plt.subplots()
    filtered_df['food_item'].value_counts().plot(
        kind='bar',
        color='#A1887F',
        ax=ax
    )
    ax.set_facecolor('#F5F1E8')
    fig.patch.set_facecolor('#F5F1E8')
    ax.tick_params(colors='#5D4037')
    ax.set_xlabel("")
    ax.set_ylabel("")
    st.pyplot(fig)

# Avg Rating
with col2:
    st.subheader("⭐ Avg Rating per Food")

    avg = filtered_df.groupby('food_item')['rating'].mean()

    fig, ax = plt.subplots()
    avg.plot(
        kind='bar',
        color='#8D6E63',
        ax=ax
    )
    ax.set_facecolor('#F5F1E8')
    fig.patch.set_facecolor('#F5F1E8')
    ax.tick_params(colors='#5D4037')
    ax.set_xlabel("")
    ax.set_ylabel("")
    st.pyplot(fig)

st.markdown("---")

# Satisfaction
st.subheader("😊 Satisfaction Distribution")

fig, ax = plt.subplots()
filtered_df['satisfaction'].value_counts().plot(
    kind='bar',
    color='#BCAAA4',
    ax=ax
)
ax.set_facecolor('#F5F1E8')
fig.patch.set_facecolor('#F5F1E8')
ax.tick_params(colors='#5D4037')
ax.set_xlabel("")
ax.set_ylabel("")
st.pyplot(fig)

st.markdown("---")

# Table
st.subheader("📋 Dataset")
st.dataframe(filtered_df, use_container_width=True)