import unittest
from pages.buscador_empleo_page import BuscadorEmpleoPage

class TestBuscadorEmpleo(unittest.TestCase):
    def setUp(self):
        self.buscador = BuscadorEmpleoPage()

    def test_buscador_empleo(self):
        try:
            self.buscador.navegar_a_empleos_google()
            self.buscador.buscar_empleos("python")
            self.buscador.aplicar_filtros()
            self.buscador.ordenar_por()
            texto_trabajo = self.buscador.obtener_descripcion_trabajo()
            self.assertTrue("Python" in texto_trabajo)  # Verifica que la descripción contiene la palabra 'Python'.
        except Exception as e:
            self.fail(f"Error: {str(e)}")
        finally:
            self.buscador.cerrar_navegador()

if __name__ == "__main__":
    unittest.main()
