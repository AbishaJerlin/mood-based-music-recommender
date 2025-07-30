# 🎵 Mood-Based Music Recommendation System

A fun, interactive project that recommends songs based on your mood
---

## 🧠 Why I Created This Project

I suddenly had a thought:  
**“How can we track or recommend music from our playlist based on our mood?”**

Initially, I tried using the **Spotify API** to fetch mood-based playlists dynamically. However, due to the need for **user authentication via OAuth2** and limitations in accessing live playlists, I decided to take a different approach.

So, I manually **created** a **custom dataset of 105 songs**, with **21 songs** for each mood. This gave me full control over:

- The mood tagging process  
- The recommendation logic  
- The user experience through visualizations and the frontend interface  

This project explores how **music and emotions** can be meaningfully connected using data science.

---

## 🖼️ App Preview



## 🔄 Workflow Overview

#### 📌 PHASE 1: Data Preparation
- Created a dataset of 105 songs (21 for each mood).
- Added mood tags and relevant metrics (valence, energy).

#### 💻 PHASE 2: Jupyter Notebook (Backend Logic)
- Cleaned and explored the dataset.
- Built logic for filtering and recommending songs based on mood.
- Created mood-based visualizations.

#### 🌐 PHASE 3: Streamlit App (Frontend)
- Developed an interactive web app using Streamlit.
- Users can select their mood and view recommendations.
- Mood-based plots (Valence & Energy) are available via toggle.

#### 🎧 PHASE 4: Spotify Embedded
- Created **Spotify playlists** for each mood and embedded them in the app.
- Users can **listen to the songs directly** from within the app.

---

## 💡 Features

- 🎯 Mood selection: *Happy*, *Sad*, *Calm*, *Energetic*, *Angry*
- 💿 Embedded Spotify playlists for each mood
- 📊 Visualize mood metrics like **Valence** (happiness) and **Energy** (intensity)
- 🎨 Beautiful UI with custom background and hover tooltips

---

## 🛠️ Tech Stack

- **Python**
- **Pandas** – Data manipulation
- **Jupyter Notebook** – Backend logic
- **Streamlit** – Web interface
- **Matplotlib** – Visualizations

---

## 🚀 How to Run This Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/mood-based-music-recommender.git
   cd mood-based-music-recommender
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
4. **Run the App**
   ```bash
   streamlit run app.py
   
---

## 📁 Folder Structure

```text
mood-based-music-recommender/
├── 📊 data/
│   └── songs_dataset.csv
├── 📓 notebooks/
│   └── mood_recommender.ipynb
├── 🖼️ images/
│   └── preview_screenshots.png
├── app.py
├── requirements.txt
└── README.md
```

---

🙋‍♀️ Made with ❤️ by Abisha Jerlin
---
Feel the music, live the mood 🎶
