```
Author: Sharath Nair
License : Apache 2.0 (excluding API keys)
Email : nair.sharath777@gmail.com
```

#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
import requests

google_key='AIzaSyAhuw_1fMW7SCq12HxU2GaY1Fvaex3mxWk'
mapquest_key='tK0qedxCP39H0Nfvb37xe2c5mr5eMmJg'

def get_from_primary(location):
        lat_lng={}
        req = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' %(location, google_key))
        result = req.json()
        if result['status'] == 'OK':
                lat_lng=result['results'][0]['geometry']['location']
                return lat_lng
        else:
                lat_lng=get_from_secondary(location)

        return lat_lng

def get_from_secondary(location):
        lat_lng={} 
        req = requests.get('http://www.mapquestapi.com/geocoding/v1/address?key=%s&location=%s' %(mapquest_key,location))
        result = req.json()
        lat_lng=result['results'][0]['locations'][0]['latLng']
        return lat_lng


class LocationService(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
        self._set_headers()
        print self.path
        print parse_qs(self.path[2:])
        self.wfile.write("<html><body><h1>Location Service</h1></body></html>")
    def do_POST(self):
        content_len = int(self.headers.getheader('content-length'))
        post_data = self.rfile.read(content_len)
        self.send_response(200)
        self.end_headers()
        location=json.loads(post_data)
        lat_lng=get_from_primary(location['address'])
        if len(lat_lng)==0:
        	self.wfile.write("<html><body><h1>Location Not Found</h1></body></html>")
        else:
        	self.wfile.write("<html><body><h1>Latitude=%s Longitude=%s</h1></body></html>" % (lat_lng['lat'],lat_lng['lng']))
        return

def run(server_class=HTTPServer, handler_class=LocationService, port=3024):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Server running at localhost:3024...'
    httpd.serve_forever()

run()
