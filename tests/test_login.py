import pytest
from page.login_page import LoginPage
from utils.data_reader import read_users_csv
from utils.logger import get_logger

logger = get_logger(__name__)


def test_login_exitoso(driver):
    logger.info("TC-01: Login exitoso")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "/inventory.html" in driver.current_url


def test_login_password_invalido(driver):
    logger.info("TC-02: Login con password inválido")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "password_incorrecto")
    assert "Epic sadface" in login_page.get_error_message()


def test_login_usuario_invalido(driver):
    logger.info("TC-03: Login con usuario inválido")
    login_page = LoginPage(driver)
    login_page.login("usuario_que_no_existe", "secret_sauce")
    assert "Epic sadface" in login_page.get_error_message()


@pytest.mark.parametrize("user", read_users_csv())
def test_login_parametrizado(driver, user):
    logger.info(f"TC-04: Login parametrizado — usuario={user['username']}")
    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])
    if user["valid"] == "true":
        assert "/inventory.html" in driver.current_url
    else:
        assert "Epic sadface" in login_page.get_error_message()
