# Se realiza una solicitud POST a una API
# Se recibe informacion del DNI ingresado
# Se usa token de API para autentificarse
# Se imprime respuesta en formato JSON en caso ser exitoso: code status 200

import requests
import os
from decouple import config

# Configuracion Token
token = config('API_TOKEN')
url_dni = 'https://apiperu.dev/api/dni'

# Entrada de usuario
dni = input("ingrese dni :")

# Preparacion de solicitud
data_request = {
    "dni": dni 
}

# Define tipo de autenticacion y tipo de datos (PROCESO ESTANDAR)
headers_request = {
    "Authorization": "Bearer " + str(token), # forma de autentificarse o enviar credenciales de la API (con TOKEN), con formato Bearer (standar para enviar tokens de acceso en peticiones http)
    "Content-Type": "application/json" # Contenido de solicitud en formato json
}

# Envio de la solicitud POST (en este caso particular) a la respuesta "response"
response = requests.post(url_dni,json=data_request,headers=headers_request)

# Manejo de respuesta recibida de petición
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error {response.status_code}")