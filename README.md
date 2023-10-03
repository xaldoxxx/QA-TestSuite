# QA-TestSuite
"suite de pruebas de calidad" contiene todas mis pruebas.



      project-root/
          ├── tests/
          │   ├── __init__.py
          │   ├── test_login.py
          │   ├── test_signup.py
          │   └── ... (otros casos de prueba)
          ├── pages/
          │   ├── __init__.py
          │   ├── base_page.py
          │   ├── login_page.py
          │   ├── signup_page.py
          │   └── ... (otras páginas)
          ├── locators/
          │   ├── __init__.py
          │   ├── login_page_locators.py
          │   ├── signup_page_locators.py
          │   └── ... (otros localizadores)
          ├── drivers/
          │   ├── chromedriver.exe (o el controlador de navegador que uses)
          │   ├── geckodriver.exe (si usas Firefox)
          │   └── ...
          ├── config/
          │   ├── __init__.py
          │   ├── config.py
          │   └── constants.py
          ├── utils/
          │   ├── __init__.py
          │   ├── custom_exceptions.py
          │   ├── test_data.py
          │   └── ...
          ├── reports/
          │   ├── report_template.html
          │   └── ...
          └── run_tests.py



Descripción de los directorios y archivos:

tests/: Este directorio contiene los casos de prueba escritos utilizando el marco unittest. Cada archivo debe comenzar con "test_" y debe importar las páginas y utilidades necesarias.

pages/: Aquí se definen las clases que representan las páginas de la aplicación web bajo prueba. Cada página debe tener sus métodos para interactuar con los elementos de la página y realizar acciones.

locators/: Este directorio contiene los módulos que definen los localizadores (selectores) de los elementos en las páginas web. Puedes agruparlos por página o funcionalidad.

drivers/: Aquí debes colocar los controladores de los navegadores que vas a utilizar (por ejemplo, chromedriver o geckodriver para Firefox). Asegúrate de que los controladores sean compatibles con la versión del navegador que estás probando.

config/: Contiene módulos relacionados con la configuración del proyecto. Puedes tener un archivo config.py para configurar rutas y otros valores de configuración, y constants.py para definir constantes útiles.

utils/: En este directorio, puedes poner utilidades y funciones reutilizables, como manejo de excepciones personalizadas, carga de datos de prueba, etc.

reports/: Donde se almacenan los informes de pruebas generados por el marco de pruebas, si es necesario.

run_tests.py: Este archivo se utiliza para ejecutar todos los casos de prueba. Puedes personalizarlo para configurar la ejecución de pruebas, informes, etc.

report_template.html: Un archivo de plantilla para informes de pruebas personalizados, si lo necesitas.
