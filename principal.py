# principal.py
# ----------------------------------------------------------
# Programa principal de calculadoraGeometrica.
# Presenta un menú, solicita las medidas y muestra el área.
# Los cálculos se realizan en el módulo areas_geometricas.
# ----------------------------------------------------------

import areas_geometricas  # Importamos nuestro módulo propio.


def mostrar_menu():
    """Muestra por pantalla las opciones disponibles."""
    print("\n===== CALCULADORA GEOMÉTRICA =====")
    print("1. Calcular área de un rectángulo")
    print("2. Calcular área de un cuadrado")
    print("3. Calcular área de un círculo")
    print("0. Salir")


def main():
    """Controla el flujo principal de la aplicación."""

    # El menú se repite mientras no se elija la opción 0.
    while True:
        mostrar_menu()

        # input() obtiene texto; int() lo convierte a entero.
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            # Solicitamos las dos dimensiones del rectángulo.
            base = float(input("Introduce la base: "))
            altura = float(input("Introduce la altura: "))

            resultado = areas_geometricas.area_rectangulo(base, altura)
            print(f"El área del rectángulo es: {resultado:.2f}")

        elif opcion == 2:
            # Para el cuadrado solo necesitamos conocer el lado.
            lado = float(input("Introduce el lado: "))

            resultado = areas_geometricas.area_cuadrado(lado)
            print(f"El área del cuadrado es: {resultado:.2f}")

        elif opcion == 3:
            # Para el círculo solicitamos el radio.
            radio = float(input("Introduce el radio: "))

            resultado = areas_geometricas.area_circulo(radio)
            print(f"El área del círculo es: {resultado:.2f}")

        elif opcion == 0:
            print("Gracias por utilizar la calculadora. ¡Hasta pronto!")
            break  # Finaliza el bucle while.

        else:
            print("Opción no reconocida. Selecciona 0, 1, 2 o 3.")


# Este condicional comprueba cómo se está ejecutando el archivo.
# Si se ejecuta directamente, se llama a main().
# Si se importa desde otro archivo, main() no se ejecuta solo.
if __name__ == "__main__":
    main()


# IMPORTANTE: esta versión todavía no utiliza try/except.
# Una entrada no numérica provocará un error de conversión.
# La validación de entradas y las excepciones se añadirán
# en una versión posterior del proyecto.
