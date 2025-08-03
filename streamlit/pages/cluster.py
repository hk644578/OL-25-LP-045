import streamlit as st
st.snow()
st.title("🧩 Clustering Task")
st.divider()
st.header("Segment tech employees into distinct clusters based on mental health indicators to aid in tailored HR policies.")
st.divider()
st.markdown("""
## 🧠 Models Used for Classification:

1. KMeans Clustering
2. AgglomerativeClustering
3. DBSCAN
""")
st.divider()
st.subheader("🎯 Kmeans Clustering")
st.markdown("""
### Predicting Suitable Number Of Clusters Using Silhouette Score:
- Silhouette Score for k=2: 0.4253
- Silhouette Score for k=3: 0.4812
- Silhouette Score for k=4: 0.6056
- Silhouette Score for k=5: 0.6652
- Silhouette Score for k=6: 0.6419
- Silhouette Score for k=7: 0.6814
- Silhouette Score for k=8: 0.7034
- Silhouette Score for k=9: 0.7084
- Silhouette Score for k=10: 0.7076
- Silhouette Score for k=11: 0.6919
- Silhouette Score for k=12: 0.6944
- Silhouette Score for k=13: 0.6907
- Silhouette Score for k=14: 0.7173
- Silhouette Score for k=15: 0.7047
- Silhouette Score for k=16: 0.6683
- Silhouette Score for k=17: 0.6552
- Silhouette Score for k=18: 0.6315
- Silhouette Score for k=19: 0.6089
""")
st.code("Optimal Number Of Clusters Is : 9 ")
st.image("Kmeans.png")
st.divider()
st.subheader("🪜 Agglomerative Clustering")
st.subheader("Dendogram: ")
st.image("dendo.png")
st.subheader("Clusters Visualisation: ")
st.image("aggo.png")
st.divider()
st.subheader("🌌 DBSCAN Clustering")
st.markdown("""
### Tuned Hyperparameters: 
- eps = 1.4
- min_samples = 9
""")
st.code("Best Silhouette Score: 0.7216708")
st.subheader("Clusters Visualisation: ")
st.image("dbscan.png")
import streamlit as st

cluster_features = {
    0: {
        "family_history": 0.344687,
        "remote_work": 0.256369,
        "treatment": 0.162085,
        "coworkers": 0.103741,
        "work_interfere": 0.055772
    },
    1: {
        "coworkers": 0.370439,
        "remote_work": 0.198996,
        "treatment": 0.132326,
        "family_history": 0.086207,
        "employer_score": 0.080501
    },
    2: {
        "remote_work": 0.547373,
        "treatment": 0.193033,
        "work_interfere": 0.099994,
        "family_history": 0.070633,
        "employer_score": 0.046123
    },
    3: {
        "family_history": 0.362909,
        "treatment": 0.277577,
        "remote_work": 0.227294,
        "work_interfere": 0.055359,
        "employer_score": 0.041131
    },
    4: {
        "remote_work": 0.342869,
        "family_history": 0.276438,
        "treatment": 0.194512,
        "employer_score": 0.063524,
        "work_interfere": 0.062039
    },
    5: {
        "family_history": 0.359990,
        "treatment": 0.162119,
        "coworkers": 0.142003,
        "remote_work": 0.138851,
        "employer_score": 0.071441
    },
    6: {
        "remote_work": 0.454239,
        "family_history": 0.333157,
        "work_interfere": 0.074227,
        "employer_score": 0.047292,
        "treatment": 0.037733
    },
    7: {
        "coworkers": 0.281630,
        "remote_work": 0.210985,
        "treatment": 0.198586,
        "family_history": 0.145080,
        "work_interfere": 0.065331
    },
    8: {
        "coworkers": 0.348540,
        "remote_work": 0.167048,
        "treatment": 0.141971,
        "family_history": 0.106029,
        "employer_score": 0.096106
    },
}


st.title("🔍 Top Features for Each Cluster")

for cluster_id, features in cluster_features.items():
    with st.expander(f"Cluster {cluster_id}"):
        for feature, score in features.items():
            st.markdown(f"- **{feature}**: {score:.6f}")
st.subheader("🔍 Visulisation for top features for rech clusters: ")
for i in range(0,9):
    st.write(f"Cluster No. {i}")
    st.image(f"cls_{i}.png")


cluster_descriptions = {
    0: ("Hereditary Silent Sufferers", 
        "This group likely has a family history of mental health issues and works remotely, possibly isolating them further. "
        "They do seek treatment, but the cluster doesn't show strong interaction with coworkers or interference at work."),
    
    1: ("Vocal Workplace Advocates", 
        "This group is significantly shaped by coworker interactions. They may be more open or influenced by work culture around mental health."),
    
    2: ("Remote Resilients", 
        "They are primarily remote workers, and while some seek treatment, they experience interference with work."),
    
    3: ("Genetic Warriors", 
        "With a strong genetic predisposition, these individuals are actively treating their condition. They also work remotely."),
    
    4: ("Remote-Aware Responders", 
        "This group also works remotely and has some hereditary links. They're more aware of their mental health and do seek treatment."),
    
    5: ("Quiet Carriers", 
        "This group has family history but moderate interaction with coworkers and treatment."),
    
    6: ("Isolated Inheritors", 
        "High remote work and family history, but very low treatment."),
    
    7: ("Empathetic Collaborators", 
        "They’re emotionally open to coworkers, take treatment, and likely find support in their network."),
    
    8: ("Workplace Seekers", 
        "This group is deeply shaped by interactions at work, and also values the employer's role in mental health support.")
}

st.title("🧠 Cluster Profiles in Layperson's Terms")

for cluster_id, (name, desc) in cluster_descriptions.items():
    with st.expander(f"Cluster {cluster_id}: {name}"):
        st.markdown(desc)
