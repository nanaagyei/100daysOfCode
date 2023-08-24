from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta


# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_sheet_data()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

for row in sheet_data:
    if row['iataCode'] == "":
        city = row['city']
        iataCode = flight_search.get_iatacode(city)
        row['iataCode'] = iataCode

data_manager.response_data = sheet_data
data_manager.update_sheet_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_email(
            message=f"Low price alert! Only ${flight.price} to "
                    f"fly from {flight.origin_city}-{flight.origin_airport} to "
                    f"{flight.destination_city}-{flight.destination_airport}, "
                    f"from {flight.out_date} to {flight.return_date}."
            )
