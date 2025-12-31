import os, requests
class DataManager:
    def __init__(self):
        self.sheety_get_url = "https://api.sheety.co/f4a17d20847a70d523db1ab18b2fc444/unbenannteTabelle/tabellenblatt1"
        self.sheety_put_url = "https://api.sheety.co/f4a17d20847a70d523db1ab18b2fc444/unbenannteTabelle/tabellenblatt1"
        self.sheety_authorization = os.environ["sheety_authorization"]
    def response_city_names(self):
        headers = {
            "Authorization": self.sheety_authorization
        }
        response = requests.get(url=self.sheety_get_url,headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["tabellenblatt1"]
    def insert_iata_code(self, dic):
        headers = {
            "Authorization": self.sheety_authorization
        }
        n = 2
        for item, value in dic.items():
            body = {
                "tabellenblatt1": {
                    "iataCode": value
                }
            }
            response = requests.put(url=f"{self.sheety_get_url}/{n}", json= body, headers=headers)
            response.raise_for_status()
            n += 1