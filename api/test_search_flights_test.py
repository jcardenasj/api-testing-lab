import unittest
from api.service import InvalidDateException, search_flights, InvalidOriginException, InvalidDestinationException, book_flight

class TestSearchFlights(unittest.TestCase):

    def test_WhenSearchFlights_ExpectFlightsFound(self):
        # Arrange
        origen = "MAD"
        destino = "NYC"
        fecha = "2024-12-15"

        # Act
        result = search_flights(origen, destino, fecha)

        # Assert
        assert len(result) > 0
        for flight in result:
            assert flight["origen"] == origen
            assert flight["destino"] == destino
            assert flight["fecha"] == fecha

    def test_WhenSearchFlightInvalidorigen_ExpectInvalidOriginException(self):
        # Arrange
        cases = ["Invalid", None, ""]


        # Act
        for origen in cases:
            with self.assertRaises(InvalidOriginException) as c:
                self.assertEqual(search_flights(origen, "NYC", "2024-12-15"), None)
                self.assertEqual(str(c.exception), "Invalid origin")

    
    def test_WhenSearchFlightInvaliddestino_ExpectInvalidDestinationE(self):
        # Arrange
        cases = ["Invalid", None, ""]


        # Act
        for destino in cases:
            with self.assertRaises(InvalidDestinationException) as c:
                self.assertEqual(search_flights("MAD", destino, "2024-12-15"), None)
                self.assertEqual(str(c.exception), "Invalid destination")
    
    def test_WhenSearchFlightInvalidFecha_ExpectInvalidDateE(self):
        # Arrange
        cases = ["Invalid", None, "", "15-12-2024", "2024-15-12", "2024-12-15T12:00:00", "2024-12-15 12:00:00"]


        # Act
        for fecha in cases:
            with self.assertRaises(InvalidDateException) as c:
                self.assertEqual(search_flights("MAD", "NYC", fecha), None)
                self.assertEqual(str(c.exception), "Invalid date")


    def testBookFlight_WhenValidPassenger_ExpectsPassengerAdded(self):
        # Arrange
        vuelo_id = "IB123"
        passenger = { "id": "P007", "first_name": "Jose", "last_name": "Garcia" }

        # Act
        flight = book_flight(vuelo_id, passenger)

        # Assert
        self.assertEqual(passenger in flight["passengers"], True)

    def testBookFlight_WhenInvalidFlightId_ExpectsNone(self):
        # Arrange
        vuelo_id = "IB000"
        passenger = { "id": "P007", "first_name": "Jose", "last_name": "Garcia" }

        # Act
        flight = book_flight(vuelo_id, passenger)

        # Assert
        self.assertEqual(flight, None)

    def testBookFlight_WhenNotEnoughSeats_ExpectsNone(self):
        # Arrange
        vuelo_id = "IB1234"
        passenger = { "id": "P007", "first_name": "Jose", "last_name": "Garcia" }

        # Act
        flight = book_flight(vuelo_id, passenger)

        # Assert
        self.assertEqual(flight, None)