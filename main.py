import time
from cotizacion import Cotizacion
from pantalla import Pantalla

if __name__ == "__main__":
    cotizaciones = [
            Cotizacion('USD', 'EUR'),
            Cotizacion('USD', 'JPY'),
            Cotizacion('USD', 'RUB'),
        ]
    pantalla = Pantalla()

    while True:
        pantalla.buffer = []
        for cotizacion in cotizaciones:
            pantalla.buffer.append(cotizacion.dame_texto())
        pantalla.dibujar()

        time.sleep(1)
