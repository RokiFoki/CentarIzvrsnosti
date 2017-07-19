import http.server
from six.moves.BaseHTTPServer import HTTPServer

PORT = 8000

# najjednostanviji server koji samo preda index.html iz trenutnog direktorija (mape)
Server = http.server.SimpleHTTPRequestHandler

# pokreni server
httpd = HTTPServer(("", PORT), Server)
httpd.serve_forever()