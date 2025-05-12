import streamlit as st
import pandas as pd 
import numpy as np


### Title of the application
st.title(" Hello Streamlit Aplication! This is BankAlfalah")

## Displaying a simple text 
st.write("This is a simple text")

#Creating a simple dataframe
df = pd.DataFrame({
    'First Coloumn ' : [1,2,3,4],
    'Second Column' :[10,20,30,40]
})

# Displaying the data frame
st.write("Here is the dataframe")
st.write(df)

#creating a line chart 
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c',]   
)

st.line_chart(chart_data)