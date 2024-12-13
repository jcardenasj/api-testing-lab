import requests
from behave import given, when, then
from datetime import datetime

BASE_URL = "http://localhost:3000"

@given('que el usuario tiene el origen "{origen}" y el destino "{destino}"')
def step_given_usuario_tiene_origen_destino(context, origen, destino):
    context.origen = origen
    context.destino = destino

@given('selecciona la fecha "{fecha}"')
def step_given_usuario_selecciona_fecha(context, fecha):
    try:
        context.fecha = datetime.strptime(fecha, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Fecha inválida")

@when('realiza la búsqueda de vuelos')
def step_when_usuario_realiza_busqueda(context):
    # Construir la URL con los parámetros
    url = f"{BASE_URL}/search_flights?origen={context.origen}&destino={context.destino}&fecha={context.fecha}"
    
    # Hacer la solicitud GET
    response = requests.get(url)

    # Validar respuesta
    if response.status_code == 200:
        context.resultado = response.json()  # Guardar vuelos disponibles
        print(context.resultado)
    else:
        raise Exception(f"Error en la búsqueda de vuelos: {response.status_code} - {response.text}")


@then('debe mostrarse una lista de vuelos disponibles')
def step_then_lista_vuelos_disponibles(context):
    resultado = context.resultado
    
    assert len(resultado) == 2, "Debe retornar dos elementos en la lista"

    ele1 = resultado[0]
    ele2 = resultado[1]
    
    assert ele1["vuelo_id"] == 'IB123', "IB123 es el id del primer vuelo"
    assert ele2["vuelo_id"] == 'IB124', "IB124 es el id del primer vuelo"
