from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from utils.data_reader import read_products_json
from utils.logger import get_logger

logger = get_logger(__name__)


def test_agregar_producto_al_carrito(driver_logged):
    inventory_page = InventoryPage(driver_logged)
    inventory_page.agregar_primer_producto_al_carrito()
    assert inventory_page.obtener_contador_carrito() == "1"


def test_producto_en_carrito_coincide(driver_logged):
    inventory_page = InventoryPage(driver_logged)
    inventory_page.agregar_primer_producto_al_carrito()
    nombre_inventario = inventory_page.obtener_nombre_primer_producto()
    inventory_page.ir_al_carrito()
    cart_page = CartPage(driver_logged)
    productos = cart_page.obtener_productos_carrito()
    assert len(productos) == 1
    assert productos[0]["nombre"] == nombre_inventario


def test_carrito_con_datos_json(driver_logged):
    productos_json = read_products_json()
    inventory_page = InventoryPage(driver_logged)
    cart_page = CartPage(driver_logged)
    for producto in productos_json:
        inventory_page.agregar_producto_por_nombre(producto["nombre"])
    inventory_page.ir_al_carrito()
    productos_carrito = cart_page.obtener_productos_carrito()
    for p in productos_json:
        assert any(pc["nombre"] == p["nombre"] and pc["precio"] == p["precio"] for pc in productos_carrito)
