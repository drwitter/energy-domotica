import time

from utilities import utils
from reader import homewizardp1

print("Setup")

config = utils.load_config()

p1Meter = homewizardp1.HomewizardP1(config['homewizard']['p1'])

while True:
    print(p1Meter.getData())
    time.sleep(5)