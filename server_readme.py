from http.server import HTTPServer, BaseHTTPRequestHandler
import markdown
import os
import signal
import sys

# run this script to start a simple HTTP server that serves the README_dev.md file as HTML:
# python server_readme.py
# http://localhost:8000/


README_PATH = os.path.join(os.path.dirname(__file__), "README_dev.md")

# клас обробника запитів HTTP
class ReadmeHandler(BaseHTTPRequestHandler):
    def do_GET(self): 
        if self.path == "/":
            if not os.path.exists(README_PATH): # перевірка наявності README.md
                self.send_response(404) # якщо файл не знайдено, повертаємо 404
                self.send_header("Content-type", "text/plain; charset=utf-8")  
                self.end_headers() 
                self.wfile.write(b"README.md not found") # відправка повідомлення про помилку
                return

            with open(README_PATH, "r", encoding="utf-8") as f:
                md_text = f.read()
                
            # конвертація Markdown в HTML
            html = markdown.markdown(md_text, extensions=["fenced_code", "tables"])

            # Auto-reload script (optional). Uncomment to enable auto-reload every 5 seconds. AND ADD -> {auto_reload_script}

            # auto_reload_script = """
            # <script>
            #     setTimeout(() => {
            #         location.reload();
            #     }, 5000);
            # </script>
            # """
            
            # формування HTML з CSS стилями та кнопкою перезавантаження
            full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>README Preview</title>
    <!-- GitHub Markdown CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
    <style>
        body {{
            display: flex;
            justify-content: center;
            padding: 2rem;
            background: #f5f5f5;
        }}
        .container {{
            max-width: 980px;
            width: 100%;
        }}
        .button-bar {{
            display: flex;
            justify-content: flex-end;
            margin-bottom: 1em;
        }}
        .reload-button {{
            padding: 0.5em 1em;
            background: #2c974b;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1em;
        }}
        .markdown-body {{
            box-sizing: border-box;
            min-width: 200px;
            width: 100%;
            padding: 45px;
            background: white;
            border: 1px solid #ddd;
            border-radius: 6px;
        }}
    </style>
</head>
<body>
<div class="container">
    <div class="button-bar">
<button class="reload-button" onclick="location.reload()"> Refresh page </button>
    </div>
    <article class="markdown-body">
        {html}
    </article>
</div>
</body>
</html>
"""
            # відправка відповіді з HTML
           
            self.send_response(200) 
            self.send_header("Content-type", "text/html; charset=utf-8") 
            self.end_headers()  
            self.wfile.write(full_html.encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Not Found")

# функція для запуску сервера
def run(server_class=HTTPServer, handler_class=ReadmeHandler, port=8000):
    server_address = ('', port) 
    httpd = server_class(server_address, handler_class) # створення сервера

    # обробник сигналу для коректного завершення роботи сервера
    def signal_handler(sig, frame):
        print("\n Server shutdown...")
        httpd.server_close()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)  # обробка Ctrl+C для завершення сервера

    print(f"Serving README_dev.md at http://localhost:{port}")
    httpd.serve_forever()  # запуск сервера

if __name__ == "__main__":
    run()
