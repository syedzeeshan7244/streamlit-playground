import streamlit as st 
import pandas as pd
st.title("Streamlit Text Input")

name = st.text_input("Enter your name ")
age = st.slider("Select your age" , 0,100,25)


st.write(f"Your age is :  {age}")   

options = ["Python", "Java" , "c++", "Javascript"]
choice = st.selectbox("Choose your favourite programming language ", options)

st.write(f"You selected :  {choice}")   


if name:
    st.write(f"Hello {name}")   
    
    
data = {
    "Name" : ["John","Jane","Jake","Jill"],
    "Age" : [28,29,30,31],
    "city" : ["New york","LA", "Chicago","Houston"] 
}    
df =  pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)
upload_files = st.file_uploader("Choose a csv file", type ="csv")
if upload_files is not None:
    df=pd.read_csv(upload_files)
    st.write(df)
     