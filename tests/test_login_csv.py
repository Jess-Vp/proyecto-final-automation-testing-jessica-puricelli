from page.login_page import LoginPage
from utils.data_reader import read_users_csv

import pytest

@pytest.mark.parametrize("user", read_users_csv())
def test_login_csv(driver, user):
    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])
    if user["valid"] == "true":
        assert "/inventory.html" in driver.current_url, f"No se redirigío al inventario para el usuario {user['username']}."
    else:
        error_message = login_page.get_error_message()
        assert "Epic sadface" in error_message, f"No se mostró el mensaje de error para el usuario {user['username']}."