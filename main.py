import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="sbmshukla | ML Engineer", page_icon="🤖", layout="wide")

# --- HEADER ---
st.title("🤖 Shubham Shukla")
st.subheader("Machine Learning Engineer | Data Scientist | AI Enthusiast")
st.write("🚀 I build and deploy data-driven solutions that turn raw data into intelligent applications.")

# --- ABOUT ME ---
st.header("👨‍💻 About Me")
st.write("""
I am a **Machine Learning Engineer** passionate about designing, training, and deploying AI-powered applications.  
With expertise in **end-to-end ML pipelines**, I specialize in:
- Data preprocessing & feature engineering  
- Supervised & unsupervised ML models  
- Deep learning architectures (CNNs, RNNs, Transformers)  
- Model deployment with Streamlit, Flask, FastAPI, and cloud platforms  
""")

# --- SKILLS ---
st.header("🛠️ Core Skills")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("✅ **Programming**: Python, SQL, C++")
    st.markdown("✅ **Libraries**: NumPy, Pandas, Scikit-learn")
with col2:
    st.markdown("✅ **Deep Learning**: TensorFlow, PyTorch")
    st.markdown("✅ **NLP**: Transformers, HuggingFace, spaCy")
with col3:
    st.markdown("✅ **Deployment**: Streamlit, Flask, FastAPI, Docker")
    st.markdown("✅ **Visualization**: Matplotlib, Seaborn, Plotly")

# --- PROJECTS ---
st.header("📂 Featured Projects")
tab1, tab2, tab3, tab4 = st.tabs([
    "📌 Sentiment Analysis",
    "📌 Image Classifier",
    "📌 Recommendation System",
    "📄 Resume"
])

with tab1:
    st.subheader("📌 Sentiment Analysis App")
    st.write("""
    - Built an ML model to classify text sentiment (positive/negative/neutral).  
    - Deployed as a **Streamlit web app**.  
    """)
    st.markdown("[🔗 View On GitHub](https://github.com/sbmshukla/SentimentAnalysis)")
    st.markdown("[🔗 View Live Model](https://sentimatic.streamlit.app/)")

with tab2:
    st.subheader("📌 Image Classifier")
    st.write("""
    - Deep Learning-based **CNN classifier** trained on image datasets.  
    - Achieved **90%+ accuracy** on test data.  
    """)
    st.markdown("[🔗 View Project](https://github.com/yourusername/image-classifier)")

with tab3:
    st.subheader("📌 Movie Recommendation System")
    st.write("""
    - Implemented a **content-based + collaborative filtering** recommender.  
    - Built with **scikit-learn, cosine similarity, and matrix factorization**.  
    """)
    st.markdown("[🔗 View Project](https://github.com/yourusername/recommender-system)")

with tab4:
    st.subheader("📄 Download My Resume")
    with open("resume.pdf", "rb") as pdf_file:
        st.download_button(
            label="⬇️ Download Resume",
            data=pdf_file,
            file_name="Shubham_Shukla_Resume.pdf",
            mime="application/pdf"
        )

# --- CONTACT ---
st.header("📬 Contact Me")
st.write("Let's connect! 🚀")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("📧 **Email:** [sbmshukla@gmail.com](mailto:sbmshukla@gmail.com)")
with col2:
    st.markdown("🌐 **LinkedIn:** [linkedin.com/in/sbmhukla](https://linkedin.com/in/sbmhukla)")
with col3:
    st.markdown("💻 **GitHub:** [github.com/sbmshukla](https://github.com/sbmshukla)")