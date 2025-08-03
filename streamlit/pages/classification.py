import streamlit as st
st.snow()
st.title("🖥️ Classification Task")
st.divider()
st.header("To Predict whether an individual is likely to seek mental health treatment.")
st.divider()
st.markdown("""
## 🧠 Models Used for Classification:

1. Logistic Regression  
2. Random Forest  
3. XGBoost  
4. Support Vector Machine (SVM)
""")
st.divider()
st.subheader("🤖 Logisitic Regression")
st.markdown("""
### Tuned Hyperparameters:
     
- C = 0.01
- max_iter = 100
- solver = saga      

""")

st.markdown("""
### Classification Report
            
""")
st.code("""
               precision    recall  f1-score   support

          No       0.85      0.76      0.80       129
         Yes       0.77      0.86      0.82       123

    accuracy                           0.81       252
   macro avg       0.81      0.81      0.81       252
weighted avg       0.81      0.81      0.81       252
""")

st.code("Best Score With Tuned Hyperparameters :  np.float64(0.8470370917688784)")
st.divider()
st.subheader("🌳 Random Forest")
st.markdown("""
### Tuned Hyperparameters
- max_depth = None
- max_features = sqrt
- n_estimators = 100
""")
st.markdown("""
### Classification Report
""")
st.code("""
                precision    recall  f1-score   support

          No       0.84      0.76      0.80       129
         Yes       0.77      0.85      0.81       123

    accuracy                           0.81       252
   macro avg       0.81      0.81      0.81       252
weighted avg       0.81      0.81      0.81       252
""")
st.code("Best Score With Tuned Hyperparameters : np.float64(0.8341461011772818)")
st.divider()
st.subheader("⚡ XG boost")
st.markdown("""
### Tuned Hyperparameters
- max_depth = 3
- learning_rate = 0.01
- n_estimators = 200
""")
st.markdown("""
### Classification Report
""")
st.code("""
                precision    recall  f1-score   support

           0       0.79      0.78      0.78       129
           1       0.77      0.79      0.78       123

    accuracy                           0.78       252
   macro avg       0.78      0.78      0.78       252
weighted avg       0.78      0.78      0.78       252
""")
st.code("Best Score With Tuned Hyperparameters : np.float64(0.8401261021624551)")
st.divider()
st.subheader("🧮 SVM")
st.markdown("""
### Tuned Hyperparameters
- C = 0.1
- gamma = scale
- kernel = linear
""")
st.markdown("""
### Classification Report
            
""")
st.code("""
               precision    recall  f1-score   support

           0       0.90      0.71      0.79       129
           1       0.75      0.92      0.82       123

    accuracy                           0.81       252
   macro avg       0.82      0.81      0.81       252
weighted avg       0.83      0.81      0.81       252
""")
st.code("Best Score With Tuned Hyperparameters : np.float64(0.8500369439929066)")
data = {
    "Model": ["Logistic Regression", "Random Forest", "XGBoost", "Support Vector Machine (SVM)"],
    "Accuracy Score": [0.847, 0.834, 0.840, 0.850]

}
import pandas as pd
df = pd.DataFrame(data)
st.markdown("## 📊 Model Accuracy Comparison")
st.dataframe(df)