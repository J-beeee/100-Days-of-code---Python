from data_manager import DataManager
from flight_search import FlightSearch



datamanager = DataManager()
flight_search = FlightSearch()
#iata_dic = flight_search.get_iata(city_dic=datamanager.response_city_names())
#datamanager.insert_iata_code(iata_dic)
data = datamanager.response_city_names()
flight_data = flight_search.flight_offers(given_data=data)



