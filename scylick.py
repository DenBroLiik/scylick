import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
            
    def do_GET(self):
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

httpd = HTTPServer(('localhost', 1404), SimpleHTTPRequestHandler)
httpd.serve_forever()







