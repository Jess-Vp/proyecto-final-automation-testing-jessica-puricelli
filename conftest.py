import pytest
import os
from datetime import datetime
from selenium import webdriver
from page.login_page import LoginPage
from utils.data_reader import read_users_csv
from utils.logger import get_logger

logger = get_logger(__name__)


def pytest_configure(config):
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    logger.info("Carpetas de salida verificadas/creadas: reports/, screenshots/, logs/")


@pytest.fixture
def driver():
    logger.info("Iniciando WebDriver (Chrome - incógnito)")
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    yield driver
    logger.info("Cerrando WebDriver")
    driver.quit()


@pytest.fixture
def driver_logged(driver):
    login_page = LoginPage(driver)
    user = read_users_csv()[0]
    logger.info(f"Ejecutando login con usuario: {user['username']}")
    login_page.login(user["username"], user["password"])
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") or item.funcargs.get("driver_logged")
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name.replace(" ", "_")
            screenshot_name = f"screenshots/FAIL_{test_name}_{timestamp}.png"
            driver.save_screenshot(screenshot_name)
            logger.warning(f"Test fallido — Screenshot guardado: {screenshot_name}")
