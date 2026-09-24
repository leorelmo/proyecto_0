import sys

def leer_observaciones(ruta: str) -> dict:
    """Lee el archivo de observaciones del SMN y devuelve un diccionario
    {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento
    ya separado en dirección y velocidad."""

    observaciones = {}
    
    with open(ruta, 'r', encoding='latin-1') as texto:
        for linea in texto:
            linea = linea.strip()
            if not linea:
                continue

            datos = linea.split(';')
            if len(datos) != 10:
                continue

            ciudad = datos[0].strip()

            texto_st = datos[6].strip()
            if texto_st.lower() == 'no se calcula':
                sens_termica = None
            else:
                sens_termica = float(texto_st)

            direccion, velocidad = separar_viento(datos[8])

            txt_presion = datos[9].strip(' /')

            observaciones[ciudad] = {
                'fecha': datos[1].strip(),
                'hora': datos[2].strip(),
                'condicion': datos[3].strip(),
                'visibilidad': datos[4].strip(),
                'temperatura': float(datos[5].strip()),
                'sens_termica': sens_termica,
                'humedad': float(datos[7].strip()),
                'dir_viento': direccion,
                'vel_viento': velocidad,
                'presion': float(txt_presion),
            }
    return observaciones
   

def separar_viento(campo_viento: str) -> tuple:
    """Convierte un campo de viento como 'Norte  3' en (direccion, velocidad).
    Contempla el caso 'Calma' (sin velocidad numérica)."""
    campo_viento = campo_viento.strip()
    if campo_viento.lower() == 'calma':
        return ('Calma', 0)
    partes = campo_viento.rsplit(None, 1)
    direccion = partes[0]
    velocidad = int(partes[1])
    return (direccion, velocidad)


def cantidad_ciudades(observaciones: dict) -> int:
    """Devuelve la cantidad total de ciudades leídas."""
    return len(observaciones)

def cantidad_ciudades_completas(observaciones: dict) -> int:
    """Devuelve la cantidad de ciudades sin ningún dato faltante."""
    ciud_comp = 0
    for datos_ciudad in observaciones.values():
        if None not in datos_ciudad.values():
            ciud_comp += 1
    return ciud_comp

def top_n_ciudades(observaciones: dict, campo: str, n: int, descendente: bool = True) -> list:
    """Devuelve las n (por parámetro) ciudades ordenadas según 'campo', de mayor a menor
    (o al revés si descendente=False), en una lista. Reutilizable tanto para temperatura
    como para viento."""
    vale = []
    for ciudad, datos in observaciones.items():
        valor = datos.get(campo)
        if valor is not None and isinstance(valor, (int, float)):
            vale.append(ciudad)
    def valor(ciudad):
        return observaciones[ciudad][campo]
    ciud_ord = sorted(vale, key=valor, reverse=descendente)
    return ciud_ord[:n]


def mostrar_resumen(observaciones: dict) -> None:
    """Imprime por pantalla el resumen con todas las características calculadas. Usar n=5"""
    print('RESUMEN METEOROLÓGICO\n')
    print(f'Total de ciudades procesadas: {cantidad_ciudades(observaciones)}')
    print(f'Ciudades con datos completos: {cantidad_ciudades_completas(observaciones)}')
    
    print('\nTOP 5 CIUDADES MÁS CÁLIDAS')
    for ciudad in top_n_ciudades(observaciones, 'temperatura', 5, descendente=True):
        temp = observaciones[ciudad]['temperatura']
        print(f'- {ciudad}: {temp}°C')
    
    print('\nTOP 5 CIUDADES MÁS FRÍAS')
    for ciudad in top_n_ciudades(observaciones, 'temperatura', 5, descendente=False):
        temp = observaciones[ciudad]['temperatura']
        print(f'- {ciudad}: {temp}°C')
    
    print('\nTOP 5 CIUDADES CON MÁS VIENTO')
    for ciudad in top_n_ciudades(observaciones, 'vel_viento', 5, descendente=True):
        vel = observaciones[ciudad]['vel_viento']
        print(f'- {ciudad}: {vel} km/h')
    
    print('\nTOP 5 CIUDADES CON MENOS VIENTO')
    for ciudad in top_n_ciudades(observaciones, 'vel_viento', 5, descendente=False):
        vel = observaciones[ciudad]['vel_viento']
        print(f'- {ciudad}: {vel} km/h')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Error: Falta ingresar la ruta del archivo de observaciones.')
        print('Uso correcto: python analisis_smn.py <ruta_al_archivo>')
        sys.exit(1)
    ruta_archivo = sys.argv[1]
    try:
        observaciones = leer_observaciones(ruta_archivo)
        mostrar_resumen(observaciones)
    except FileNotFoundError:
        print(f'Error: No se encontró el archivo en la ruta '{ruta_archivo}'.')
    except Exception as e:
        print(f'Ocurrió un error inesperado al procesar el archivo: {e}')