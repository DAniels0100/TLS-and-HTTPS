import requests
import urllib3

# Desactivar warning por certificado autofirmado
urllib3.disable_warnings()

resp = requests.get(
    'https://localhost:5000/api/saludo',
    verify=False
)
print('Código:', resp.status_code)
print('JSON:', resp.json())
