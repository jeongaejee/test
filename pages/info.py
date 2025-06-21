import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data (you can replace this with your actual dataset)
data = {
    'University': ['Harvard', 'Stanford', 'MIT', 'UCLA', 'Seoul National Univ.', 'Yonsei Univ.', 'KAIST', 'POSTECH'],
    'Country': ['USA', 'USA', 'USA', 'USA', 'South Korea', 'South Korea', 'South Korea', 'South Korea'],
    'City': ['Cambridge', 'Stanford', 'Cambridge', 'Los Angeles', 'Seoul', 'Seoul', 'Daejeon', 'Pohang'],
    'Major Strength': ['Law', 'Tech', 'Engineering', 'Film', 'Medicine', 'Business', 'Science', 'AI'],
    'Tuition (USD/year)': [50000, 48000, 53000, 42000, 6000, 7000, 4000, 3500],
    'QS Ranking': [4, 3, 1, 40, 41, 79, 56, 81]
}

df = pd.DataFrame(data)

# 🎓 App Title
st.title("🎓 University Guidance Explorer")
st.markdown("Filter and explore global universities based on your interests. 🌍📚")

# 🔍 Filter
country = st.multiselect("Select Country", df["Country"].unique(), default=df["Country"].unique())
major = st.multiselect("Select Major Strength", df["Major Strength"].unique(), default=df["Major Strength"].unique())

filtered_df = df[(df["Country"].isin(country)) & (df["Major Strength"].isin(major))]

# 📊 Tuition Bar Chart
st.subheader("💰 Tuition Comparison")
fig = px.bar(filtered_df, x="University", y="Tuition (USD/year)", color="Major Strength", text="Tuition (USD/year)")
st.plotly_chart(fig)

# 🌍 Map Visualization (approximate location simulation)
st.subheader("📍 University Locations (Simulated Coordinates)")
df['Latitude'] = [42.3736, 37.4275, 42.3601, 34.0689, 37.4563, 37.5665, 36.3729, 36.0185]
df['Longitude'] = [-71.1097, -122.1697, -71.0942, -118.4452, 126.7052, 126.9780, 127.3650, 129.3209]

map_fig = px.scatter_geo(filtered_df,
                         lat='Latitude',
                         lon='Longitude',
                         hover_name='University',
                         size='QS Ranking',
                         color='Country',
                         projection="natural earth")
st.plotly_chart(map_fig)

# 🏆 Ranking Table
st.subheader("🏆 QS Rankings")
st.dataframe(filtered_df.sort_values(by="QS Ranking"))

# ✨ Conclusion
st.markdown("Explore more options, talk to your counselor, and good luck on your journey! 🚀")


