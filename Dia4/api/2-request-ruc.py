import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = 'https://apiperu.dev/api/ruc'
TOKEN = os.getenv("TOKEN")
# TOKEN = 'd8a91a29cbdac2310a9d02125bbc2e197f9bf3ac125a2d31c71aef72a6b6c60c'
data_request = {
  "ruc":"20117592899"
}

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

response = requests.post(API_URL,json=data_request,headers=headers)

if response.status_code == 200:
    data = response.json()['data']
    print("="*50)
    print(f'RUC : {data["ruc"]}')
    print(f'Razon Social : {data["nombre_o_razon_social"]}')
    print(f'Dirección : {data["direccion"]}')
    print(f'Distrito : {data["distrito"]}')
    print(f'Provincia : {data["provincia"]}')
    print(f'Departamento : {data["departamento"]}')
    print(f'ubigeo : {data["ubigeo_sunat"]}')