import pickle 
import streamlit as st
import pandas as pd

pickle_in = open("C:/Users/Sushri Supravat/stroke/brain_stroke.pkl", 'rb')
model = pickle.load(pickle_in)

def predict_brainstroke(gender, age, hypertension, heart_disease, ever_married, work_type,
                        Residence_type, avg_glucose_level, bmi, smoking_status):
    
    if gender == 'Male':
        gender = 1
    elif gender == 'Female':
        gender = 0
    elif gender == 'Other':
        gender = 2
        
    if hypertension == 'Yes':
        hypertension = 1
    elif hypertension == 'No':
        hypertension = 0
        
    if heart_disease == 'Yes':
        heart_disease = 1
    elif heart_disease == 'No':
        heart_disease = 0
           
    if ever_married == 'Yes':
        ever_married = 1
    elif ever_married == 'No':
        ever_married = 0
        
    if work_type == 'Private':
        work_type = 3
    elif work_type == 'Self-employed':
        work_type = 4
    elif work_type == 'children':
        work_type = 0
    elif work_type == 'Govt_job':
        work_type = 1
    elif work_type == 'Never_worked':
        work_type = 2
        
    if Residence_type == 'Urban':
        Residence_type = 1
    elif Residence_type == 'Rural':
        Residence_type = 0
        
    if smoking_status == 'never smoked':
        smoking_status = 1
    elif smoking_status == 'Unknown':
        smoking_status = 3
    elif smoking_status == 'formerly smoked':
        smoking_status = 0
    else:
        smoking_status = 2
        
    predict_brainstroke = model.predict(pd.DataFrame[[gender, age, hypertension,
                          heart_disease, ever_married, work_type, Residence_type,
                          avg_glucose_level, bmi, smoking_status]]) 
    
    return predict_brainstroke

def main():
    html_temp = """ 
    <div style ="background-color:white;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> Brain Sroke Prediction </h1> 
    </div> 
    """
    
    st.markdown(html_temp, unsafe_allow_html = True)
    
    gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
    
    age = st.text_input('Age', 'Type Here')
    
    hypertension = st.selectbox('Hypertension', ['Yes', 'No'])
    
    heart_disease = st.selectbox('Heart Disease', ['Yes', 'No'])
    
    ever_married = st.selectbox('Married', ['Yes', 'No'])
    
    work_type = st.selectbox('Work Type', ['Private', 'children', 'Govt_job', 'Nver_worked'])
    
    Residence_type = st.selectbox('Residence_type', ['Urban','Rural'])
    
    avg_glucose_level = st.text_input('Average Glucose level', 'Type Here')
    
    bmi = st.text_input('BMI', 'Type Here')
    
    smoking_status = st.selectbox('Smoking Status', ['never_smoked', 'Unknown', 'Formerly smoked', 'smokes'])
    
    result = ''
    
    if st.button('Predict'):
        result = predict_brainstroke(gender, age, hypertension, heart_disease, 
                  ever_married, work_type, Residence_type, avg_glucose_level, bmi, 
                  smoking_status)
        st.success('The output is {}'.format(result))
        
if __name__ == '__main__':
    main()
