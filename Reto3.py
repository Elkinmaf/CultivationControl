# Definición de la clase Cultivo para manejar la información de cada cultivo
class Cultivo:
    def __init__(self, nombre, mantenimiento, regado, abono, etapas):
        self.nombre = nombre
        self.mantenimiento = mantenimiento
        self.regado = regado
        self.abono = abono
        self.etapas = etapas

# Clase para manejar la información contable
class InformacionContable:
    def __init__(self):
        self.gastos_por_mes = []  # Lista para los 5 meses
        self.costos_por_mes = []  # Lista para los 5 meses
        self.valor_arroba = 0
        self.kilos_recolectados = 0

    def ingresar_datos_mensuales(self):
        for mes in range(5):
            print(f"\n=== Mes {mes + 1} ===")
            # Opción para cancelar
            print("Para cancelar y volver al menú principal, escriba 'cancelar'")
            
            # Gastos (Costos Variables)
            # gastos = {
            #     'medicamentos': float(input("Ingrese gastos en medicamentos: ")),
            #     'imprevistos': float(input("Ingrese gastos en imprevistos: "))
            # }

            medicamentos = input("Ingrese gastos en medicamentos: ")
            if medicamentos.lower() == 'cancelar':
                return False
            
            imprevistos = input("Ingrese gastos en imprevistos: ")
            if imprevistos.lower() == 'cancelar':
                return False

            try:
                gastos = {
                    'medicamentos': float(medicamentos),
                    'imprevistos': float(imprevistos)
                }

            except ValueError:
                print("Valor no válido")
                return False


            self.gastos_por_mes.append(gastos)
            
            # Costos (Costos Fijos)
            costos = {
                'mano_obra': float(input("Ingrese costo de mano de obra: ")),
                'abono': float(input("Ingrese costo de abono: ")),
                'agua': float(input("Ingrese costo de agua: ")),
                'mantenimiento': float(input("Ingrese costo de mantenimiento: "))
            }
            self.costos_por_mes.append(costos)

    def ingresar_produccion(self):
        self.valor_arroba = float(input("\nIngrese valor de la arroba (12.5 kilos) de arroz: "))
        self.kilos_recolectados = float(input("Ingrese cantidad de kilos recolectados: "))

    def calcular_resultados(self):
        # a. Costos totales por mes
        costos_totales_mes = []
        for mes in range(5):
            total = sum(self.costos_por_mes[mes].values())
            costos_totales_mes.append(total)
            print(f"Mes {mes + 1} - Costos totales: ${total:,.2f}")

        # b. Costos totales de mano de obra
        total_mano_obra = sum(mes['mano_obra'] for mes in self.costos_por_mes)
        print(f"\nTotal mano de obra: ${total_mano_obra:,.2f}")

        # c. Meses sin gastos
        meses_sin_gastos = [mes + 1 for mes in range(5) 
                           if sum(self.gastos_por_mes[mes].values()) == 0]
        print(f"Meses sin gastos: {meses_sin_gastos if meses_sin_gastos else 'Ninguno'}")

        # d. Meses con gastos menores a 100,000
        meses_gastos_bajos = [mes + 1 for mes in range(5) 
                             if sum(self.gastos_por_mes[mes].values()) < 100000]
        print(f"Meses con gastos < $100,000: {meses_gastos_bajos if meses_gastos_bajos else 'Ninguno'}")

        # e. Meses donde costo > gasto
        meses_costo_mayor = [mes + 1 for mes in range(5) 
                            if sum(self.costos_por_mes[mes].values()) > sum(self.gastos_por_mes[mes].values())]
        print(f"Meses donde costo > gasto: {meses_costo_mayor}")

        # f. Promedio de costos fijos y variables
        promedio_costos = sum(sum(mes.values()) for mes in self.costos_por_mes) / 5
        promedio_gastos = sum(sum(mes.values()) for mes in self.gastos_por_mes) / 5
        print(f"Promedio costos fijos: ${promedio_costos:,.2f}")
        print(f"Promedio costos variables: ${promedio_gastos:,.2f}")

        # g. Cálculo de ganancia
        ingresos = (self.kilos_recolectados / 12.5) * self.valor_arroba
        total_costos = sum(sum(mes.values()) for mes in self.costos_por_mes)
        total_gastos = sum(sum(mes.values()) for mes in self.gastos_por_mes)
        ganancia = ingresos - total_costos - total_gastos
        print(f"\n¿Hubo ganancia?: {'Sí' if ganancia > 0 else 'No'}")
        if ganancia > 0:
            print(f"Ganancia: ${ganancia:,.2f}")

        # h. Ganancia con incremento del 37% en precio
        valor_arroba_incrementado = self.valor_arroba * 1.37
        ingresos_incrementados = (self.kilos_recolectados / 12.5) * valor_arroba_incrementado
        ganancia_incrementada = ingresos_incrementados - total_costos - total_gastos
        print(f"\nGanancia con incremento del 37%: ${ganancia_incrementada:,.2f}")

        # i. Ganancia con reducción de costos y producción
        costos_gastos_reducidos = (total_costos + total_gastos) * 0.95
        kilos_reducidos = self.kilos_recolectados * 0.37
        ingresos_reducidos = (kilos_reducidos / 12.5) * self.valor_arroba
        ganancia_reducida = ingresos_reducidos - costos_gastos_reducidos
        print(f"Ganancia con reducción: ${ganancia_reducida:,.2f}")


