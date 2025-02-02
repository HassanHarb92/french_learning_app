import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("stories.csv")  # Make sure to upload and use your CSV file here

# Load stories
df = load_data()

# Create a list of unique story titles
story_titles = df["Title (French)"].unique()

# Streamlit app title
st.title("📖 French-English Short Stories")

# Dropdown to select a story
selected_title = st.selectbox("Choisissez une histoire / Choose a story", story_titles)

# Filter the dataframe based on selected title
selected_story = df[df["Title (French)"] == selected_title]

# Display the story
st.subheader(selected_title)
st.write("### **French & English Lines**")

for _, row in selected_story.iterrows():
    st.markdown(f"**🇫🇷 {row['French Line']}**")
    st.markdown(f"*🇬🇧 {row['English Translation']}*\n")

# Add a note
st.write("💡 Use this app to practice reading and comprehension in French!")

