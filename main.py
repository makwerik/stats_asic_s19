import requests
import json


class S19:
    def __init__(self):
        """Load headers"""
        try:
            with open('data/auth.json', encoding='utf8') as file:
                self.headers = json.load(file)
        except:
            print("Account information is missing")

    def stats(self):
        """Get stats asic"""
        response = requests.get('http://192.168.0.40/cgi-bin/stats.cgi', headers=self.headers).json()

        print(f'Fan Speed : {response.get("STATS")[0].get("fan")}')

        for i in range(0,3):
            print(f'CHIP STATUS BOARD-{i} : {response.get("STATS")[0].get("chain")[i].get("temp_chip")}')
            print(f'PCB STATUS BOARD-{i} : {response.get("STATS")[0].get("chain")[i].get("temp_pcb")}')


if __name__ == '__main__':
    s = S19()
    s.stats()
