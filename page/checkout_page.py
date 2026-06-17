from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        # Step One
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")
        # Step Two
        self.finish_button = (By.ID, "finish")
        self.summary_subtotal = (By.CLASS_NAME, "summary_subtotal_label")
        self.summary_total = (By.CLASS_NAME, "summary_total_label")
        # Complete
        self.complete_header = (By.CLASS_NAME, "complete-header")
        self.back_home_button = (By.ID, "back-to-products")

    def ingresar_datos_personales(self, first_name: str, last_name: str, postal_code: str):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.first_name_input))
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def get_error_message(self) -> str:
        return self.driver.find_element(*self.error_message).text

    def obtener_subtotal(self) -> str:
        return self.driver.find_element(*self.summary_subtotal).text

    def obtener_total(self) -> str:
        return self.driver.find_element(*self.summary_total).text

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()

    def obtener_mensaje_confirmacion(self) -> str:
        return self.driver.find_element(*self.complete_header).text

    def volver_al_inicio(self):
        self.driver.find_element(*self.back_home_button).click()
