import sqlite3

# Crear o conectar la base de datos local
conexion = sqlite3.connect("base_datos.db")
cursor = conexion.cursor()

# Crear tabla de alumnos
cursor.execute("""
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT UNIQUE,
    nombres_apellidos TEXT,
    dni TEXT,
    curso TEXT,
    turno TEXT,
    estado_pago TEXT DEFAULT 'Al día',
    sede TEXT
)
""")

# Crear tabla de asistencias
cursor.execute("""
CREATE TABLE IF NOT EXISTS asistencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    alumno_id INTEGER,
    hora_ingreso TEXT,
    fecha_ingreso TEXT,
    hora_salida TEXT,
    fecha_salida TEXT,
    FOREIGN KEY(alumno_id) REFERENCES alumnos(id)
)
""")

conexion.commit()
conexion.close()

print("✅ Base de datos creada correctamente (base_datos.db)")
