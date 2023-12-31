# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:01:15 2022

@author: siddhardhan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Çoklu Hastalık Tahmin Sistemi',
                          
                          ['Diyabet Tahmini',
                           'Kalp Hastalığı Tahmini',
                           'Parkinson Tahmini'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diyabet Tahmini'):
    
    # page title
    st.title('Makine Öğrenmesi Kullanarak Diyabet Tahmini')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Hamilelik Sayısı')
        
    with col2:
        Glucose = st.text_input('Glikoz Seviyesi')
    
    with col3:
        BloodPressure = st.text_input('Kan Basıncı')
    
    with col1:
        SkinThickness = st.text_input('Cilt Kalınlığı')
    
    with col2:
        Insulin = st.text_input('İnsülin Seviyesi')
    
    with col3:
        BMI = st.text_input('BMI Değeri')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diyabet Soyağacı Değeri')
    
    with col2:
        Age = st.text_input('Yaş')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diyabet Test Sonucu'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'Diyabet Hastasıdır'
        else:
          diab_diagnosis = 'Diyabet Hastası Değildir'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Kalp Hastalığı Tahmini'):
    
    # page title
    st.title('Makine Öğrenmesi Kullanarak Kalp Hastalığı Tahmini')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Yaş')
        
    with col2:
        sex = st.text_input('Cinsiyet')
        
    with col3:
        cp = st.text_input('Göğüs Ağrısı Türleri')
        
    with col1:
        trestbps = st.text_input('Dinlenme Kan Basıncı')
        
    with col2:
        chol = st.text_input('Serum Kolestoral, mg/dl cinsinden')
        
    with col3:
        fbs = st.text_input('Açlık Kan Şekeri > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Dinlenme Elektrokardiyografi sonuçları')
        
    with col2:
        thalach = st.text_input('Maksimum Kalp Atış Hızı')
        
    with col3:
        exang = st.text_input('Egzersize Bağlı Angina')
        
    with col1:
        oldpeak = st.text_input('Egzersizin neden olduğu ST depresyonu')
        
    with col2:
        slope = st.text_input('Zirve egzersiz ST segmentinin eğimi')
        
    with col3:
        ca = st.text_input('Florosopi ile renklendirilen başlıca damarlar')
        
    with col1:
        thal = st.text_input('tal: 0 = normal; 1 = sabit kusur; 2 = geri döndürülebilir kusur')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Kalp Hastalığı Test Sonucu'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'Kalp Hastasıdır.'
        else:
          heart_diagnosis = 'Kalp Hastası Değildir.'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinson Tahmini"):
    
    # page title
    st.title("Makine Öğrenmesi Kullanarak Parkinson Hastalığı Tahmini")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson Hastalığı Test Sonucu"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "Parkinson Hastasıdır."
        else:
          parkinsons_diagnosis = "Parkinson Hastası Değildir."
        
    st.success(parkinsons_diagnosis)
















