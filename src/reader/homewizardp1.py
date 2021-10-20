import requests

class HomewizardP1:
    def __init__(self, config):
        self.config = config

    def getData(self):
        response = requests.get(f"{self.config['url']}{self.config['url_path']}").json()
        dataDict = {
            "total_high_energy": response['total_power_import_t2_kwh'],
            "total_low_energy": response['total_power_import_t1_kwh'],
            "current_energy": response['active_power_w'],
            "gas": response["total_gas_m3"]
        }
        return dataDict