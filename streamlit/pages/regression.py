import streamlit as st
st.snow()
st.title("📈 Regression Task")
st.divider()
st.header("Predict the age of an individual based on personal and workplace attributes, supporting age-targeted intervention design")
st.divider()
st.markdown("""
## 📈 Models Used for Regression

- ➕ Linear Regression  
- 🧱 Ridge Regression  
- 🪢 Lasso Regression    
- 🌳 Decision Tree Regressor  
- 🌲 Random Forest Regressor     
- ⚡ XGBoost Regressor  
""")
st.divider()
st.subheader("➕ Linear Regression")
st.code("""MSE: 41.66017109076887
RMSE: 6.454469078922671
R2 Score: 0.05108698866536188""")
st.subheader("🧱 Ridge Regression")
st.markdown("""
### Tuned Hyperparameters: 
- alpha = 1.0
""")
st.code("""MSE: 41.64429524479578
RMSE: 6.453239128127501
R2 Score: 0.05144860016179531""")
st.subheader("🪢 Lasso Regression")
st.markdown("""
### Tuned Hyperparameters: 
- alpha = 0.01
""")
st.code("""MSE: 41.583852376893
RMSE: 6.448554285798717
R2 Score: 0.0528253353573942""")
st.subheader("🌳 Decision Tree Regressor")
st.markdown("""
### Tuned Hyperparameters: 
- max_depth = 3
- min_samples_leaf = 1
- min_samples_split = 2
""")
st.code("""MSE: 44.568474064983114
RMSE: 6.675962407397387
R2 Score: -0.01515677512337188""")
st.subheader("🌲 Random Forest Regressor")
st.markdown("""
### Tuned Hyperparameters: 
- max_depth = 5
- n_estimators = 100
- min_samples_split = 2
""")
st.code("""MSE: 42.87626772392533
RMSE: 6.547997229987604
R2 Score: 0.02338739243163168""")
st.subheader("⚡ XGBoost Regressor")
st.markdown("""
### Tuned Hyperparameters: 
- max_depth = 5
- n_estimators = 100
- learning_rate = 0.05
""")
st.code("""MSE: 41.942684173583984
RMSE: 6.476317176728143
R2 Score: 0.04465204477310181""")

st.header("⚖️ Models Comparison")
st.code("""               Model        MSE      RMSE  R2 Score
2   Lasso Regression  41.583852  6.448554  0.052825
1   Ridge Regression  41.644295  6.453239  0.051449
0  Linear Regression  41.660171  6.454469  0.051087
5            XGBoost  41.942684  6.476317  0.044652
4      Random Forest  42.876268  6.547997  0.023387
3      Decision Tree  44.568474  6.675962 -0.015157
""")

