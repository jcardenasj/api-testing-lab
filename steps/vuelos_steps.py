import requests
from behave import given, when, then

@given(u'un trayecto "{trayecto}"')
def step_impl(context, trayecto):
    raise NotImplementedError(u'STEP: Given un trayecto "MAD -> NYC"')


@given(u'una fecha valida de busqueda "{fecha}"')
def step_impl(context, fecha):
    raise NotImplementedError(u'STEP: Given una fecha valida de busqueda "2024-12-15"')


@when(u'hago una solicitud de busqueda')
def step_impl(context):
    raise NotImplementedError(u'STEP: When hago una solicitud de busqueda')


@then(u'la respuesta debe contener 1 lista de vuelos en la fecha establecidas')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then la respuesta debe contener 1 lista de vuelos en la fecha establecidas')