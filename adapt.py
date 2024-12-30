import csv

# Ruta del archivo
input_file = 'DatosGLPI.csv'
output_file = 'DatosGLPINov2024.csv'

def ajustar_columnas(fila, num_columnas=25):
    """Agrega columnas vacías para asegurar que la fila tenga el número correcto de columnas."""
    while len(fila) < num_columnas:
        fila.append('')
    return fila

# Detectar y conservar la codificación original
with open(input_file, 'rb') as infile:
    raw_data = infile.read()
    encoding = 'utf-8-sig' if raw_data.startswith(b'\xef\xbb\xbf') else 'latin1'

# Leer el archivo con la codificación detectada
with open(input_file, 'r', encoding=encoding, errors='strict') as infile:
    reader = csv.reader(infile)
    filas = []

    for fila in reader:
        filas.append(ajustar_columnas(fila))

# Ordenar las filas por ID
encabezado = filas[0]
filas_datos = filas[1:]
filas_datos.sort(key=lambda x: int(x[0]) if x[0].isdigit() else float('inf'))

# Guardar el archivo corregido en UTF-8 con BOM
with open(output_file, 'w', newline='', encoding='utf-8-sig') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(encabezado)
    writer.writerows(filas_datos)

print(f"Archivo procesado correctamente. Guardado como {output_file} en UTF-8 con BOM.")
