from random import randint
#import psutil
#import wmi

#POO en Python
#Class' definition
class Sensor:

    #Constructore de la clase
    def __init__(self):
        #Works for linux
        #self._sensor = psutil.cpu_percent()
        #Works for windows
        #self._wmi = wmi.WMI(namespace='root\OpenHardwareMonitor')
        pass

    def get_temp(self):
        return self._sensor['coretemp']

    #It simulates the taking of some value of another sensor that we have
    def get_random_number(self):
        return randint(0, 50)


    '''def get_temp_wmi(self):
        return self._wmi.SensorType['Temperature']'''
        