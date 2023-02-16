# I2C Interface, genuine Micropython

from board.bohei import Board
#from config import Config
#from display import Display
from ewh_net import Network
from heartbeat import Heartbeat
from name import Name
#from mqtt import MQTT
from task import Scheduler
#import ntptime


from bme680i import BME680_I2C
from machine import I2C, Pin
import time
bme = BME680_I2C(I2C(-1, Pin(22), Pin(21)))


network = Network()
board = Board(network)
board.init()

heartbeat = Heartbeat(board.display)


scheduler = Scheduler()

name = Name(board.display)
scheduler.register(board.display)
scheduler.register(heartbeat)
scheduler.register(network)

print("Starting scheduler!")

scheduler.start(100)

# #for _ in range(3):
# while True:
#     print(bme.temperature, bme.humidity, bme.pressure, bme.gas)
#     time.sleep(1)