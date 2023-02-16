#from bme680 import *
from machine import I2C, Pin
import time
i2c = I2C(-1, Pin(22), Pin(21))
print("YES")
i2c.scan()

#bme = BME680_I2C(I2C(-1, Pin(22), Pin(21)))
#for _ in range(3):
#    print(bme.temperature, bme.humidity, bme.pressure, bme.gas)
#    time.sleep(1)


