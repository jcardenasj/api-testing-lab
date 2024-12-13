Feature: Búsqueda de vuelos

  Scenario: Buscar vuelos con fechas válidas
    Given que el usuario tiene el origen "MAD" y el destino "NYC"
    And selecciona la fecha "2024-12-15"
    When realiza la búsqueda de vuelos
    Then debe mostrarse una lista de vuelos disponibles