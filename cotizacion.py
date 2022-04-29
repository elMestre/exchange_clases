from datetime import datetime
from random import randint


class Cotizacion:

    def __init__(self, moneda_ref, moneda_cambio, tiempo_ref=60):
        # moneda_ref = 'EUR'
        self.moneda_ref = moneda_ref
        self.moneda_cambio = moneda_cambio
        self.tiempo_ref = tiempo_ref
        self.actualizar()

    def actualizar(self):
        self.valor = randint(0, 100)
        self.now = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        # self.valor = solicita_nuevo_precio_de(self.moneda_ref, self.moneda_cambio)

    def dame_texto(self):
        return self.moneda_ref + ' - ' + f"{self.valor}" + \
            self.moneda_cambio + ' a las ' + \
            self.now


        # return "Hora actual: {hora}".format(hora=current_time)
