import streamlit as st
def home():
    st.snow()
    st.title("📚 OpenLearn 1.0 - ML Capstone Project")
    st.subheader("🧠 Mental Wellness in Tech")

    st.markdown("""
    ## 🎯 Project Objective
    This project aims to uncover insights into mental health challenges faced by tech professionals and develop machine learning solutions to:
    
    - 🩺 **Classify** individuals likely to seek treatment.
    - 📊 **Predict** age based on workplace and personal attributes.
    - 🔍 **Cluster** employees into mental wellness profiles for targeted support.

    ## 🗂️ Dataset Source
    - **Name**: Mental Health in Tech Survey  
    - **Provided by**: OSMI (Open Sourcing Mental Illness)  
    - **Size**: 1,500+ responses  
    - **Features**: Demographics, workplace policies, mental health history, support attitudes.

    ## 💼 Real-World Scenario
    Imagine working as a Machine Learning Engineer at NeuronInsights, helping top tech firms identify signs of burnout and improve employee wellbeing through data-driven HR strategies.

    ## 🧪 ML Components
    - **EDA**: Explore trends in gender, age, remote work, and support systems.
    - **Classification**: Predict if a person seeks treatment.
    - **Regression**: Estimate age from workplace and mental health traits.
    - **Clustering**: Identify personas like _Silent Strugglers_ and _Open Advocates_.

    ## 🖥️ Final Product
    An interactive Streamlit dashboard with:
    - Data visualizations
    - ML predictions
    - Persona clustering insights
    - Practical HR recommendations
    """)
    
app = st.navigation(
    [
        st.Page(home, title="Project Details", icon="🏠"),
        st.Page("pages/EDA.py", title="Data Analysis", icon="🔎"),
        st.Page("pages/classification.py", title="Classification Task", icon="🖥️"),
        st.Page("pages/regression.py", title="Regression Task", icon="📈"),
        st.Page("pages/cluster.py", title="Clustering Task", icon="🧩"),
        st.Page("pages/predict.py", title="Time to Predict", icon="🔮")

    ]
)
app.run()

    
    
