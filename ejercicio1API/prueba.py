import pandas as pd
from fastapi import FastAPI
from typing import Optional, List

# --- Carga de Datos ---
try:
    df = pd.read_csv("uno.csv")
except FileNotFoundError:
    print("Error: El archivo 'uno.csv' no se encontró. Asegúrate de que esté en el mismo directorio.")
    # Crea un DataFrame vacío para evitar errores si no se encuentra el archivo.
    df = pd.DataFrame(columns=['Apellidos', 'Nombre', 'ID', 'Asistencia', 'Parcial1', 'Parcial2', 'Ordinario1', 'Practicas', 'OrdinarioPracticas'])

# Aseguramos que la columna 'ID' sea un tipo de dato que podamos usar como clave
df['ID'] = df['ID'].astype(str)

# --- Inicialización de la API ---
app = FastAPI(title="iesazarquiel - Gestión de Alumnos")

# --- Endpoint 1: info-alumnos ---
@app.get("/info-alumnos")
async def info_alumnos():
    if df.empty:
        return {"error": "No se han podido cargar los datos de alumnos."}
        
    # Devuelve la lista de todos los IDs
    return {"alumnos_ids": df['ID'].tolist()}

# --- Endpoint 2: asistencia ---
@app.get("/asistencia")
async def asistencia(id_alumno: Optional[str] = None):
    if id_alumno is None:
        # Mensaje de información si no se especifica el ID
        return {
            "mensaje": "Endpoint asistencia - Parámetro Requerido (Opcional en la URL)",
            "parametros_posibles": [
                {"parametro": "id_alumno", "tipo": "string", "descripcion": "ID del alumno a consultar.", "ejemplo": f"/asistencia?id_alumno={df['ID'].iloc[0]}" if not df.empty else "/asistencia?id_alumno=1001"}
            ]
        }
    
    # Busca el alumno por ID
    alumno = df[df['ID'] == id_alumno]
    if alumno.empty:
        return {"error": f"Alumno con ID {id_alumno} no encontrado."}
    
    # Extrae los datos
    nombre_completo = f"{alumno['Nombre'].iloc[0]} {alumno['Apellidos'].iloc[0]}"
    asistencia_porcentaje = f"{alumno['Asistencia'].iloc[0] * 100:.1f}%"
    return {
        "id_alumno": id_alumno,
        "nombre_completo": nombre_completo,
        "porcentaje_asistencia": asistencia_porcentaje
    }

# --- Endpoint 3: notas ---
@app.get("/notas")
async def notas(id_alumno: Optional[str] = None, nota_consultada: Optional[str] = None):
    categorias_notas = ['Parcial1', 'Parcial2', 'Ordinario1', 'Practicas', 'OrdinarioPracticas']
    # Verifica si falta algún parámetro
    if id_alumno is None or nota_consultada is None:
        return {
            "mensaje": "Endpoint notas - Parámetros Requeridos (Opcionales en la URL)",
            "parametros_posibles": [
                {"parametro": "id_alumno", "tipo": "string", "descripcion": "ID del alumno a consultar.", "ejemplo": f"id_alumno={df['ID'].iloc[0]}" if not df.empty else "id_alumno=1001"},
                {"parametro": "nota_consultada", "tipo": "string", "descripcion": "La categoría de nota a consultar.", "valores_posibles": categorias_notas}
            ],
            "ejemplo_url": f"/notas?id_alumno={df['ID'].iloc[0]}&nota_consultada=Parcial1" if not df.empty else "/notas?id_alumno=1001&nota_consultada=Parcial1"
        }
        
    # 1. Valida la categoría de la nota
    if nota_consultada not in categorias_notas:
        return {
            "error": "Categoría de nota no válida.",
            "categorias_permitidas": categorias_notas
        }
    
    # 2. Busca el alumno por ID
    alumno = df[df['ID'] == id_alumno]
    if alumno.empty:
        return {"error": f"Alumno con ID {id_alumno} no encontrado."}
        
    # 3. Extrae los datos
    nombre_completo = f"{alumno['Nombre'].iloc[0]} {alumno['Apellidos'].iloc[0]}"
    calificacion = alumno[nota_consultada].iloc[0]
    
    return {
        "id_alumno": id_alumno,
        "nombre_completo": nombre_completo,
        "categoria_nota": nota_consultada,
        "calificacion": float(calificacion)
    }