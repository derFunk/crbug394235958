from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''
                <html>
                <body>
                <ol>    
                    <li><a href="/download-pkpasses">Download bundle.pkpasses</a> (works as expected)</li>
                    <li><a href="/download-pkpass">Download generic.pkpass</a> (works as expected)</li>
                    <li><a href="/download-order">Download test.order</a> (does not work as expected)</li>
                </ol>
                </body>
                </html>
            ''')
        elif self.path in ['/download-order', '/download-pkpasses', '/download-pkpass']:
            self.send_response(200)
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
            self.send_header('Pragma', 'no-cache')
            
            if self.path == '/download-order':
                content_type = 'application/vnd.apple.finance.order'
                filename = 'test.order'
            elif self.path == '/download-pkpasses':
                content_type = 'application/vnd.apple.pkpasses'
                filename = 'bundle.pkpasses'
            else:
                content_type = 'application/vnd.apple.pkpass'
                filename = 'generic.pkpass'
            
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
            self.end_headers()
            with open(filename, 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_error(404, 'File Not Found')

def run(server_class=HTTPServer, handler_class=CustomHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd server on port 8080...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
