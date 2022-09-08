#!/usr/bin/env python
# coding: utf-8

# In[12]:


import joblib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from numpy import outer
from PIL import Image

#model = joblib.load(m)



# model = joblib.load("‪C:\Users\jaswa\Downloads\customer.pkl")
model = joblib.load('customer.pkl')


def web_app():

    st.write("""
    # Customer Behaviour Analysis with Machine Learning
    ## This app predicts to which category a customer belongs too
   """)
    image = Image.open("C:/Users/karthika2001/Downloads/customer behaviour.png")

    st.image(image, caption='Customer Behaviour Analysis')

    
    st.header("User Details")
    st.subheader("Kindly Enter The following Details in order to make a prediction")

    INCOME = st.number_input("INCOME",1500,120000)
    AGE = st.number_input("AGE",19,80)
    Month_Customer = st.number_input("Month_Customer",12,50)
    TotalSpendings = st.number_input("TotalSpendings",5,3000)
    Children = st.number_input("Children",0,3)
    
    if st.button("Press here to make Prediction"):
        
        result = model.predict([[INCOME,AGE,Month_Customer,TotalSpendings,
                                Children]])
        if result == 0:
            result = "Group 1"
        elif result == 1: 
            result = "Group 2"
        elif result == 2: 
            result = "Group 3"
        else : 
            result = "Group 4"
        
        
        st.text_area(label='Category belongs to:- ',value=result , height= 100)
         
    
    
run = web_app()


# In[ ]:




