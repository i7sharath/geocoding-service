This code is a simple stab at developing a geocoding service. 
This service provides a REST http interface and uses two third party map APIs to resolve the request 
Google Maps and MapQuest have been used in this implementation . 

How to Use : 

A - Install the following modules : 

sudo pip install json \n
sudo pip install requests

B - Compile and run the server at port 3024 (port number can be changed !) 

python GetLocation.py

C - Sending Query with address using commandline

For eg: 
Address = 4941 Heather Drive
IP address(local) = 192.168.1.10 < you must use the IP of your local machine >

cmd = curl  192.168.1.10:3024 -H "Content-Type: application/json" -X POST -d '{"address":"4941 Heather Drive"}'


Sample Output : 
<html>
  <body>
    <h1>Latitude=42.3242698 Longitude=-83.2028284</h1>
  </body>
</html>

