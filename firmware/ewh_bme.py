from bme680i import BME680_I2C
from machine import I2C, Pin
from task import Task

class BMESensor(Task):

    def __init__(self, display):
        super().__init__()
        
        self.display = display
        self.scl = 22
        self.sda = 21
        self.bme = BME680_I2C(I2C(-1, 
            Pin(self.scl), 
            Pin(self.sda)))
        print("BME Initialiszing ...")
        self.status = None
        self.bme_msg = "Init ..."

    def update(self, scheduler):
        status = "Reading ..."
        self.bme_msg = status
        self.bme.temperature
        self.bme.humidity
        self.bme.gas
        #self.display.text('{}'.format(self.bme_msg), 0)
        self.display.text('Temp C{:10.2f}'.format(self.bme.temperature), 1)
        self.display.text('Hum % {:10.2f}'.format(self.bme.humidity), 2)
        self.display.text('Gas   {:10.0f}'.format(self.bme.gas), 3)
        self.status = status
