# 📪 AI Social Post Repurposer

Transform your blogs, newsletters, or articles into **platform-ready social media posts** in seconds using **Mistral AI** 🚀  

[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Mistral AI](https://img.shields.io/badge/AI-Mistral%20API-8A2BE2?logo=openai&logoColor=white)](https://mistral.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Deploy](https://img.shields.io/badge/Deployed%20on-Streamlit%20Cloud-FF4B4B?logo=streamlit&logoColor=white)](https://social-media-posts-7.streamlit.app/)

---

## ✨ Features
- 📝 Paste any **long-form content** (blogs, reports, newsletters, etc.)
- 🌐 Generate posts tailored for **Twitter, LinkedIn, Instagram, and more**
- 🎭 Customize **tone** (formal, witty, casual, professional)
- 📏 Adjust **length** (short, medium, long)
- 🎨 Control **creativity** with temperature slider
- 📥 Export results as **CSV** or **JSON**
- ⚡ Powered by **Mistral AI**

---

## 📂 Project Structure
```bash
social-posts/
│
├── app.py # Streamlit UI
├── requirements.txt # Dependencies
├── .env # API Key 
│
├── src/ # Core logic
│ ├── init.py
│ ├── generator.py # Mistral API calls
│ └── styles.py # Platform-specific style templates
│
├── utils/ # Helpers
│ ├── init.py
│ └── file_utils.py # Save/export functions
│
├── data/ # Sample input
│ └── sample_blog.txt
│
└── outputs/ # Generated posts
├── posts.json
└── posts.csv
```

---

## ⚙️ Setup & Installation

### 1. Clone this repo
```bash
git clone https://github.com/msravanthi674/social-media-posts.git
cd social-posts
```
2. Create & activate environment (using conda)
```bash
conda create -n social-posts python=3.9 -y
conda activate social-posts
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Add your Mistral API key

Create a .env file in the project root:
```bash
MISTRAL_API_KEY=your_api_key_here
```
5. Run the app locally
```bash
streamlit run app.py
```
## 🔮 Future Improvements

- 📌 Add multi-post variations per platform
- 🎤 Support voice input for content drafting
- 📊 Show character/word counts (esp. for Twitter)
- ⏰ Schedule posts directly to platforms
