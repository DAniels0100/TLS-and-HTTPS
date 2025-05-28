En este repositorio se presentan 2 aplicaciones sencillas que usan el metodo TLS para una comunicacion segura. 

La primera exclusivamente usa el metodo TLS para la comunicacion encriptada, esta siendo un app de "mesajeria" server-client. 

La segunda siendo una app web que usa el protocolo HTTPS.

App TLS 

-----------------------Comandos a utilizar--------------------------------- 

Primero crear certificado y llave: -python generate_cert.py 

Segundo correr app: -python Mensajeria_TLS.py

App HTTPS 

-----------------------Comandos a utilizar--------------------------------- 

python -m venv venv source venv/bin/activate 

pip install Flask requests

(Para crear un entorno virtual) 

Levantar el servidor: source venv/bin/activate python server.py 

Levantar el cliente: source venv/bin/activate python client.py
