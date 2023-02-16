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
from ewh_bme import BMESensor

network = Network()
board = Board(network)
board.init()

bmesensor = BMESensor(board.display)
heartbeat = Heartbeat(board.display)

scheduler = Scheduler()

name = Name(board.display)
scheduler.register(board.display)
scheduler.register(heartbeat)
scheduler.register(network)
scheduler.register(bmesensor)

print("Starting scheduler!")

scheduler.start(100)
