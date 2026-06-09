import streamlit as st
import pandas as pd

# Title
st.title("Finance Data Extractor")

# Input box
paragraph = st.text_area("Enter financial paragraph:")

# Mock function to extract financial data (replace with actual function)
def extract(text):
    return {
        "revenue_actual": "94.93 billion", 
        "revenue_expected": "94.58 billion", 
        "eps_actual": "1.64",
        "eps_expected": "1.60"
    }
    
if st.button("Extract"):
    if paragraph:
        extracted_data = extract(paragraph)
        data = {
            "Measure": ['Revenue', 'EPS'],
            "Estimated": [extracted_data['revenue_expected'], extracted_data['eps_expected']],
            "Actual": [extracted_data['revenue_actual'], extracted_data['eps_actual']]
        }
        df = pd.DataFrame(data)
        st.table(df)
    else:
        st.warning("Please enter a paragraph to extract data from.")