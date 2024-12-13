Feature: Búsqueda de vuelos

  Scenario: Obtener todos los posts
    Given el servidor está activo
    When hago una solicitud GET a "/posts"
    Then la respuesta debe contener 1 elemento