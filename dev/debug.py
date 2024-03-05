from http.server import BaseHTTPRequestHandler, HTTPServer
import html

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # 创建一个包含 JavaScript 的 HTML 页面
        html_content = html.escape("<script>console.log('Hello, World!');</script>")
        self.wfile.write(html_content.encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()