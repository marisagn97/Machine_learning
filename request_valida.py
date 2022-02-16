# Importación de librerías
import requests

# Diccionario/JSON con los datos
request_dict = {
    "C_YEAR": 2006,
    "C_MNTH": 8,
    "C_WDAY": 5,
    "C_HOUR": 14,
    "C_WTHR": "1",
    "C_RALN": "1",
    "P_SEX": "M",
    "P_SAFE": "02",
    "P_USER": "2",
    "C_VEHS": "2",
    "P_AGE": "04",
    "V_ANTIG": "19",
    "P_PSN": "23",
    "C_CONF": "31",
    "C_TRAF": "18",
    "V_TYPE": "01",
    "C_RCFG": "01",
    "C_RSUR": "1"
}

# Definición ruta /predict
url = "http://127.0.0.1:5000/predict"

# Generación de la petición de tipo POST
r = requests.post(url, json=request_dict)

# Comprobación del estado de la petición por medio de su código de estado
r.status_code

print(r.json())