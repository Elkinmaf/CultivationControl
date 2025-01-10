import math
import statistics
from typing import List, Union, Dict

# ========= MÓDULO DE OPERACIONES BÁSICAS =========
"""
Este módulo contiene las funciones para operaciones aritméticas básicas.
Cada función incluye validación de entrada y manejo de errores.
"""

def suma(a: float, b: float) -> float:
    """Realiza la suma de dos números y retorna el resultado"""
    return a + b

def resta(a: float, b: float) -> float:
    """Realiza la resta de dos números y retorna el resultado"""
    return a - b

def multiplicacion(a: float, b: float) -> float:
    """Realiza la multiplicación de dos números y retorna el resultado"""
    return a * b

def division(a: float, b: float) -> Union[float, str]:
    """
    Realiza la división entre dos números.
    Maneja el caso especial de división por cero.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No es posible dividir por cero"

# ========= MÓDULO DE OPERACIONES EXTENDIDAS =========
"""
Este módulo implementa operaciones matemáticas más avanzadas como
potencias, raíces, logaritmos y funciones especiales.
"""

def division_entera(a: float, b: float) -> Union[int, str]:
    """Calcula la división entera entre dos números"""
    try:
        return a // b
    except ZeroDivisionError:
        return "Error: No es posible dividir por cero"

def residuo(a: float, b: float) -> Union[float, str]:
    """Calcula el residuo de la división entre dos números"""
    try:
        return a % b
    except ZeroDivisionError:
        return "Error: No es posible dividir por cero"

def potencia(base: float, exponente: float) -> float:
    """Eleva un número a la potencia especificada"""
    return base ** exponente

def raiz_n(numero: float, n: int) -> Union[float, str]:
    """
    Calcula la raíz n-ésima de un número.
    Valida que no se intente calcular raíz par de número negativo.
    """
    if numero < 0 and n % 2 == 0:
        return "Error: No existe raíz par de un número negativo"
    return numero ** (1/n)

def logaritmo_base_10(numero: float) -> Union[float, str]:
    """Calcula el logaritmo en base 10 de un número"""
    try:
        return math.log10(numero)
    except ValueError:
        return "Error: No existe logaritmo de un número no positivo"

def factorial(n: int) -> Union[int, str]:
    """Calcula el factorial de un número entero no negativo"""
    if n < 0:
        return "Error: No existe factorial de número negativo"
    try:
        return math.factorial(n)
    except ValueError:
        return "Error: Número demasiado grande"

# ========= MÓDULO DE OPERACIONES TRIGONOMÉTRICAS =========
"""
Este módulo implementa funciones trigonométricas básicas.
Los ángulos deben proporcionarse en radianes.
"""

def seno(angulo: float) -> float:
    """Calcula el seno de un ángulo en radianes"""
    return math.sin(angulo)

def coseno(angulo: float) -> float:
    """Calcula el coseno de un ángulo en radianes"""
    return math.cos(angulo)

# ========= MÓDULO DE OPERACIONES ESTADÍSTICAS =========
"""
Este módulo maneja operaciones estadísticas básicas sobre
conjuntos de números.
"""

def calcular_estadisticas(numeros: List[float]) -> Dict[str, float]:
    """
    Calcula estadísticas básicas de un conjunto de números:
    media, mediana y moda
    """
    try:
        return {
            'media': statistics.mean(numeros),
            'mediana': statistics.median(numeros),
            'moda': statistics.mode(numeros)
        }
    except statistics.StatisticsError:
        return {
            'error': "No hay suficientes datos para calcular estadísticas"
        }

# ========= INTERFAZ DE USUARIO =========
"""
Este módulo maneja la interacción con el usuario a través de
menús y submenús para acceder a las diferentes operaciones.
"""

def mostrar_menu_principal() -> None:
    """Muestra el menú principal de la calculadora"""
    print("\n==== CALCULADORA CIENTÍFICA ====")
    print("1. Operaciones básicas")
    print("2. Operaciones extendidas")
    print("3. Operaciones trigonométricas")
    print("4. Operaciones estadísticas")
    print("5. Salir")

def main():
    """
    Función principal que controla el flujo del programa.
    Maneja la selección de operaciones y la entrada de datos.
    """
    while True:
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción: ")

        # Control de flujo principal para las diferentes operaciones
        if opcion == "1":
            print("\n-- Operaciones Básicas --")
            print("1. Suma\n2. Resta\n3. Multiplicación\n4. División")
            op = input("Seleccione operación: ")
            
            # Entrada de operandos
            try:
                a = float(input("Primer número: "))
                b = float(input("Segundo número: "))
                
                # Ejecución de la operación seleccionada
                if op == "1":
                    print(f"Resultado: {suma(a, b)}")
                elif op == "2":
                    print(f"Resultado: {resta(a, b)}")
                elif op == "3":
                    print(f"Resultado: {multiplicacion(a, b)}")
                elif op == "4":
                    print(f"Resultado: {division(a, b)}")
                else:
                    print("Operación no válida")
            except ValueError:
                print("Error: Entrada no válida")

        elif opcion == "2":
            # Submenu para operaciones extendidas
            print("\n-- Operaciones Extendidas --")
            print("1. División Entera\n2. Residuo\n3. Potencia\n4. Raíz\n5. Logaritmo\n6. Factorial")
            # ... implementación similar a las operaciones básicas

        elif opcion == "3":
            # Submenu para operaciones trigonométricas
            print("\n-- Operaciones Trigonométricas --")
            print("1. Seno\n2. Coseno")
            # ... implementación de operaciones trigonométricas

        elif opcion == "4":
            # Entrada de datos para estadísticas
            print("\n-- Operaciones Estadísticas --")
            numeros = []
            print("Ingrese números (escriba 'fin' para terminar):")
            
            while True:
                entrada = input()
                if entrada.lower() == 'fin':
                    break
                try:
                    numeros.append(float(entrada))
                except ValueError:
                    print("Entrada no válida, intente de nuevo")
            
            if numeros:
                resultados = calcular_estadisticas(numeros)
                for key, value in resultados.items():
                    print(f"{key}: {value}")
            else:
                print("No se ingresaron números")

        elif opcion == "5":
            print("¡Qué tenga un gran día!")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()