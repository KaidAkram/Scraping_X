import streamlit as st
from main import Scrapping_account
import pandas as pd
st.title("Scrapping tweets")
st.subheader("Just by giving the X account you want to scrape you can get all tweets ")
data = None
account = st.text_input("Enter the url account")
if st.button("scrape it"):
    if account and data == None:
        st.write('getting tweets ...')
        data = Scrapping_account(account)
if data : 
 st.write('Total of Posts:' , len(data['tweets']))
 st.dataframe(data , width=800)

else:
    
    st.write("No data yet")


