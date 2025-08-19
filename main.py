import streamlit as st

# --- HEADER ---
st.set_page_config(page_title="My Portfolio", page_icon=":wave:", layout="wide")
st.title("👋 Hi, I'm [Your Name]")
st.subheader("Machine Learning Engineer | Data Scientist | AI Enthusiast")
st.write("Welcome to my portfolio! 🚀 Here you’ll find my projects, skills, and experience.")

# --- ABOUT ME ---
st.header("About Me")
st.write("""
I am a Machine Learning Engineer passionate about building AI-powered applications.
My expertise includes Python, ML, DL, and data analytics.
""")

# --- SKILLS ---
st.header("Skills")
st.write("""
- 🐍 Python, Pandas, NumPy  
- 🤖 Machine Learning (Scikit-learn, TensorFlow, PyTorch)  
- 📊 Data Visualization (Matplotlib, Seaborn, Plotly)  
- 🌐 Streamlit, Flask, FastAPI  
""")

# --- PROJECTS ---
st.header("Projects")
st.markdown("### 📌 [Sentiment Analysis App](https://github.com/sbmshukla/sentiment-analysis-app)")
st.write("Built a machine learning model to analyze sentiment in text and deployed it on Streamlit.")

st.markdown("### 📌 [Image Classifier](https://github.com/yourusername/image-classifier)")
st.write("Deep learning-based image classifier using TensorFlow and CNNs.")

# --- CONTACT ---
st.header("Contact Me")
st.write("📧 Email: sbmshukla@gmail.com")
st.write("🌐 LinkedIn: [Your Profile](https://linkedin.com/in/sbmhukla)")
st.write("💻 GitHub: [Your Repos](https://github.com/sbmshukla)")