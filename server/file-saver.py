from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qsl, urlparse

class RequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    #print('do_GET')
    message = dict(parse_qsl(urlparse(self.path).query))['msg']
    #print('GET message=' + message)
    # Could implement messages to delete all saved files, merge all files into one, etc.
    self.send_response(200)
    self.send_header("Content-Type", "application/json")
    self.end_headers()

  def do_POST(self):
    #print('do_POST')
    content_disposition = self.headers.get("Content-Disposition")
    content_disposition_split = content_disposition.split('"')
    # For security, content_disposition (and especially filename) should be parsed carefully. That isn't done here.
    filename = content_disposition_split[1]   # assume content_disposition is formatted normally, and filename is valid
    content_length = int(self.headers.get("Content-Length", 0))
    content = self.rfile.read(content_length)

    with open(filename, 'wb') as file:
      file.write(content)

    self.send_response(200)
    self.send_header("Content-Type", "application/json")
    self.end_headers()

server = HTTPServer(("0.0.0.0", 8000), RequestHandler)
print('Server running')
server.serve_forever()
