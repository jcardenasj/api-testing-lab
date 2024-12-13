import datetime
FLIGHTS = [
    {
    "vuelo_id": "IB123",
    "origen": "MAD",
    "destino": "NYC",
    "fecha": "2024-12-15",
    "seats_available": 50,
    "passengers": [
        { "id": "P001", "first_name": "Juan", "last_name": "Perez" },
        { "id": "P002", "first_name": "Ana", "last_name": "Gomez" }
    ]
    },
    {
    "vuelo_id": "IB1234",
    "origen": "MAD",
    "destino": "NYC",
    "fecha": "2024-12-15",
    "seats_available": 0,
    "passengers": [
        { "id": "P001", "first_name": "Juan", "last_name": "Perez" },
        { "id": "P002", "first_name": "Ana", "last_name": "Gomez" }
    ]
    },
    {
    "vuelo_id": "IB124",
    "origen": "MAD",
    "destino": "NYC",
    "fecha": "2024-12-15",
    "seats_available": 30,
    "passengers": [
        { "id": "P003", "first_name": "Luis", "last_name": "Martinez" },
        { "id": "P004", "first_name": "Maria", "last_name": "Lopez" }
    ]
    },
    {
    "vuelo_id": "IB125",
    "origen": "MAD",
    "destino": "BCN",
    "fecha": "2024-12-20",
    "seats_available": 20,
    "passengers": [
        { "id": "P005", "first_name": "Carlos", "last_name": "Hernandez" },
        { "id": "P006", "first_name": "Sofia", "last_name": "Diaz" }
    ]
    }
]

PLACES = ["MAD", "NYC", "BCN"]

class InvalidOriginException(Exception):
    def __str__(self):
        return "Invalid origin"
    
class InvalidDestinationException(Exception):
    def __str__(self):
        return "Invalid destination"

class InvalidDateException(Exception):
    def __str__(self):
        return "Invalid date"

def search_flights(origen, destino, fecha):
    if origen not in PLACES:
        raise InvalidOriginException()
    
    if destino not in PLACES:
        raise InvalidDestinationException()
    
    #validate date has format YYYY-MM-DD
    try:
        datetime.datetime.strptime(fecha, '%Y-%m-%d')
    except Exception:
        raise InvalidDateException()
    
    flights = list(filter(lambda flight: flight['origen'] == origen and flight['destino'] == destino and flight['fecha'] == fecha, FLIGHTS))
    return flights


def book_flight(vuelo_id, passenger):
    flight = list(filter(lambda flight: flight['vuelo_id'] == vuelo_id, FLIGHTS))
    if not flight:
        return None
    flight = flight[0]
    if flight["seats_available"] == 0:
        return None
    flight["passengers"].append(passenger)
    flight["seats_available"] -= 1
    return flight

    