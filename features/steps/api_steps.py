from behave import given, when, then
import requests

headers = {
    "x-api-key": "pub_3cb50d49e26ede1c2237630a0d1628c1c565e3bd444b60d1a91dee87d1061daf"
}

@given("la API de Reqres esta disponible")
def step_acceder_api(context):
    context.base_url = "https://reqres.in/api"

#Scenario 1
@when("se realiza un login valido")
def step_login(context):
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    context.response = requests.post(
                    f"{context.base_url}/login",
                    headers=headers,
                    json=body
    )


@then("el status code debe ser {status_code:d}")
def step_impl(context, status_code):
    print(f"status:{context.response.status_code}")
    assert context.response.status_code == status_code


#Scenario 2
@when("se realiza un login sin contraseña")
def step_login_sin_contraseña(context):
    body = {
        "email": "eve.holt@reqres.in"
    }

    context.response = requests.post(
                    f"{context.base_url}/login",
                    headers=headers,
                    json=body
    )

@then("el mensaje de error debe ser '{mensaje}'")
def step_validacion_mensaje(context, mensaje):
    body = context.response.json()
    
    assert body["error"] == mensaje

