
# Bibliotecas necesarias para cálculos estadísticos
from statistics import mean, mode, median, stdev
from datetime import datetime
# Para validar correo electrónico
import re

# Diccionario global para almacenar los estudiantes, identificación única por estudiante

estudiantes = {}

# Validación correo Regex
def validar_correo(correo):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, correo) is not None

# Función para validar que la nota esté entre 0 y 5
def validar_nota(nota):
    try:
        nota = float(nota)
        return 0 <= nota <= 5
    except ValueError:
        return False

#Función para agregar un nuevo estudiante
def agregar_estudiante():
    try:
        id = input("Identificación: ")
        if id in estudiantes:
            print("Error! Estudiante ya existe")
            return
    
        nombre = input("Nombre: ")

        #Validamos el correo
        while True:
            correo = input("Correo: ")
            if validar_correo(correo):
                break
            print("Correo inválido. Intente nuevamente")
        
        telefono = input("Teléfono: ")

        #Validamos fecha de nacimiento
        while True:
            try:
                fecha_nac = input("Fecha de nacimiento (DD/MM/YYYY): ")
                fecha_nac = datetime.strptime(fecha_nac, "%d/%m/%Y")
                break
            except ValueError:
                print("Por favor, valide la fecha de nacimiento")

        notas = []
        for i in range(4):
            while True:
                nota = input(f"Nota {i+1} (0-5): ")
                if validar_nota(nota):
                    notas.append(float(nota))
                    break
                print("Nota inválida. Debe estar entre 0 y 5")

        # Guardamos los estudiantes en el diccionario

        estudiantes[id] = {
            'nombre': nombre,
            'correo': correo,
            'telefono': telefono,
            'fecha_nacimiento': fecha_nac,
            'notas': notas
        }

        print("Estudiante agregado exitosamente")


    except Exception as e:
        print(f"Error al agregar estudiante: {e}")

# Función para buscar un estudiante por ID
def buscar_estudiante():
    id = input("Ingrese la identificación del estudiante: ")
    if id in estudiantes:
        est = estudiantes[id]
        print("\nInformación del estudiante: ")
        print(f"Nombre: {est['nombre']}")
        print(f"Correo: {est['correo']}")
        print(f"Teléfono: {est['telefono']}")
        print(f"Fecha de nacimiento: {est['fecha_nacimiento'].strftime('%d/%m/%Y')}")
        print(f"Notas: {est['notas']}")
        return id
    else:
        print("Estudiante no encontrado")
        return None

# Función para modificar las notas de un estudiante
def modificar_notas():
    id = buscar_estudiante()
    if id:
        nuevas_notas = []
        for i in range(4):
            while True:
                nota = input(f"Nueva nota {i+1} (0-5): ")
                if validar_nota(nota):
                    nuevas_notas.append(float(nota))
                    break
                print("Nota inválida. Debe estar entre 0 y 5")

        estudiantes[id]['notas'] = nuevas_notas
        print("Notas modificadas exitosamente")

# Función para eliminar un estudiante
def cancelar_materia():
    id = buscar_estudiante()
    if id:
        confirmacion = input("¿Está seguro de eliminar este estudiante? (s/n): ")
        if confirmacion.lower() == 's':
            del estudiantes[id]
            print("Estudiante eliminado exitosamente")

# Función para calcular estadísticas del grupo
def calcular_estadisticas_grupo():
    if not estudiantes:
        return None

    notas_finales = [sum(est['notas'])/4 for est in estudiantes.values()]
    return {
        'promedio': mean(notas_finales),
        'mediana': median(notas_finales),
        'moda': mode(notas_finales),
        'desv_std': stdev(notas_finales) if len(notas_finales) > 1 else 0,
        'notas_finales': notas_finales
    }

# Función para calcular el percentil de una nota
def calcular_percentil(nota, notas_grupo):
    return sum(1 for x in notas_grupo if x < nota) / len(notas_grupo) *100

# Función para mostrar resultados de un estudiante
def resultados_estudiante():
    id = buscar_estudiante()
    if id and estudiantes:
        est = estudiantes[id]
        nota_final = sum(est['notas'])/4
        stats = calcular_estadisticas_grupo()

        print(f"\nNota_final: {nota_final:.2f}")
        print(f"Promedio del grupo: {stats['promedio']:.2f}")
        print(f"Estado: {'Por encima' if nota_final > stats['promedio'] else 'Por debajo'} del promedio")
        print(f"Resultado: {'Ganó' if nota_final >= 3.0 else 'Perdió'} el curso")
        print(f"Percentil: {calcular_percentil(nota_final, stats['notas_finales']):.2f}")

# Función para mostrar el informe general del grupo
def informe_grupo():
    if not estudiantes:
        print("No hay estudiantes registrados")
        return

    stats = calcular_estadisticas_grupo()
    notas_finales = stats['notas_finales']

# Resultados individuales
    print("\nNotas finales por estudiante:")
    for id, est in estudiantes.items():
        nota_final = sum(est['notas'])/4
        print(f"{est['nombre']}: {nota_final:.2f}")

    n_ganadores = sum(1 for n in notas_finales if n >= 3.0)
    n_perdedores = len(notas_finales) - n_ganadores

# Mostrar estadísticas generales

    print(f"\nPromedio del grupo: {stats['promedio']:.2f}")
    print(f"Estudiantes por encima del promedio: {sum(1 for n in notas_finales if n > stats['promedio'])}")
    print(f"Estudiantes por debajo del promedio: {sum(1 for n in notas_finales  if n < stats['promedio'])}")
    print(f"Estudiantes en el promedio: {sum(1 for n in notas_finales if n == stats['promedio'])}")
    print(f"Ganadores: {n_ganadores} ({n_ganadores/len(notas_finales)*100:.2f}%)")
    print(f"Perdedores: {n_perdedores} ({n_perdedores/len(notas_finales)*100:.2f}%)")
    print(f"Moda: {stats['moda']:.2f}")
    print(f"Mediana: {stats['mediana']:.2f}")
    print(f"Desviación estándar: {stats['desv_std']:.2f}")

    print("\nDistribución por percentiles:")
    percentiles = [25, 50, 75, 100]
    for p in percentiles:
        count = sum(1 for n in notas_finales if calcular_percentil(n, notas_finales) <= p)
        print(f"0-{p}%: {count} estudiantes")

# Función para mostrar y manejar el menú principal
def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar estudiante")
        print("2. Buscar estudiante")
        print("3. Modificar notas")
        print("4. Cancelar materia")
        print("5. Resultados por estudiante")
        print("6. Informe de grupo")
        print("7. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            buscar_estudiante()
        elif opcion == "3":
            modificar_notas()
        elif opcion == "4":
            cancelar_materia()
        elif opcion == "5":
            resultados_estudiante()
        elif opcion == "6":
            informe_grupo()
        elif opcion == "7":
            print("Cerrando el programa\n¡Qué tenga un gran día!")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu_principal()