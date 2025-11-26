import pandas as pd
from fastapi import FastAPI, HTTPException
import uvicorn
from typing import Optional, List

def load_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path, sep=';', encoding='utf-8')
        df['ID'] = df['ID'].astype(str)
        df['Asistencia'] = df['Asistencia'].str.replace('%', '').astype(float) / 100 
        return df
    except FileNotFoundError:
        raise RuntimeError(f"Error: El archivo {file_path} no se encuentra.")
    except Exception as e:
        raise RuntimeError(f"Error al cargar o procesar el archivo CSV: {e}")

# --- 1. Inicialización de la API y Carga de Datos ---
app = FastAPI(
    title="iesazarquiel",
    description="API de consulta de datos de alumnos.",
    version="1.0.0" # Puedes mantener o quitar esto
)

try:
    df_alumnos = load_data('datos_alumnos.csv')
except RuntimeError as e:
    print(e)
    df_alumnos = pd.DataFrame() 

# --- 2. Endpoints ---

@app.get("/info-alumnos", response_model=List[str], tags=["Información General"])
def info_alumnos():
    """Devuelve el listado de IDs de alumnos a consultar."""
    if df_alumnos.empty:
        raise HTTPException(status_code=500, detail="Los datos de alumnos no están cargados.")
        
    return df_alumnos['ID'].tolist()

@app.get("/asistencia", tags=["Asistencia"])
def asistencia(ID: Optional[str] = None):
    """Devuelve el nombre, apellidos y % de asistencia de un alumno por su ID."""
    if df_alumnos.empty:
        raise HTTPException(status_code=500, detail="Los datos de alumnos no están cargados.")
        
    # Mensaje de ayuda si no se especifica el ID
    if ID is None:
        return {
            "mensaje": "Por favor, especifique el ID del alumno para consultar su asistencia.",
            "parámetro_requerido": "ID (opcional, si no se indica, muestra este mensaje de ayuda)",
            "posibles_valores_ID": df_alumnos['ID'].tolist()
        }
        
    # Búsqueda del alumno
    alumno = df_alumnos[df_alumnos['ID'] == ID]
    if alumno.empty:
        raise HTTPException(status_code=404, detail=f"Alumno con ID {ID} no encontrado.")
        
    nombre_completo = f"{alumno['Nombre'].iloc[0]} {alumno['Apellidos'].iloc[0]}"
    asistencia_porcentaje = f"{round(alumno['Asistencia'].iloc[0] * 100, 2)}%"
    
    return {
        "ID": ID,
        "Nombre_Completo": nombre_completo,
        "Asistencia": asistencia_porcentaje
    }

@app.get("/notas", tags=["Notas"])
def notas(ID: Optional[str] = None, nota_consultada: Optional[str] = None):
    """Devuelve el nombre, apellidos y calificación de un alumno en una categoría de nota."""
    if df_alumnos.empty:
        raise HTTPException(status_code=500, detail="Los datos de alumnos no están cargados.")
        
    columnas_notas_validas = [col for col in df_alumnos.columns if col not in ['Apellidos', 'Nombre', 'ID', 'Asistencia']]
    
    # Mensaje de ayuda si no se especifica el ID o la nota
    if ID is None or nota_consultada is None:
        return {
            "mensaje": "Por favor, especifique el ID del alumno y la nota consultada.",
            "parámetros_requeridos": {
                "ID": "ID del alumno (opcional, si no se indica, muestra este mensaje de ayuda)",
                "nota_consultada": "Categoría de la nota (opcional, si no se indica, muestra este mensaje de ayuda)"
            },
            "posibles_valores_ID": df_alumnos['ID'].tolist(),
            "posibles_valores_nota_consultada": columnas_notas_validas
        }

    if nota_consultada not in columnas_notas_validas:
        raise HTTPException(status_code=400, detail=f"Categoría de nota '{nota_consultada}' no válida. Las opciones son: {', '.join(columnas_notas_validas)}")
        
    alumno = df_alumnos[df_alumnos['ID'] == ID]
    if alumno.empty:
        raise HTTPException(status_code=404, detail=f"Alumno con ID {ID} no encontrado.")
        
    nombre_completo = f"{alumno['Nombre'].iloc[0]} {alumno['Apellidos'].iloc[0]}"
    calificacion = alumno[categoria_nota].iloc[0]
    
    return {
        "ID": ID,
        "Nombre_Completo": nombre_completo,
        "Categoría_Nota": nota_consultada,
        "Calificación": calificacion
    }

# --- 3. Arranque de la Aplicación ---

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
