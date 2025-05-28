import socket
import ssl
import threading

HOST = 'localhost'
PORT = 8443

def run_server():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="cert_&_key/cert.pem", keyfile="cert_&_key/key.pem")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind((HOST, PORT))
        sock.listen(5)
        print(f"[Servidor] Esperando conexión en {HOST}:{PORT}...")
        with context.wrap_socket(sock, server_side=True) as ssock:
            conn, addr = ssock.accept()
            print(f"[Conectado con] {addr}")
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                print(f"[Mensaje recibido] {data}")
                reply = input("Server: ")
                conn.send(reply.encode())

def run_client():
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  # Solo para pruebas

    with socket.create_connection((HOST, PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=HOST) as ssock:
            print(f"[Cliente] Conectado a {HOST}:{PORT}")
            while True:
                msg = input("Client: ")
                ssock.send(msg.encode())
                data = ssock.recv(1024).decode()
                print(f"[Mensaje recibido] {data}")

if __name__ == "__main__":
    role = input("¿Ejecutar terminal como server (s) o cliente (c)? ").strip().lower()
    if role == "s":
        run_server()
    else:
        run_client()
