from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from page.inventory_page import InventoryPage
from page.login_page import LoginPage

INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")


def test_inventory_title(driver_logged):
    inventory_page = InventoryPage(driver_logged)
    titulo = inventory_page.obtener_titulo()
    assert titulo == "Swag Labs", "El título de la página no es correcto."


def test_productos_visibles(driver_logged):
    inventory_page = InventoryPage(driver_logged)
    productos = inventory_page.obtener_productos()
    assert len(productos) > 0, "No se encontraron productos en el inventario."


def test_ui_elements(driver_logged):
    inventory_page = InventoryPage(driver_logged)
    assert inventory_page.menu_visible(), "El menú no está visible."
    assert inventory_page.filtro_visible(), "El filtro no está visible."


def test_first_product_details(driver_logged):
    inventory_page = InventoryPage(driver_logged)
    productos = driver_logged.find_elements(*inventory_page.inventory_items)
    first_name = productos[0].find_element(*inventory_page.nombres_productos).text
    first_price = productos[0].find_element(*INVENTORY_ITEM_PRICE).text
    assert first_name != "", "El primer producto no tiene nombre."
    assert first_price.startswith("$"), "El precio del primer producto no tiene formato correcto."


def test_opciones_filtro(driver_logged):
    inventory_page = InventoryPage(driver_logged)
    expected = ["Name (A to Z)", "Name (Z to A)", "Price (low to high)", "Price (high to low)"]
    assert inventory_page.obtener_opciones_filtro() == expected, "Las opciones del filtro no son correctas."