# Lista para almacenar los cultivos
cultivos = [
    Cultivo(
        "Arroz",
        "Lunes, Jueves 4:00 pm",
        "Martes, Viernes 3:00 pm",
        "Miércoles 2:00 pm",
        {
            "Etapa 1 - Fase Vegetativa": "5 a 30 días",
            "Etapa 2 - Fase Reproductiva": "31 a 60 días",
            "Etapa 3 - Fase Maduración": "61 a 90 días"
        }
    ),
]

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL - Huerta Escolar===")
    print("1. Horario de Gestión de Cultivo")
    print("2. Etapas del Cultivo")
    print("3. Información Contable")
    print("4. Agregar Cultivo")
    print("5. Salir")

# Función para agregar nuevos cultivos
def agregar_cultivo():
    nombre = input("Nombre del cultivo: ")
    mantenimiento = input("Días y horarios de mantenimiento: ")
    regado = input("Días y horario de regado: ")
    abono = input("Días y horario de abono: ")

    etapas = {}
    num_etapas = int(input("Número de etapas: "))
    for i in range(num_etapas):
        nombre_etapa = input(f"Nombre de etapa {i+1}: ")
        duracion = input(f"Duración de etapa {i+1}: ")
        etapas[nombre_etapa] = duracion

    nuevo_cultivo = Cultivo(nombre, mantenimiento, regado, abono, etapas)
    cultivos.append(nuevo_cultivo)
    print("Cultivo agregato exitosamente!")

# Función para mostrar los cultivos disponibles
def mostrar_cultivos():
    print("\nCultivos disponibles:")
    for i, cultivo in enumerate(cultivos, 1):
        print(f"{i}. {cultivo.nombre}")

# Función para mostrar horarios de gestión
def mostrar_horarios(cultivo):
    print(f"\nHorarios de gestión para {cultivo.nombre}:")
    print(f"Mantenimiento: {cultivo.mantenimiento}")
    print(f"Regado: {cultivo.regado}")
    print(f"Abono: {cultivo.abono}")

# Función para mostrar etapas
def mostrar_etapas(cultivo):
    print(f"\nEtapas de {cultivo.nombre}:")
    for etapa, duracion in cultivo.etapas.items():
        print(f"{etapa}: {duracion}")

def main():
    info_contable = InformacionContable()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            mostrar_cultivos()
            try:
                seleccion = int(input("Seleccione un cultivo: ")) - 1
                if 0 <= seleccion < len(cultivos):
                    mostrar_horarios(cultivos[seleccion])
                else:
                    print("Cultivo no válido")
            except ValueError:
                print("Entrada no válida")
                
        elif opcion == "2":
            mostrar_cultivos()
            try:
                seleccion = int(input("Seleccione un cultivo: ")) - 1
                if 0 <= seleccion < len(cultivos):
                    mostrar_etapas(cultivos[seleccion])
                else:
                    print("Cultivo no válido")
            except ValueError:
                print("Entrada no válida")
                
        elif opcion == "3":
            #Información Contable

            print("\n=== INFORMACIÓN CONTABLE ===")
            #Opción cancelar:
            if info_contable.ingresar_datos_mensuales() == False:
                continue
            info_contable.ingresar_produccion()
            info_contable.calcular_resultados()

        elif opcion == "4":
            agregar_cultivo()
            
        elif opcion == "5":
            print("¡Qué tenga un feliz resto de día!")
            break
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()

