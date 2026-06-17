from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.filtro = (By.CLASS_NAME, "product_sort_container")
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
        self.contador_carrito = (By.CLASS_NAME, "shopping_cart_badge")
        self.link_carrito = (By.CLASS_NAME, "shopping_cart_link")
        self.nombres_productos = (By.CLASS_NAME, "inventory_item_name")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def obtener_titulo(self) -> str:
        return self.driver.title

    def obtener_productos(self) -> list:
        return self.driver.find_elements(*self.inventory_items)

    def menu_visible(self) -> bool:
        return self.driver.find_element(*self.menu_button).is_displayed()

    def filtro_visible(self) -> bool:
        return self.driver.find_element(*self.filtro).is_displayed()

    def obtener_opciones_filtro(self) -> list[str]:
        select = Select(self.driver.find_element(*self.filtro))
        return [option.text for option in select.options]

    def agregar_primer_producto_al_carrito(self):
        self.driver.find_elements(*self.add_to_cart_buttons)[0].click()

    def obtener_contador_carrito(self) -> str:
        return self.driver.find_element(*self.contador_carrito).text

    def obtener_nombre_primer_producto(self) -> str:
        return self.driver.find_elements(*self.nombres_productos)[0].text

    def ir_al_carrito(self):
        self.driver.find_element(*self.link_carrito).click()

    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logout_link))
        self.driver.find_element(*self.logout_link).click()

    def agregar_producto_por_nombre(self, nombre_producto: str):
        productos = self.driver.find_elements(*self.inventory_items)
        for producto in productos:
            nombre = producto.find_element(*self.nombres_productos).text
            if nombre == nombre_producto:
                producto.find_element(*self.add_to_cart_buttons).click()
                break
