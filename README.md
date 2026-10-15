La idea de este proyecto es obtener una serie de datos a partir de las observaciones actuales del Servicio Meteorológico Nacional. El objetivo es crear una herramienta de líneas de comandos que interprete las observaciones y guarde los datos en un diccionario indexado por ciudad (o estación), y calcule características y estadísticas generales sobre esos datos (estaciones leídas, datos faltantes, columnas ausentes, temperaturas y vientos extremos, rankings de ciudades).



Las observaciones del SMN se obtienen de su página web (https://www.smn.gob.ar/descarga-de-datos), en la página debes aceptar los TyC para poder acceder a los datos y se descarga el 'Estado del Tiempo Presente' en el apartado de 'Descarga de datos actuales: [fecha]'. Esto te da un .zip que al descomprimirlo se obtiene el archivo .txt con los datos meteorológicos del día.



Para ejecutar la herramienta desde la terminal, se debe invocar el script pasando la ruta del archivo '.txt' de observaciones como argumento:

python analisis_smn.py observaciones_smn.txt



Al ejecutar el programa, se obtiene un reporte consolidado en la consola:

RESUMEN METEOROLÓGICO

Total de ciudades procesadas: 121
Ciudades con datos completos: 25

TOP 5 CIUDADES MÁS CÁLIDAS
- Rivadavia: 28.0°C
- Orán: 27.4°C
- Pcia. Roque Saenz Peña: 26.7°C
- Tartagal: 26.4°C
- Resistencia: 26.3°C

TOP 5 CIUDADES MÁS FRÍAS
- Base Belgrano II: -28.6°C
- Base San Martín: -24.8°C
- Base Orcadas: -24.3°C
- Base Marambio: -15.5°C
- Base Esperanza: -9.5°C

TOP 5 CIUDADES CON MÁS VIENTO
- Mount Pleasant Airport (Islas Malvinas): 42 km/h
- Perito Moreno: 38 km/h
- Río Gallegos: 37 km/h
- San Julián: 37 km/h
- Comodoro Rivadavia: 33 km/h

TOP 5 CIUDADES CON MENOS VIENTO
- Bolívar: 0 km/h
- Mar del Plata: 0 km/h
- Olavarría: 0 km/h
- Pigué: 0 km/h
- Villa María Del Río Seco: 0 km/h

DATOS FALTANTES POR CAMPO:
- fecha_y_hora: 0 faltantes
- condicion: 0 faltantes
- visibilidad: 0 faltantes
- temperatura: 0 faltantes
- sens_termica: 96 faltantes
- humedad: 0 faltantes
- dir_viento: 0 faltantes
- vel_viento: 0 faltantes
- presion: 0 faltantes

 Horarios de reporte: 09:00, 10:00, 11:00, 12:00, 13:00, 15:00