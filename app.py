import streamlit as st
import base64
import pandas as pd
import matplotlib.pyplot as plt

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Mood-Based Music Recommender", layout="wide")

# ---------- BACKGROUND IMAGE SETUP ----------
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

add_bg_from_local("train.jpg")

# ---------- CREDIT TOP RIGHT ----------
st.markdown(
    """
    <div style='text-align: right; margin-top: 10px; margin-bottom: -40px;'>
        <span style='color: red; font-size: 16px;'>❤</span> 
        <span style='color: white; font-size: 16px;'>By Abisha Jerlin</span>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- TITLE + SUBTITLE ----------
st.markdown(
    "<h1 style='text-align: center; color: white;'>Mood-Based Music Recommender</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h3 style='text-align: center; color: white;'>Explore songs that match your mood 🎶</h3>",
    unsafe_allow_html=True
)
st.markdown("##", unsafe_allow_html=True)

# ---------- MOOD SELECTION ----------
st.markdown("""
<style>
.mood-label {
    color: white;
    font-size: 20px;
    margin-bottom: -10px;
}
/* FIRST DROPDOWN: white box with black text inside and rounded corners */
div[data-baseweb="select"]:first-of-type {
    background-color: white !important;
    border-radius: 12px !important;
}
div[data-baseweb="select"]:first-of-type * {
    color: black !important;
    background-color: white !important;
}
</style>
<p class="mood-label">🎧 What's your current mood?</p>
""", unsafe_allow_html=True)

mood = st.selectbox("", ["Happy", "Sad", "Calm", "Energetic", "Angry"])

# ---------- PLAYLIST EMBED LINKS ----------
playlist_links = {
    "Happy": "https://open.spotify.com/embed/playlist/1AX6Qra1kWlCEG4fQiElYM?utm_source=generator",
    "Sad": "https://open.spotify.com/embed/playlist/7D4qnXXINGRUSs9z7OPZem?utm_source=generator",
    "Calm": "https://open.spotify.com/embed/playlist/6v6wP4ZhEkvFanwzrqpo36?utm_source=generator",
    "Energetic": "https://open.spotify.com/embed/playlist/3gh5JZzMwUlT4MbTZ88ilg?utm_source=generator",
    "Angry": "https://open.spotify.com/embed/playlist/5MhM8mvoKAGjb0NYEH2npI?utm_source=generator"
}

# ---------- EMBED THE PLAYLIST ----------
st.markdown(f"<h4 style='color:white;'>💿 Songs that match your <u>{mood}</u> mood</h4>", unsafe_allow_html=True)

st.markdown(
    f"""
    <iframe style="border-radius:12px"  
    src="{playlist_links[mood]}"  
    width="100%" height="400" frameBorder="0" allowfullscreen=""  
    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"  
    loading="lazy"></iframe>
    """,
    unsafe_allow_html=True
)

# ---------- MOOD METRICS INFO ----------
st.markdown("""
<style>
.tooltip {
  color: white;
  position: relative;
  display: inline-block;
  cursor: pointer;
  font-size: 16px;
}
.tooltip .tooltiptext {
  visibility: hidden;
  background-color: #333;
  color: white;
  text-align: left;
  border-radius: 6px;
  padding: 10px 15px;
  position: absolute;
  z-index: 1;
  top: 120%;
  left: 0;
  opacity: 0;
  transition: opacity 0.3s;
  white-space: nowrap;
}
.tooltip:hover .tooltiptext {
  visibility: visible;
  opacity: 1;
}
</style>
<div class="tooltip">💭 Mood Metrics Info
  <div class="tooltiptext">
    Valence: How happy or sad a song sounds → High = Cheerful, Low = Melancholic.<br>
    Energy: Intensity of the song → High = Powerful, Low = Calm.
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- LOAD DATA ----------
df = pd.read_csv("105 songs.csv")

# ---------- GLOBAL STYLING ----------
st.markdown("""
<style>
.stCheckbox > div > label {
    color: white !important;
}
.row-widget.stCheckbox > label > div {
    color: white !important;
}
.stSelectbox label {
    color: white !important;
}
/* SECOND DROPDOWN: fully black with white text & rounded corners */
div[data-baseweb="select"]:not(:first-of-type) {
    background-color: black !important;
    border-radius: 12px !important;
}
div[data-baseweb="select"]:not(:first-of-type) * {
    color: white !important;
    background-color: black !important;
}
.stApp {
    background-color: #0e0e0e;
}
</style>
""", unsafe_allow_html=True)

# ---------- CHECKBOX AND UPDATED PLOT ----------
show_mood_checkbox = st.checkbox("📊 Visualizing the feel and flow of music")

if show_mood_checkbox:
    st.markdown("""
    <style>
        div[data-baseweb="select"]:nth-of-type(2) {
            background-color: black !important;
            border-radius: 12px !important;
        }
        div[data-baseweb="select"]:nth-of-type(2) * {
            color: white !important;
            background-color: black !important;
        }
    </style>
    """, unsafe_allow_html=True)

    moods = df["Mood"].unique()
    selected_mood = st.selectbox(
        "",
        options=list(moods),
        index=None,
        placeholder="Select your mood to visualize"
    )

    if selected_mood:
        filtered_df = df[df["Mood"] == selected_mood].reset_index(drop=True)

        plt.style.use("dark_background")
        fig, ax = plt.subplots(figsize=(10, 6))

        # Combined Scatter plot for Valence and Energy
        ax.scatter(filtered_df.index, filtered_df['Valence'], color='skyblue', label='Valence (Happiness)', s=60)
        ax.scatter(filtered_df.index, filtered_df['Energy'], color='orange', label='Energy (Intensity)', s=60)

        ax.set_xlabel("Song Index", color="white")
        ax.set_ylabel("Value", color="white")
        ax.set_title(f"Valence & Energy - {selected_mood} Mood", color="white")
        ax.tick_params(colors='white')
        ax.grid(True, linestyle='--', alpha=0.3)
        ax.legend(facecolor='black', edgecolor='white', labelcolor='white')

        st.pyplot(fig)
