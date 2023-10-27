class BuscadorEmpleoLocators:
    URL = "https://www.google.com/about/careers/applications/jobs/results"
    CUADRO_BUSQUEDA = "/html[1]/body[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]/input[1]"
    BOTON_FILTRO = "//button[@aria-label='Locations filter options']//i[@aria-hidden='true']"
    LISTA_TRABAJOS = "/html[1]/body[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/label[1]"
    BOTON_ORDENAR = "(//i[@class='google-material-icons VfPpkd-kBDsod'][normalize-space()='expand_more'])[6]"
    BOTON_ENVIAR = '/html[1]/body[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[7]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]'
    DESCRIPCION_TRABAJO = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div[2]/main'
