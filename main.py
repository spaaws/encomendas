import http.server
import socketserver

class PingPongHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Verifica se a URL é /ping
        if self.path == '/ping':
            # Define o código de resposta HTTP (200 OK)
            self.send_response(200)
            # Define os headers
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Envia a resposta com o texto "pong"
            self.wfile.write(b'{"message": "pong"}')
        else:
            # Responde com 404 se a rota não for /ping
            self.send_response(404)
            self.end_headers()

# Configurando o servidor
PORT = 8080
with socketserver.TCPServer(("", PORT), PingPongHandler) as httpd:
    print(f"Servidor rodando na porta {PORT}")
    httpd.serve_forever()