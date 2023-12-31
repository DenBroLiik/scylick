import serial
import http.server
import socketserver
import os
import gc

# from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
os.environ['PYTHONGC'] = '1'
gc.collect()








# Подключение к Arduino Uno на COM4 
# arduino_1 = serial.Serial('COM4', 512)  

# Подключение к Arduino Uno на COM5
arduino_2 = serial.Serial('COM5', 512)
# # Установите правильный порт для подключения к Arduino Uno
# arduino_port = 'COM5'

# # Установите правильную скорость передачи данных
# baud_rate = 9600

# # Подключение к Arduino
# arduino = serial.Serial(arduino_port, baud_rate)

# Класс для обработки запросов к серверу
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Обработка запроса
        ...
        # Очистка памяти после обработки запроса
        gc.collect()



        # Пример команды для отправки данных на Arduino
        # arduino_1.write(b'1')  # Отправка данных "1" на Arduino 

        arduino_2.write(b'2') # Отправка данных "2" на Arduino
        self.send_response(200)
        # self.send_header('Content-type', 'text/html')
        # self.end_headers()
        # self.wfile.write(b'Server is running')
        

# class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
            
    # def do_GET(self):
        url = urlparse(self.path)
        if url.path.endswith('.ico') or url.path.endswith('.png') or url.path.endswith('.jpg') or url.path.endswith('.webp') or url.path.endswith('.html'):
            # Обработка запросов к файлам изображений
            file_path = '.' + url.path
            if os.path.isfile(file_path):
                self.send_response(200)
                self.send_header('Content-type', 'image/x-icon')
                self.send_header('Content-type', 'image/png')
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                with open(file_path, 'rb') as file:
                    self.wfile.write(file.read())
            else:
                # Отправка страницы 404.html в случае ошибки 404
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.send_header('Content-type', 'image/x-icon')
                self.send_header('Content-type', 'image/png')
                self.end_headers()
                with open('404.html', 'rb') as file:
                    self.wfile.write(file.read())
        else:
            # Обработка других запросов (например, к HTML-файлам)
            self.send_response(200)
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())

# Запуск сервера на порту 8000
with socketserver.TCPServer(("", 8000), MyHandler) as httpd:
    print("Server is running on port 8000")
    httpd.serve_forever()
    
