# QA-TestSuite
"suite de pruebas de calidad" contiene todas mis pruebas.
    <ul>
        <!-- Directorio raíz -->
        <li class="root">project-root/
            <ul>
                <!-- Subdirectorios -->
                <li class="sublevel">tests/
                    <ul>
                        <li>__init__.py</li>
                        <li>test_login.py</li>
                        <li>test_signup.py</li>
                        <!-- Agrega más elementos según sea necesario -->
                    </ul>
                </li>
                <li class="sublevel">pages/
                    <ul>
                        <li>__init__.py</li>
                        <li>base_page.py</li>
                        <li>login_page.py</li>
                        <li>signup_page.py</li>
                        <!-- Agrega más elementos según sea necesario -->
                    </ul>
                </li>
                <li class="sublevel">locators/
                    <ul>
                        <li>__init__.py</li>
                        <li>login_page_locators.py</li>
                        <li>signup_page_locators.py</li>
                        <!-- Agrega más elementos según sea necesario -->
                    </ul>
                </li>
                <li class="sublevel">drivers/
                    <ul>
                        <li>chromedriver.exe (o el controlador de navegador que uses)</li>
                        <li>geckodriver.exe (si usas Firefox)</li>
                        <!-- Agrega más elementos según sea necesario -->
                    </ul>
                </li>
                <li class="sublevel">config/
                    <ul>
                        <li>__init__.py</li>
                        <li>config.py</li>
                        <li>constants.py</li>
                        <!-- Agrega más elementos según sea necesario -->
                    </ul>
                </li>
                <li class="sublevel">utils/
                    <ul>
                        <li>__init__.py</li>
                        <li>custom_exceptions.py</li>
                        <li>test_data.py</li>
                        <!-- Agrega más elementos según sea necesario -->
                    </ul>
                </li>
                <li class="sublevel">reports/
                    <ul>
                        <li>report_template.html</li>
                        <!-- Agrega más elementos según sea necesario -->
                    </ul>
                </li>
                <li class="sublevel">run_tests.py</li>
            </ul>
        </li>
    </ul>
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
