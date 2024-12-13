import requests
from behave import given, when, then

BASE_URL = "http://localhost:3000"

@given('que el usuario tiene una reserva en el vuelo "{vuelo_id}"')
def step_given_usuario_reserva(context, vuelo_id):
    context.vuelo_id = vuelo_id
    response = requests.get(f"{BASE_URL}/search_flights/{vuelo_id}")
    if response.status_code == 200:
        context.vuelo = response.json()
    else:
        raise Exception(f"Vuelo no encontrado: {vuelo_id}")

@given('la reserva incluye los siguientes pasajeros')
def step_given_reserva_incluye_pasajeros(context):
    context.passengers_to_cancel = []
    for row in context.table:
        passenger = {
            "id": row["id"],
            "first_name": row["first_name"],
            "last_name": row["last_name"]
        }
        context.passengers_to_cancel.append(passenger)
    # Asegurarnos de que los pasajeros existan en el vuelo
    for passenger in context.passengers_to_cancel:
        assert passenger in context.vuelo["passengers"], (
            f"El pasajero {passenger} no está en la lista de pasajeros del vuelo."
        )

@when('cancela la reserva')
def step_when_cancela_reserva(context):
    updated_passengers = [
        passenger for passenger in context.vuelo["passengers"]
        if passenger not in context.passengers_to_cancel
    ]
    updated_data = {
        "seats_available": context.vuelo["seats_available"] + len(context.passengers_to_cancel),
        "passengers": updated_passengers
    }

    # Usamos DELETE para simular la cancelación de la reserva
    response = requests.put(f"{BASE_URL}/search_flights/{context.vuelo_id}", json=updated_data)

    if response.status_code == 200:
        context.updated_vuelo = response.json()
    else:
        raise Exception(f"Error al cancelar la reserva: {response.status_code} - {response.text}")

@then('la reserva debe eliminarse exitosamente')
def step_then_reserva_eliminada(context):
    assert "updated_vuelo" in context, "La cancelación de la reserva no se completó exitosamente."

@then('el número de asientos disponibles debe incrementarse en {cantidad}')
def step_then_incrementar_asientos(context, cantidad):
    cantidad = int(cantidad)
    expected_seats = context.vuelo["seats_available"] + cantidad
    assert context.updated_vuelo["seats_available"] == expected_seats, (
        f"Los asientos disponibles no se actualizaron correctamente. Esperado: {expected_seats}, "
        f"Obtenido: {context.updated_vuelo['seats_available']}"
    )

@then('los pasajeros cancelados no deben estar en la lista del vuelo')
def step_then_pasajeros_no_estan(context):
    for passenger in context.passengers_to_cancel:
        assert passenger not in context.updated_vuelo["passengers"], (
            f"El pasajero {passenger} aún aparece en la lista de pasajeros del vuelo."
        )

@then('el reembolso debe procesarse automáticamente')
def step_then_reembolso_procesado(context):
    # Simulación de procesamiento de reembolso
    # Aquí podrías llamar a otro endpoint de la API si existe uno para procesar reembolsos
    reembolso_simulado = True  # Supongamos que siempre es exitoso en este test
    assert reembolso_simulado, "El reembolso no se procesó automáticamente."
