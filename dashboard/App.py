import streamlit as st
import pandas as pd


import streamlit as st
import pandas as pd
import psycopg2
import numpy as np

def get_patients_df():
    connection = psycopg2.connect(
            host="localhost",
            database="patient_elt_pipeline", 
            user="postgres",
            password="password",  
            port="5432" 
        )
    query = "SELECT * FROM transformed.patients"
    df = pd.read_sql_query(query, con=connection)
    connection.close()
    return df

def get_claims_transactions_df():
    connection = psycopg2.connect(
            host="localhost",
            database="patient_elt_pipeline", 
            user="postgres",
            password="password",  
            port="5432" 
        )
    query = "SELECT * FROM transformed.claims_transactions"
    df = pd.read_sql_query(query, con=connection)
    connection.close()
    return df

#############

st.set_page_config(page_title='Dashboard', layout='wide')

st.title('Welcome to the `patient_elt_pipeline` dashboard!', text_alignment='center')

st.divider()

patients = get_patients_df()
claims_transactions = get_claims_transactions_df()

c1,c2,c3 = st.columns(3)
c1.metric(label='County', value='Oakland')
c2.metric(label='Median income', value= np.median(patients['healthcare_coverage']))
c3.metric(label='Unique patients', value= int(np.median(patients['income'])))

st.space()

c5,c6 = st.columns(2)
with c5:
    num_unique_claims = claims_transactions['claim_id'].nunique()
    c5.metric(label='Number of claims', value=num_unique_claims)
with c6:
    total_claim_value = round(claims_transactions['transaction_amount'].sum(), 2)
    st.metric(label='Total claim amount', value=total_claim_value)

st.space()

c7, c8 = st.columns(2)
with c7:
    gender_distribution = patients['gender'].value_counts()
    st.bar_chart(gender_distribution, x_label='Gender Distribution')

with c8:
    st.dataframe(patients)
