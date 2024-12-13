Feature: Cancelar reservas de vuelo
  Como usuario, quiero poder cancelar una reserva antes del vuelo
  para que se actualice la disponibilidad y se procese el reembolso.

  Scenario: Cancelar una reserva para 2 pasajeros
    Given que el usuario tiene una reserva en el vuelo "IB124"
    And la reserva incluye los siguientes pasajeros:
      | id     | first_name | last_name |
      | P003   | Luis       | Martinez |
      | P004   | Maria      | Martinez  |
    When cancela la reserva
    Then la reserva debe eliminarse exitosamente
    And el número de asientos disponibles debe incrementarse en 2
    And los pasajeros cancelados no deben estar en la lista del vuelo
    And el reembolso debe procesarse automáticamente