import streamlit as st
import pandas as pd
from database import create_table,add_expenses,show_expenses,view_expenses_name

create_table()
st.title("Personal Expenses Tracker")

st.sidebar.header("Add Expense !!")
name = st.sidebar.text_input("Enter your name .....")
date = st.sidebar.date_input("Date")
desc = st.sidebar.text_input("Description here")
cat = st.sidebar.selectbox("Category",['Food','Transport','Entertaiment','Bills','Others'])
amt = st.sidebar.number_input("Amount",min_value=0.0,format="%.2f")


if st.sidebar.button("Add Expense"):
    add_expenses(name,date,desc,cat,amt)
    st.sidebar.success("Expense added successfully")


st.header("Expense History")
expenses = show_expenses(name)
expenses_df = pd.DataFrame(expenses,columns=['ID','Name','Date','Description','Category','Amount'])
st.dataframe(expenses_df)

st.header("Expenses by Category")
category_data = view_expenses_name(name)
category_df = pd.DataFrame(category_data, columns=["Category", "Total Amount"])
st.bar_chart(category_df.set_index("Category"))


st.header("Total Expense")
total_expense = expenses_df['Amount'].sum()
st.write(f"Total: ${total_expense:.2f}")