import requests
from behave import given, when, then

@given('unas fechas validas de busqueda')
def step_server_active(context):
    context.base_url = "http://localhost:3000"

@when('hago una solicitud GET a "{endpoint}"')
def step_make_get_request(context, endpoint):
    response = requests.get(f"{context.base_url}{endpoint}")
    context.response = response

@then('la respuesta debe contener {count} elemento')
def step_validate_response(context, count):
    response_json = context.response.json()
    assert len(response_json) == int(count), f"Esperado {count} elementos pero obtuve {len(response_json)}"