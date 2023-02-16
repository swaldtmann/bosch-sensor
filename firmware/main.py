#
# this script assumes the default connection of the I2C bus
# On pycom devuces that is P9 = SDA, P10 = scl
#
from machine import I2C, Pin
import bme280_float as bme280

i2c = I2C(-1, Pin(22), Pin(21))
bme = bme280.BME280(i2c=i2c)

print(bme.values)
