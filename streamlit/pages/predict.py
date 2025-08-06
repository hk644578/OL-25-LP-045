import streamlit as st
st.title("🔮Mental Health Treatment Classifier")
st.subheader("Enter Parameters: ")
age=st.number_input("Enter Your Age:",min_value=0,max_value=120,step=1)
cln_gender=st.selectbox("Gender",['Male','Female'])
self_employed = st.selectbox("Self Employed", [ 'Yes','No'])
family_history = st.selectbox("Family History of Mental Illness", [ 'Yes','No'])
work_interfere = st.selectbox("Work Interfere", ['Sometimes', 'Never', 'Rarely', 'Often','Dont know'])
range_no_employees = st.selectbox("No. of Employees", ['6-25', '26-100', 'More than 1000', '100-500', '1-5', '500-1000'])
remote_work = st.selectbox("Remote Work", [ 'Yes','No'])
tech_company = st.selectbox("Tech Company", ['Yes', 'No'])
benefits = st.selectbox("Mental Health Benefits", ['Yes', "Don't know", 'No'])
care_options = st.selectbox("Care Options", ['Yes','No','Not sure'])
wellness_program = st.selectbox("Wellness Program", [ 'Yes','No', "Don't know"])
seek_help = st.selectbox("Seek Help", ['Yes', "Don't know", 'No'])
anonymity = st.selectbox("Anonymity", [ 'Yes', 'No',"Don't know"])
leave = st.selectbox("Leave", ["Don't know", 'Somewhat easy', 'Very easy', 'Somewhat difficult', 'Very difficult',"Don't know" ])
mental_health_consequence = st.selectbox("Mental Health Consequence", ['Yes','Maybe','No'])
phys_health_consequence = st.selectbox("Physical Health Consequence", ['Yes','Maybe','No'])
coworkers = st.selectbox("Coworkers", ['Yes','Some of them','No'])
supervisor = st.selectbox("Supervisor", ['Yes','Some of them','No'])
mental_health_interview = st.selectbox("Mental Health Interview", ['Yes','Maybe','No'])
phys_health_interview = st.selectbox("Physical Health Interview", ['Yes','Maybe','No'])
mental_vs_physical = st.selectbox("Mental vs Physical", ['Yes','No',"Don't know"])
obs_consequence = st.selectbox("Observed Consequences",['Yes','No'] )
import pandas as pd

def convert_no_employees(value):
    if isinstance(value, str):
        if 'more than 1000' in value.lower():
            return 1000
        elif '-' in value:
            parts = value.split('-')
            try:
                return (int(parts[0]) + int(parts[1])) // 2
            except ValueError:
                return None
    return None
no_employees=convert_no_employees(range_no_employees)
input_dict = {
        'Age': age,
        'Cleaned_Gender': cln_gender,
        'self_employed': self_employed,
        'family_history': family_history,
        'work_interfere': work_interfere,
        'no_employees': no_employees,
        'remote_work': remote_work,
        'tech_company': tech_company,
        'benefits': benefits,
        'care_options': care_options,
        'wellness_program': wellness_program,
        'seek_help': seek_help,
        'anonymity': anonymity,
        'leave': leave,
        'mental_health_consequence': mental_health_consequence,
        'phys_health_consequence': phys_health_consequence,
        'coworkers': coworkers,
        'supervisor': supervisor,
        'mental_health_interview': mental_health_interview,
        'phys_health_interview': phys_health_interview,
        'mental_vs_physical': mental_vs_physical,
        'obs_consequence': obs_consequence
}
import joblib
model=joblib.load("pipeline.pkl")
if st.button("Predict"):
    st.balloons()
    import pandas as pd
    input_df=pd.DataFrame([input_dict])
    prediction = model.predict(input_df)
    st.success(f"Treatment ? : *{prediction[0]}*")

