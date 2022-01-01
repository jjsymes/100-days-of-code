class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, id, city, lowest_price=0.0, iata_code="") -> None:
        self.id = id
        self.city = city
        self.iata_code = iata_code
        self.lowest_price = lowest_price
    
    @classmethod
    def from_dict(cls, flight_data_as_dict):
        return cls(id=flight_data_as_dict['id'], city=flight_data_as_dict['city'], iata_code=flight_data_as_dict['iataCode'], lowest_price=flight_data_as_dict['lowestPrice'])

    def to_dict(self):
        return {
            "city": self.city,
            "iataCode": self.iata_code,
            "lowestPrice": self.lowest_price
        }
