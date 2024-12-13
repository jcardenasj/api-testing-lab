import requests
from behave import given, when, then

BASE_URL = "http://localhost:3000"

@given(u'que el usuario tiene el vuelo "{vuelo_id}"')
def step_given_usuario_tiene_vuelo(context, vuelo_id):
    context.vuelo_id = vuelo_id
    response = requests.get(f"{BASE_URL}/search_flights?vuelo_id={vuelo_id}")
    if response.status_code == 200:
        context.vuelo = response.json()[0]
    else:
        raise Exception(f"Vuelo no encontrado: {vuelo_id}")


@given(u'hay al menos {cantidad} asientos disponibles en el vuelo')
def step_given_asientos_disponibles(context, cantidad):
    context.cantidad = int(cantidad)

# @when(u'realiza una reserva con los siguientes pasajeros: {table}')
@when(u'realiza una reserva con los siguientes pasajeros')
def step_when_reserva_pasajeros(context):
    passengers = []
    for row in context.table:
        passengers.append({
            "id": row["id"],
            "first_name": row["first_name"],
            "last_name": row["last_name"]
        })
    
    context.new_passengers = passengers
    payload = {
        "vuelo_id": context.vuelo_id,
        "origen": context.vuelo['origen'],
        "destino": context.vuelo['destino'],
        "fecha": context.vuelo['fecha'],
        "seats_available": context.vuelo['seats_available'],
        "passengers": passengers
    }
    
    response = requests.post(f"{BASE_URL}/search_flights?vuelo_id={context.vuelo_id}", json=payload)
    print(response)

    if response.status_code == 200 or response.status_code == 201:
        context.updated_vuelo = response.json()
    else:
        raise Exception(f"Error al realizar la reserva: {response.status_code} - {response.text}")

@then(u'la reserva debe completarse exitosamente')
def step_then_reserva_exitosa(context):
    assert "updated_vuelo" in context, "La reserva no se completó exitosamente."

# @then(u'el número de asientos disponibles debe reducirse en 3')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then el número de asientos disponibles debe reducirse en 3')

# @then(u'los nuevos pasajeros deben aparecer en la lista del vuelo')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then los nuevos pasajeros deben aparecer en la lista del vuelo')

# # Base de datos simulada
# flight_data = {
#     "23": {"status": "completamente reservado", "price": None},
#     "24": {"status": "disponible", "price": 250}
# }

# @given('un ID de vuelo seleccionado "{vuelo_id}"')
# def step_given_vuelo_id(context, vuelo_id):
#     context.vuelo_id = vuelo_id

# @when(u'usuario envía una nueva solicitud de reserva')
# def step_when_user_sends_reservation_request(context):
#     flight = context.flight_info
#     if flight["status"] == "completamente reservado":
#         context.response_message = "El vuelo está completamente reservado. No se puede realizar la reserva."
#     elif flight["status"] == "disponible":
#         # Simular cambio de precio (por ejemplo, ajuste dinámico)
#         new_price = flight["price"] + 50  # Ajuste de precio
#         context.response_message = f"El precio del vuelo ha cambiado. Nuevo precio: ${new_price}"

# @then(u'retornar mensaje de cancelación por vuelo completamente reservado')
# def step_then_return_full_reservation_message(context):
#     assert "completamente reservado" in context.response_message
#     print(context.response_message)

# @then(u'devolver mensaje de información con nuevo precio de reserva')
# def step_then_return_price_change_message(context):
#     assert "Nuevo precio" in context.response_message
#     print(context.response_message)
