from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from locators.buscador_empleo_locators import BuscadorEmpleoLocators

class BuscadorEmpleoPage:
    def __init__(self):
        self.driver = self._iniciar_driver()

    def _iniciar_driver(self):
        opciones = Options()
        opciones.page_load_strategy = 'normal'
        return webdriver.Chrome(options=opciones)

    def navegar_a_empleos_google(self):
        self.driver.get(BuscadorEmpleoLocators.URL)
        time.sleep(3)

    def buscar_empleos(self, palabra_clave):
        cuadro_busqueda = self.driver.find_element(By.XPATH, BuscadorEmpleoLocators.CUADRO_BUSQUEDA)
        cuadro_busqueda.send_keys(palabra_clave)
        time.sleep(3)

    def aplicar_filtros(self):
        boton_filtro = self.driver.find_element(By.XPATH, BuscadorEmpleoLocators.BOTON_FILTRO)
        boton_filtro.click()
        time.sleep(3)

        lista_trabajos = self.driver.find_element(By.XPATH, BuscadorEmpleoLocators.LISTA_TRABAJOS)
        lista_trabajos.click()
        time.sleep(3)

    def ordenar_por(self):
        boton_ordenar = self.driver.find_element(By.XPATH, BuscadorEmpleoLocators.BOTON_ORDENAR)
        boton_ordenar.click()
        time.sleep(3)

        boton_enviar = self.driver.find_element(By.XPATH, BuscadorEmpleoLocators.BOTON_ENVIAR)
        boton_enviar.click()
        time.sleep(3)

    def obtener_descripcion_trabajo(self):
        descripcion_trabajo = self.driver.find_element(By.XPATH, BuscadorEmpleoLocators.DESCRIPCION_TRABAJO)
        return descripcion_trabajo.text

    def cerrar_navegador(self):
        self.driver.quit()
