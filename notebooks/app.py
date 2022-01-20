# Importación de librerías
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

# Inicialización de la aplicación de Flask
app = Flask(__name__)
model = pickle.load(open('modelo.pkl', 'rb'))

# Cuerpo/contenido de la aplicación
@app.route('/') # Ruta/Página de inicio
def home(): # Definición de su contenido
    '''
    Página de inicio
    '''
    return render_template('index.html') # Impresión por pantalla del archivo HTML

@app.route('/predict',methods=['POST']) # Ruta/Página de predicción vía request (JSON)
def predictr():
    '''
    Predicción por medio de una request
    '''
    int_features = [x for x in request.json.values()] # Conversión de los datos de la request en formato JSON a números enteros
    final = np.array(int_features) # Agrupación en array de Numpy de dichos datos
    data_unseen = pd.DataFrame([final], columns = ['C_YEAR', 'C_MNTH', 'C_WDAY', 'C_HOUR', 'C_WTHR', 'C_RALN', 'P_SEX', 'P_SAFE', 'P_USER', 'C_VEHS', 'P_AGE', 'V_ANTIG','P_PSN', 'C_CONF', 'C_TRAF', 'V_TYPE', 'C_RCFG', 'C_RSUR'])
    prob_predictions = model.predict_proba(data_unseen) # Predicción de probabilidades sobre los nuevos datos
    output= prob_predictions[:,1][0]# Utilización únicamente de las probabilidades de pertenecer a la categoría 1 (Fallecimiento)
    return jsonify(output) # Devolución de la probabilidad de que ocurra accidente con falleimiento


@app.route('/predictGUI',methods=['POST']) # Ruta/Página de predicción vía formulario (GUI)
def predict():
    '''
    Predicción por medio de la GUI
    '''
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = ['C_YEAR', 'C_MNTH', 'C_WDAY', 'C_HOUR', 'C_WTHR', 'C_RALN', 'P_SEX', 'P_SAFE', 'P_USER', 'C_VEHS', 'P_AGE', 'V_ANTIG','P_PSN', 'C_CONF', 'C_TRAF', 'V_TYPE', 'C_RCFG', 'C_RSUR'])
    prob_predictions = model.predict_proba(data_unseen)
    probs = prob_predictions[:,1][0]
    return render_template('index.html', prediction_text='Accident probability of fatality is {}'.format(probs))
    # Impresión por pantalla de los resultados incrustado dentro del documento HTML

# Puesta en marcha de la aplicación de Flask
if __name__ == "__main__":
    app.run(debug=True)
