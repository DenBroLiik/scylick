# import os
# from http.server import HTTPServer, BaseHTTPRequestHandler
# from urllib.parse import urlparse
# import threading
# import requests
# import time

# class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
            
#     def do_GET(self):
#         url = urlparse(self.path)
#         if url.path.endswith('.ico') or url.path.endswith('.mp4') or url.path.endswith('.mp3') or url.path.endswith('.png') or url.path.endswith('.jpg') or url.path.endswith('.webp') or url.path.endswith('.html'):
#             # Обработка запросов к файлам изображений
#             file_path = '.' + url.path
#             if os.path.isfile(file_path):
#                 self.send_response(200)
#                 self.send_header('Content-type', 'image/x-icon')
#                 self.send_header('Content-type', 'image/png')
#                 self.send_header('Content-type', 'image/jpeg')
#                 self.send_header('Content-type', 'image/jpg')
#                 self.send_header('Content-type', 'text/html')
#                 self.end_headers()
#                 with open(file_path, 'rb') as file:
#                     self.wfile.write(file.read())
#             else:
#                 # Перенаправление на страницу 404.html в случае ошибки 404
#                 self.send_response(302)
#                 self.send_header('Location', '/404.html')
#                 self.end_headers()
#         elif url.path.endswith('/503'):
#             # Имитация ошибки 503 и перенаправление на страницу 503.html
#             self.send_response(503)
#             self.send_header('Content-type', 'text/html')
#             self.end_headers()
#             with open('503.html', 'rb') as file:
#                 self.wfile.write(file.read())
#         else:
#             # Обработка других запросов (например, к HTML-файлам)
#             self.send_response(200)
#             self.end_headers()
#             with open('index.html', 'rb') as file:
#                 self.wfile.write(file.read())

# def run_server(port, handler_class=SimpleHTTPRequestHandler):
#     server_address = ('', port)
#     httpd = HTTPServer(server_address, handler_class)
#     httpd.serve_forever()

# # def check_server(server_url):
# #     try:
# #         response = requests.get(server_url, timeout=2)
# #         return response.status_code == 200
# #     except requests.exceptions.RequestException:
# #         return False

# # Запуск первого сервера
# threading.Thread(target=run_server, args=[1404]).start()

# # Запуск второго сервера
# threading.Thread(target=run_server, args=[80]).start()

# # while True:
# #     time.sleep(1)  # Проверка каждую секунду
# #     if not check_server('http://localhost:1404'):
# #         print("Перенаправление на сервер 2")
# #         # Ваш код для перенаправления здесь
# #         response = requests.get('http://localhost:1405')
# #         print(response.text)
# #     elif not check_server('http://localhost:1405'):
# #         print("Перенаправление на сервер 1")
# #         # Ваш код для перенаправления здесь
# #         response = requests.get('http://localhost:1404')
# #         print(response.text)

# # httpd = HTTPServer(('localhost', 1404), SimpleHTTPRequestHandler)
# # httpd.serve_forever()

from flask import Flask, send_from_directory, redirect, abort
import threading
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def send_file(path):
    try:
        if path.endswith(('.ico', '.mp4', '.mp3', '.png', '.jpg', '.webp', '.html')):
            return send_from_directory('.', path)
        elif path.endswith('/503'):
            abort(503)
        else:
            return send_from_directory('.', path)
    except FileNotFoundError:
        return redirect('/404.html')

def run_server(port):
    app.run(port=port)

# Запуск первого сервера
threading.Thread(target=run_server, args=[1404]).start()

# Запуск второго сервера
threading.Thread(target=run_server, args=[80]).start()
