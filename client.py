from http import client
from iiot_device import Sensor
import json
import time


#The creation of an object with destination to the class HTTPConnection
_conn = client.HTTPConnection(host='localhost', port=5000)

#This is the creation of the object to the class Sensor, that we are gonna use
s = Sensor()

#To make the JSON that the server receives
j = {'Content-type': 'application/json'}

while True:

    data = {
        'id' : 1,
        'name' : 'Temp_Sensor',
        'value' : s.get_random_number()
    }

    json_data = json.dumps(data)

    # The way that we send the data to the server
    _conn.request('POST', '/devices', json_data, headers=j)
    _conn.close()


    #print(s.get_random_number())

    val_S = data['value']
    if val_S < 15:
        print(val_S, "the sensor detects less than 15")
    else: 
        print(val_S, "the sensor detects more than 15")

    #print(s.get_temp_wmi())
    time.sleep(.5)

