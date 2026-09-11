La idea de este proyecto es obtener una serie de datos a partir de las observaciones actuales del Servicio Meteorológico Nacional. El objetivo es crear una herramienta de líneas de comandos que interprete las observaciones y guarde los datos en un diccionario indexado por ciudad/estación, y calcule características y estadísticas generales sobre esos datos (estaciones leídas, datos faltantes, columnas ausentes, temperaturas y vientos extremos, rankings de ciudades).



Las observaciones del SMN se obtienen de su página web (https://www.smn.gob.ar/descarga-de-datos), en la página debes aceptar los TyC para poder acceder a los datos y se descarga el 'Estado del Tiempo Presente' en el apartado de 'Descarga de datos actuales: \[fecha]'. Esto te da un .zip que al descomprimirlo se obtiene el archivo .txt con los datos meteorológicos del día.

