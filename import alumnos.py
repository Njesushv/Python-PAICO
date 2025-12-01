import sqlite3

conn = sqlite3.connect("base_datos.db")
cur = conn.cursor()

cur.execute("""
INSERT INTO alumnos (codigo, nombres_apellidos, dni, curso, turno, estado_pago, sede)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", ("ELEC001", "Juan Pérez López", "12345678", "Electrónica", "Mañana", "Al día", "Sede Central"))

conn.commit()
conn.close()

print("✅ Alumno agregado")
