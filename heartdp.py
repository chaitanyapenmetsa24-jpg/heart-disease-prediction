import streamlit as st
import joblib

st.title("HEART DISEASE PREDICTION")
model=joblib.load('hdp1.joblib')
a=st.number_input("Enter Age")
b=st.number_input("Enter Cigars per Day")
c=st.number_input("Enter Total Cholestrol")
d=st.number_input("Enter Systolic Bp ")
e=st.number_input("Enter Diastolic Bp")
f=st.number_input("Enter BMI")
g=st.number_input("Enter Heart Rate")
h=st.number_input("Enter Glucose")
if st.button('PREDICT'):
    p=model.predict([[a,b,c,d,e,f,g,h]])
    if p==1:
        st.text("BE CAUTION,YOU ARE VERY LIKELY TO HAVE HEART DISEASE IN NEXT 10 YEARS")
    else:
        ("CHEERS,YOUR SAFE ")
