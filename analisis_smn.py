import sys

def leer_observaciones(ruta: str) -> dict:
    """Lee el archivo de observaciones del SMN y devuelve un diccionario
    {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento
    ya separado en dirección y velocidad."""

    with open('observaciones_smn.txt', 'r', encoding='latin-1') as texto:
    datos=texto.read()
    datos = datos.replace(' / \n ', '||').replace(' / \n', '').split('||') # lista con todos los datos
        
    listas = []
    data = {}
    for i in range(len(datos)-1):
        listas.append(datos[i].split(';')) # separa las ciudades con sus datos
    for lista in listas:
        data.update({lista[0]: lista[1:]}) # crea el diccionario 'ciudad': datos.


def separar_viento(campo_viento: str) -> tuple:
    """Convierte un campo de viento como 'Norte  3' en (direccion, velocidad).
    Contempla el caso 'Calma' (sin velocidad numérica)."""


def cantidad_ciudades(observaciones: dict) -> int:
    """Devuelve la cantidad total de ciudades leídas."""
    print(f'Cantidad de ciudades leídas: {len(data) + 1}')

def cantidad_ciudades_completas(observaciones: dict) -> int:
    """Devuelve la cantidad de ciudades sin ningún dato faltante."""


def top_n_ciudades(observaciones: dict, campo: str, n: int, descendente: bool = True) -> list:
    """Devuelve las n (por parámetro) ciudades ordenadas según 'campo', de mayor a menor
    (o al revés si descendente=False), en una lista. Reutilizable tanto para temperatura
    como para viento."""


def mostrar_resumen(observaciones: dict) -> None:
    """Imprime por pantalla el resumen con todas las características calculadas. Usar n=5"""
