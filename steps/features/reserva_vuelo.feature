Feature: Reserva de vuelos
Como usuario
Quiero obetener información precisa
Para reservar vuelos

    Scenario: Reservar 3 asientos en un vuelo
        Given que el usuario tiene el vuelo "IB125"
        And hay al menos 3 asientos disponibles en el vuelo
        When realiza una reserva con los siguientes pasajeros:
        | id     | first_name | last_name    |
        | P007   | Carlos     | Fernandez    |
        | P008   | Lucia      | Martinez     |
        | P009   | Andres     | Gutierrez    |
        Then la reserva debe completarse exitosamente

