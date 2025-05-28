from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/saludo')
def saludo():
    return jsonify(mensaje='Testing HTTPS Server Running on Python')

if __name__ == '__main__':
    # ssl_context=(ruta_certificado, ruta_clave)
    app.run(
        host='0.0.0.0',
        port=5000,
        ssl_context=('cert/cert.pem', 'cert/key.pem')
    )
