import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
st.snow()
df=pd.read_csv('survey.csv')
st.title("📊 DATA ANALYSIS")
st.subheader("How Big Is The Data: ")
st.code(df.shape)
st.subheader("How Does Data Look Like")
st.dataframe(df.head(),use_container_width=True)
st.subheader("What Is The Data Type Of Column")
buffer=io.StringIO()
df.info(buf=buffer)
info_str=buffer.getvalue()
info_df = pd.DataFrame({
    'Column': df.columns,
    'Non-Null Count': df.notnull().sum(),
    'Dtype': df.dtypes.astype(str)
}).reset_index(drop=True)
st.dataframe(info_df, use_container_width=True)
st.subheader("Are There Any Missing Value")
st.code(df.isnull().sum())
st.subheader("How Does The Data Look Mathematically")
st.code(df.describe())
st.subheader("Are There Any Duplicate Values")
st.code(df.duplicated().sum())
st.divider()
st.subheader("UNIVARIATE ANALYSIS")
st.divider()
import random
random.seed(42)
def clean_gender(gender):
    gender = str(gender).strip().lower()

    if gender in ['male', 'm', 'cis male', 'man', 'make', 'msle', 'mal', 'maile', 'male-ish', 'malr', 'cis man', 'mail']:
        return 'Male'
    elif gender in ['female', 'f', 'cis female', 'woman', 'femake', 'femail', 'female (cis)', 'trans woman']:
        return 'Female'
    else:
        # Randomly assign either 'Male' or 'Female'
        return random.choice(['Male', 'Female'])
df['Cleaned_Gender'] = df['Gender'].map(clean_gender)
df.drop(columns=['Gender'], inplace=True)
fig, ax = plt.subplots()
df['Cleaned_Gender'].value_counts().plot(kind='bar', ax=ax)
ax.set_xlabel('Gender')
ax.set_ylabel('Count')
ax.set_title('Gender Distribution')
st.subheader("Gender Distribution")
st.pyplot(fig)
df1 = df[(df['Age'] <= 10) | (df['Age'] >= 100)]
valid_ages = df[(df['Age'] >= 10) & (df['Age'] <= 100)]
age_mode = valid_ages['Age'].mode()[0]
df.loc[(df['Age'] < 10) | (df['Age'] > 100) | (df['Age'].isna()), 'Age'] = age_mode
fig, ax = plt.subplots()
sns.histplot(df['Age'], kde=True, ax=ax)
ax.set_xlabel('Age')
ax.set_ylabel('Count')
ax.set_title('Age Distribution')
st.subheader("Age Distribution")
st.pyplot(fig)
country_counts = df['Country'].value_counts()
top_countries = country_counts.head(10).index.tolist()
df['Country_Cleaned'] = df['Country'].apply(lambda x: x if x in top_countries else 'Other')
fig,ax=plt.subplots()
df['Country_Cleaned'].value_counts().plot(kind='bar',ax=ax)
ax.set_xlabel('Country')
ax.set_ylabel('Count')
ax.set_title('Country Distribution')
st.subheader("Country Distribution")
st.pyplot(fig)
df.drop(columns=['state'], inplace=True)
df['self_employed'] = df['self_employed'].apply(
    lambda x: random.choice(['Yes', 'No']) if pd.isna(x) else x
)
fig, ax = plt.subplots()
df['family_history'].value_counts(dropna=False).plot(kind='bar', ax=ax)
ax.set_xlabel('family_history')
ax.set_ylabel('Count')
ax.set_title('Family History Distribution')
st.subheader("Family History Distribution")
st.pyplot(fig)
fig, ax = plt.subplots()
df['treatment'].value_counts(dropna=False).plot(kind='bar', ax=ax)
ax.set_xlabel('treatment')
ax.set_ylabel('Count')
ax.set_title('Treatment Distribution')
st.subheader("Treatment Distribution")
st.pyplot(fig)
df['work_interfere']=df['work_interfere'].apply(lambda x: 'Dont know' if pd.isna(x) else x)
fig, ax = plt.subplots()
df['work_interfere'].value_counts(dropna=False).plot(kind='bar', ax=ax)
ax.set_xlabel('work_interfere')
ax.set_ylabel('Count')
ax.set_title('Work Interfere Distribution')
st.subheader("Work Interfere Distribution")
st.pyplot(fig)
df.drop(columns=['comments'], inplace=True)
df.drop(columns=['Timestamp'], inplace=True)
categorical_cols = ['no_employees', 'remote_work', 'tech_company',
       'benefits', 'care_options', 'wellness_program', 'seek_help',
       'anonymity', 'leave', 'mental_health_consequence',
       'phys_health_consequence', 'coworkers', 'supervisor',
       'mental_health_interview', 'phys_health_interview',
       'mental_vs_physical', 'obs_consequence']
for col in categorical_cols:
    st.subheader(f"{col} Distribution")
    
    fig, ax = plt.subplots()
    df[col].value_counts(dropna=False).plot(kind='bar', ax=ax)
    ax.set_xlabel(col)
    ax.set_ylabel('Count')
    ax.set_title(f'{col} Distribution')
    
    st.pyplot(fig)

st.divider()
st.subheader("BIVARIATE ANALYSIS")
st.divider()

sns.set(style='whitegrid')


cat_cols = ['self_employed', 'family_history', 'treatment',
       'work_interfere', 'no_employees', 'remote_work', 'tech_company',
       'benefits', 'care_options', 'wellness_program', 'seek_help',
       'anonymity', 'leave', 'mental_health_consequence',
       'phys_health_consequence', 'coworkers', 'supervisor',
       'mental_health_interview', 'phys_health_interview',
       'mental_vs_physical', 'obs_consequence', 'Cleaned_Gender',
       'Country_Cleaned']
for col in cat_cols:
    st.subheader(f"Treatment vs {col}")

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(x='treatment', hue=col, data=df, ax=ax)
    ax.set_title(f'Treatment vs {col}')
    ax.set_xlabel('Treatment')
    ax.set_ylabel('Count')
    ax.legend(title=col, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
    st.pyplot(fig)