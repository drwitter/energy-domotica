import time

from utilities import utils
from reader import homewizardp1
from writer.database import database

from writer.database.models import P1Meter

config = utils.load_config()

p1Meter = homewizardp1.HomewizardP1(config['homewizard']['p1'])

# time.sleep(5)

db = database.Database(config["database"]["db"])

print(db.get_last(P1Meter.P1Meter, P1Meter.P1Meter.timestamp))

while True:
    data = p1Meter.getData()
    db_object = P1Meter.P1Meter(timestamp = int(time.time()), total_high_energy = data['total_high_energy'], total_low_energy = data['total_low_energy'],current_energy = data['current_energy'], gas = data['gas'])
    db.write(db_object)
    print(db.count(P1Meter.P1Meter, P1Meter.P1Meter.timestamp))
    time.sleep(5)