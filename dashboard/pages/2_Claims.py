import streamlit as st
import pandas as pd


claims_df = pd.read_csv("../../data_source/test_data/claims.csv")
claims_transactions_df = pd.read_csv("../../data_source/test_data/claims_transactions.csv")

col_1, col_2, col_3 = st.columns(3)
col_1.metric("Total claims", 4)
col_2.metric("Total transactions", 5)
col_3.metric("Total transactions amount", 6)

col_4, col_5 = st.columns(2)
col_4.line_chart()
col_5.bar_chart()
