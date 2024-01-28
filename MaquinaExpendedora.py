class MaquinaExpendedora:
    def __init__(self):
        self.estados = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']
        self.alfabeto = ['5', '10', '25', '50', '.']
        self.matriz_transiciones = [
            ['q1',  'q2',  'q5',  'q10', '-'],
            ['q2',  'q3',  'q6',  'e',   '-'],
            ['q3',  'q4',  'q7',  'e',   'chicle'],
            ['q4',  'q5',  'q8',  'e',   '-'],
            ['q5',  'q6',  'q9',  'e',   '-'],
            ['q6',  'q7',  'q10', 'e',   'papas rufles'],
            ['q7',  'q8',  'e',   'e',   '-'],
            ['q8',  'q9',  'e',   'e',   '-'],
            ['q9',  'q10', 'e',   'e',   '-'],
            ['q10', 'e',   'e',   'e',   '-'],
            ['e',   'e',   'e',   'e',   'tango']
        ]
        self.estado_inicial = 'q0'
        self.estados_aceptacion = ['q2', 'q5', 'q10']
        self.ganancia_total = 0.0
        self.ganancia_i = 0.0

    def transicion(self, estado_actual, simbolo):
        columna = self.alfabeto.index(simbolo)
        return self.matriz_transiciones[self.estados.index(estado_actual)][columna]
    
    def procesar_monedas(self, monedas):
        if "." not in monedas:
                return "Ingrese un \".\" al final"
        
        estado_actual = self.estado_inicial
        self.ganancia_i = 0.0

        for moneda in monedas:
            if moneda not in self.alfabeto:
                return "Ingresó una moneda no valida"
            if "." in moneda and self.es_aceptacion(estado_actual):
                return " - Producto: " + self.matriz_transiciones[self.estados.index(estado_actual)][4]
            
            if "." in moneda and not self.es_aceptacion(estado_actual):
                return self.quedarse_con_cambio(estado_actual)
            
            self.ganancia_i += float(moneda)
            estado_actual = self.transicion(estado_actual, moneda)

    def es_aceptacion(self, estado_actual):
        return estado_actual in self.estados_aceptacion
    
    def quedarse_con_cambio(self, estado_actual):
        return " - Producto: " + self.encontrar_producto_adquirible(estado_actual) + "\n - Ganancia de la maquina en esta compra: " + str(self.ganancia_i) + "\n - Ganacia total de la maquina: " + str(self.ganancia_total)
    
    def encontrar_producto_adquirible(self, estado_actual):
        estados_aceptacion_reversa = self.estados_aceptacion[::-1]
        
        for estado_acept_i in estados_aceptacion_reversa:
            if int(self.estados.index(estado_actual)) > int(self.estados.index(estado_acept_i)):
                self.calcular_ganancia(estado_acept_i)
                return self.matriz_transiciones[self.estados.index(estado_acept_i)][4]
        return "No se puede adquirir ningun producto"

    def calcular_ganancia(self, estado_acept_i):
        self.ganancia_i = self.ganancia_i - (float(self.estados.index(estado_acept_i))*5)
        self.ganancia_total += self.ganancia_i