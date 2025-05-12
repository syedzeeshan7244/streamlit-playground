**Introduction to Streamlit**

Streamlit is an open-source Python library that makes it easy to create and share custom web apps for machine learning and data science projects with very little code.

**🔹 Why Use Streamlit?**

**Fast:** Turn data scripts into shareable web apps in minutes.
**Simple:** No need to learn HTML, CSS, or JavaScript.
**Interactive:** Easily add widgets (sliders, buttons, inputs) to control data or visualizations.

**🔧 Basic Installation**

pip install streamlit

**✅ Your First Streamlit App**

Create a file named app.py:

import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is your first Streamlit app.")


Run the app:

streamlit run app.py

This launches a local web server and opens the app in your browser.


🔹 Common Streamlit Functions

| Function              | Purpose                               |
| --------------------- | ------------------------------------- |
| `st.title()`          | Add a title to the app                |
| `st.write()`          | Display text, data, or markdown       |
| `st.text_input()`     | Text input box                        |
| `st.button()`         | Button widget                         |
| `st.slider()`         | Slider for numeric input              |
| `st.line_chart(data)` | Plot a line chart                     |
| `st.dataframe(df)`    | Show a pandas DataFrame interactively |
| `st.file_uploader()`  | Upload files into the app             |


**🧠 Example: Simple Interactive App**

import streamlit as st

st.title("BMI Calculator")

height = st.number_input("Enter height (in meters):")
weight = st.number_input("Enter weight (in kg):")

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is {bmi:.2f}")
    else:
        st.error("Please enter a valid height.")

Streamlit is ideal for rapid prototyping of data apps or ML model demos.        
