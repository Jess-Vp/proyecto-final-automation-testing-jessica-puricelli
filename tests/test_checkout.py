from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage
from utils.logger import get_logger

logger = get_logger(__name__)


def test_checkout_flujo_completo(driver_logged):
    inventory_page = InventoryPage(driver_logged)
    cart_page = CartPage(driver_logged)
    checkout_page = CheckoutPage(driver_logged)

    inventory_page.agregar_primer_producto_al_carrito()
    inventory_page.ir_al_carrito()
    assert len(cart_page.obtener_productos_carrito()) == 1

    cart_page.ir_a_checkout()
    assert "checkout-step-one" in driver_logged.current_url

    checkout_page.ingresar_datos_personales("Jessica", "Puricelli", "1000")
    checkout_page.click_continue()
    assert "checkout-step-two" in driver_logged.current_url

    assert "Item total" in checkout_page.obtener_subtotal()
    assert "Total" in checkout_page.obtener_total()

    checkout_page.click_finish()
    assert "checkout-complete" in driver_logged.current_url
    assert "Thank you for your order" in checkout_page.obtener_mensaje_confirmacion()


def test_checkout_sin_datos_personales(driver_logged):
    inventory_page = InventoryPage(driver_logged)
    cart_page = CartPage(driver_logged)
    checkout_page = CheckoutPage(driver_logged)

    inventory_page.agregar_primer_producto_al_carrito()
    inventory_page.ir_al_carrito()
    cart_page.ir_a_checkout()
    checkout_page.click_continue()

    assert "First Name is required" in checkout_page.get_error_message()
