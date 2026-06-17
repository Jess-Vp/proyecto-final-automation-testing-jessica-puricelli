import pytest
import pytest_check as check
import requests

headers = {
    "x-api-key": "pub_3cb50d49e26ede1c2237630a0d1628c1c565e3bd444b60d1a91dee87d1061daf"
}

@pytest.mark.smoke
@pytest.mark.api
def test_login_valido():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    assert response.status_code == 200


@pytest.mark.regression
@pytest.mark.api
def test_login_sin_password():
    body = {
        "email": "eve.holt@reqres.in",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    body = response.json()
    assert response.status_code == 400
    assert body["error"] == "Missing password"


@pytest.mark.regression
@pytest.mark.api
def test_login_sin_email():
    body = {
        "password": "cityslicka",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    body = response.json()
    assert response.status_code == 400
    assert body["error"] == "Missing email or username"


@pytest.mark.regression
@pytest.mark.api
def test_create_user():
    body = {
        "name": "Jessica",
        "email": "jessica.puricelli78@gmail.com",
        "password": "12345*"
    }

    response = requests.post("https://reqres.in/api/users", headers=headers, json=body)
    data = response.json()

    check.equal(response.status_code, 201)
    check.is_true(body["email"].count("@") == 1)
    check.is_in("*", body["password"])
    check.equal(data["name"], body["name"])
    check.equal(data["email"], body["email"])
    check.less(response.elapsed.total_seconds(), 1)


@pytest.mark.regression
@pytest.mark.api
def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)
    assert response.status_code == 204


@pytest.mark.regression
@pytest.mark.api
def test_get_user():
    response = requests.get("https://reqres.in/api/users/2", headers=headers)

    assert response.status_code == 200
    #Validacion de tiempo de respuesta
    print(response.elapsed.total_seconds())
    assert response.elapsed.total_seconds() < 1, "El tiempo de ejecucion tardo mas de lo esperado"


@pytest.mark.regression
@pytest.mark.api
def test_crear_y_obtener_usuario():
    body = {
        "name": "Jessica",
        "job": "QA Automation Engineer"
    }

    post_response = requests.post("https://reqres.in/api/users", headers=headers, json=body)
    assert post_response.status_code == 201

    user_id = post_response.json()["id"]

    get_response = requests.get(f"https://reqres.in/api/users/{user_id}", headers=headers)
    assert get_response.status_code in [200, 404]
