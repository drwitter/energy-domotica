import requests
import time

class HomewizardP1:
    def __init__(self, config):
        self.config = config

    def getData(self):
        try:
            response = requests.get(f"{self.config['url']}{self.config['url_path']}").json()
            dataDict = {
                "total_high_energy": response['total_power_import_t2_kwh'],
                "total_low_energy": response['total_power_import_t1_kwh'],
                "current_energy": response['active_power_w'],
                "gas": response["total_gas_m3"]
            }
        except:
            dataDict = {
                "total_high_energy": 0.0,
                "total_low_energy": 0.0,
                "current_energy": 0.0,
                "gas": 0.0
            }
        

        return dataDict