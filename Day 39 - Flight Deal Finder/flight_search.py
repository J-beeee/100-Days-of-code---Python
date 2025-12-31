import os, requests, datetime, json


IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:
    def __init__(self):
        self.client_id = os.environ["amadeus-api-key"]
        self.client_secret = os.environ["amadeus-api-secret"]
        self.access_token = ""
        self.token_time = 0
    def get_token(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=data)
        response.raise_for_status()
        token = response.json()
        self.access_token = token["access_token"]
        self.token_time = datetime.datetime.today().timestamp()
        data = {
            "token": self.access_token,
            "time": self.token_time
        }
        with open("token.json", "w") as file:
            json.dump(data, file)


    def check_token(self):
        now = datetime.datetime.today().timestamp()
        try:
            with open(file="token.json", mode="r") as file:
                data = json.load(file)
                if (now - data["time"]) >= 1799:
                    print("Es wurde ein neuer Key erstellt")
                    self.get_token()
                else:
                    self.access_token = data["token"]
        except FileNotFoundError:
            print("no file")
            self.get_token()

    def get_iata(self, city_dic):
        self.check_token()
        iata_code_dic = {}
        for city in city_dic:
            city = city["city"].upper()
            data = {
                "keyword": city
            }
            header = {
                "Authorization": f"Bearer {self.access_token}"
            }
            response = requests.get(url=IATA_ENDPOINT, params=data, headers=header)
            response.raise_for_status()
            iata_code = response.json()
            iata_code = iata_code["data"][0]["iataCode"]
            iata_code_dic.update({city: iata_code})
        return iata_code_dic

    def flight_offers(self, given_data):
        self.check_token()
        start_date = datetime.date.today()
        header = {
            "Authorization": f"Bearer {self.access_token}"
        }
        lowest_price_fly = {}
        for item in given_data:
            lowest_price_fly.update({item["city"]: 10000, "day": "N/A"})
            for day_offset in range(180):
                check_date = start_date + datetime.timedelta(days=day_offset)
                date_str = check_date.strftime("%Y-%m-%d")
                data = {
                    "originLocationCode": "BER",
                    "destinationLocationCode": item["iataCode"],
                    "departureDate": date_str,
                    "adults": 1,
                    "currencyCode": "EUR",
                    "maxPrice": item["lowestPrice"]
                }
                response = requests.get(url=FLIGHT_ENDPOINT, params=data,headers=header)
                response = response.json()
                n = 0
                print(response)
                for data in response["data"]:
                    if float(data["price"]["total"]) < lowest_price_fly[item["city"]]:
                        lowest_price_fly.update({item["city"]: float(data["price"]["total"]), "day": data["lastTicketingDate"]})
                        n +=1
            print(f"{item['city']} - done")
            print(lowest_price_fly)

