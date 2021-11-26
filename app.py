from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd

def predict_cvc (model, df):
    predictions_data = predict_model(estimator = model, data = df)
    return predictions_data['Label'][0]

model = load_model('nb_tunado')

st.title('Prevendo se o paciente irá desenvolver uma doença cardiovascular.')
st.write('Esse aplicativo irá predizer se o seu estado atual de saúde é propenso à evolução de um CVC.         Preencha os campos abaixo e clique em "Predizer".')


anaemia_options = { 
    1: "Sim",
    0: "Não"
    } 

diabetes_options = { 
    1: "Sim",
    0: "Não"
    }

pressure_options = { 
    1: "Sim",
    0: "Não"
    }

sex_options = { 
    1: "Masculino",
    0: "Feminino"
    }

smoking_options = { 
    1: "Sim",
    0: "Não"
    }


age = st.slider(label = 'Idade', min_value = 0,
                          max_value = 100,
                          value = 40,
                          step = 1)

anaemia = st.radio(label = "Tem anemia?",
                   options = (1,0),
                   format_func = lambda x: anaemia_options.get(x))

diabetes = st.radio(label = "Tem diabetes?",
                   options = (1,0),
                   format_func = lambda x: diabetes_options.get(x))

pressure = st.radio(label = "Tem pressão alta?",
                   options = (1,0),
                   format_func = lambda x: pressure_options.get(x))

sex = st.radio(label = "Qual é o seu gênero?",
                   options = (1,0),
                   format_func = lambda x: sex_options.get(x))

smoking = st.radio(label = "É fumante?",
                   options = (1,0),
                   format_func = lambda x: smoking_options.get(x))


features = {
            'age': age,
            'anaemia': anaemia,
            'diabetes': diabetes,
            'high_blood_pressure': pressure,
            'sex': sex,
            'smoking': smoking
            }

features_df  = pd.DataFrame([features])


if st.button('Predizer'):
    
    prediction = predict_cvc(model, features_df)
    
    if prediction == 0:
        st.write('O paciente não tem pré-disposição para desenvolver uma doença cardiovascular!')
    else:
        st.write('O paciente tem pré-disposição para desenvolver uma doença cardiovascular!')
