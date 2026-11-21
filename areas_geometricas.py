# areas_geometricas.py
# ----------------------------------------------------------
# Este módulo reúne las funciones para calcular áreas.
# Cada función recibe las medidas necesarias y devuelve
# el área calculada. No muestra mensajes por pantalla.
# ----------------------------------------------------------

import math  # Módulo estándar: permite utilizar math.pi.


def area_rectangulo(base, altura):
    """Devuelve el área de un rectángulo."""
    return base * altura


def area_cuadrado(lado):
    """Devuelve el área de un cuadrado."""
    return lado * lado


def area_circulo(radio):
    """Devuelve el área de un círculo."""
    return math.pi * radio**2


# En esta versión no se gestionan excepciones ni se validan
# valores negativos. Esa mejora se añadirá posteriormente.
